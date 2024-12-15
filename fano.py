from collections import Counter
from itertools import islice
import math
import os

import requests


class ShannonFanoNode:
    """Node class for the Shannon-Fano tree with a character, frequency, left and right child"""
    def __init__(self, char, freq):
        """Initializes the node with a character and its frequency"""
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Defines the less than operator to compare nodes based on their frequency"""
        return self.freq < other.freq

    # Display function copied and adjusted from https://stackoverflow.com/a/54074933 
    # by user "J. V." https://stackoverflow.com/users/1143396/j-v
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.char
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % (self.char if not "None" else ".")
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % (self.char if not "None" else ".")
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % (self.char if not "None" else ".")
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def build_tree(frequencies):
    """Builds the Shannon-Fano tree from a dictionary of character frequencies"""
    if len(frequencies) == 1:
        temp_list = list(frequencies.items())
        return ShannonFanoNode(temp_list[0][0], temp_list[0][1])

    total_frequency, left_symbols, right_symbols = split_frequencies(frequencies)
    
    node = ShannonFanoNode(None, total_frequency)
    node.left = build_tree(left_symbols)
    node.right = build_tree(right_symbols)

    return node

def split_frequencies(frequencies):
    total_frequency = sum(frequencies.values())
    cumulative_frequency = 0
    split_index = 0
    index = 0

    
    # find the index at which the cumulative frequency is greater than or equal to half of the total frequency
    for char, freq in (frequencies.items()):
        cumulative_frequency += freq
        index += 1
        if cumulative_frequency >= total_frequency / 2:
            split_index = index
            break
    

    # split the frequencies dictionary into two parts    
    left_symbols = dict(list(frequencies.items())[:split_index])
    right_symbols = dict(list(frequencies.items())[split_index:])
    return total_frequency,left_symbols,right_symbols


def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def get_codes(node, codes={}):
    if node is not None:
        if node.symbol is not None:
            codes[node.symbol] = node.code
        get_codes(node.left, codes)
        get_codes(node.right, codes)
    return codes

def get_character_counts(text):
    """simply use the Counter class from the collections module to count the occurrences of each character"""
    return Counter(text)


if __name__ == "__main__":
    # download the tiny shakespeare dataset (from Andrey Karpathy's char-rnn)
    input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    if not os.path.exists(input_file_path):
        data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
        with open(input_file_path, 'w', encoding='utf-8') as f:
            f.write(requests.get(data_url).text)

    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # remove whitespaces and newlines
    text = ''.join(text.split())
    # remove special characters
    text = ''.join(e for e in text if e.isalnum())
    # make all characters uppercase
    text = text.upper()

    # Uncomment to use an alternative text for testing
    # text = "AAAABCCD"

    # get the character frequencies
    frequencies = get_character_counts(text)
    print("Character Frequencies:", frequencies)

    # sort the frequencies in descending order
    frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

    # print sum of all character frequencies
    print("Sum of all character frequencies:", sum(frequencies.values()))
    
    # print the entropy of the text
    entropy = -sum([freq/sum(frequencies.values()) * math.log2(freq/sum(frequencies.values())) for freq in frequencies.values()])
    print("Entropy:", entropy)

    # build the Shannon-Fano tree
    shannon_fano_tree = build_tree(frequencies)
    shannon_fano_tree.display()

    # generate the Shannon-Fano codes
    shannon_fano_codes = generate_codes(shannon_fano_tree)
    print("Shannon-Fano Codes:", shannon_fano_codes)

    # get mean code length
    mean_code_length = sum([len(code) * freq for char, freq in frequencies.items() for char_code, code in shannon_fano_codes.items() if char == char_code])/sum(frequencies.values())
    print("Mean Code Length:", mean_code_length)