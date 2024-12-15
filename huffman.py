import heapq
from collections import Counter
import math
import os
import requests

class HuffmanNode:
    """Node class for the Huffman tree with a character, frequency, left and right child"""
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

def get_character_counts(text):
    """simply use the Counter class from the collections module to count the occurrences of each character"""
    return Counter(text)

def build_huffman_tree(frequencies):
    """Builds a Huffman tree from a dictionary of character frequencies using the Heap queue algorithm (a.k.a. priority queue)."""
    # Create a min heap
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Go through the tree from the bottom up
    while len(heap) > 1:
        # remove the two smallest nodes
        smallest_node = heapq.heappop(heap)
        second_smallest_node = heapq.heappop(heap)
        # merge them into a new node
        merged_node = HuffmanNode(None, smallest_node.freq + second_smallest_node.freq)
        merged_node.left = smallest_node
        merged_node.right = second_smallest_node
        # push the new node back into the heap
        heapq.heappush(heap, merged_node)

    return heap[0]

def generate_huffman_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", codebook)
        generate_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def load_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def make_canonical_huffman_tree(huffman_tree):
    # create a list of lists to store the nodes at each level of the tree
    levels = []
    # create a list to store the nodes at the current level
    current_level = [huffman_tree]
    # iterate through the tree level by level
    while current_level:
        # add the current level to the levels list
        levels.append(current_level)
        # create a list to store the nodes at the next level
        next_level = []
        # iterate through the nodes at the current level
        for node in current_level:
            # add the left and right children of the current node to the next level
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        # set the current level to the next level
        current_level = next_level
    # sort the nodes at each level by their frequency
    for level in levels:
        level.sort(key=lambda node: node.freq)
    # create a dictionary to store the canonical codes
    canonical_codes = {}
    # iterate through the levels in reverse order
    

def encode(message, huffman_dict):
    return ''.join(huffman_dict[char] for char in message)


def decode(encoded_message, huffman_dict):
    # create a reverse dictionary for decoding
    reverse_dict = {v: k for k, v in huffman_dict.items()}
    # decode the message
    current_code = ''
    decoded_message = ''
    for bit in encoded_message:
        current_code += bit
        # check if the current code is in the reverse dictionary
        if current_code in reverse_dict:
            decoded_message += reverse_dict[current_code]
            current_code = ''
    return decoded_message


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
    frequencies = get_character_counts(text)
    print("Character Frequencies:", frequencies)

    # print sum of all character frequencies
    print("Sum of all character frequencies:", sum(frequencies.values()))
    
    # print the entropy of the text
    entropy = -sum([freq/sum(frequencies.values()) * math.log2(freq/sum(frequencies.values())) for freq in frequencies.values()])
    print("Entropy:", entropy)

    huffman_tree = build_huffman_tree(frequencies)
    huffman_tree.display()

    huffman_codes = generate_huffman_codes(huffman_tree)
    print("Huffman Codes:", huffman_codes)

    # get mean code length
    mean_code_length = sum([len(code) * freq for char, freq in frequencies.items() for char_code, code in huffman_codes.items() if char == char_code])/sum(frequencies.values())
    print("Mean Code Length:", mean_code_length)

    # test encoding and decoding
    message = "ABC"
    print("Original message:", message)

    encoded_message = encode(message, huffman_codes)
    print("Encoded message:", encoded_message)

    decoded_message = decode(encoded_message, huffman_codes)
    print("Decoded message:", decoded_message)