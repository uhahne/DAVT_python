from collections import Counter 
import math
import os
import requests


def get_character_counts(text):
    """simply use the Counter class from the collections module to count the occurrences of each character"""
    return Counter(text)

def load_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

# arithmetic encoding
def encode(message, frequencies, cumulative_frequencies):
    # initialize the interval
    low = 0
    high = 1
    # encode the message
    for char in message:
        # calculate the range
        range = high - low
        # calculate the new high and low values
        high = low + range * (cumulative_frequencies[char] + frequencies[char])
        low = low + range * cumulative_frequencies[char]
    return (low + high) / 2

def get_code_from_interval(interval):
    code = ""
    while interval != 0:
        interval *= 2
        if interval >= 1:
            code += "1"
            interval -= 1
        else:
            code += "0"
    return code

def decode(encoded_message, frequencies, cumulative_frequencies, total):
    message = ""
    interval = encoded_message
    while True:
        for char, freq in frequencies.items():
            if cumulative_frequencies[char] <= interval * total < cumulative_frequencies[char] + freq:
                message += char
                low = cumulative_frequencies[char] / total
                high = (cumulative_frequencies[char] + freq) / total
                interval = (interval - low) / (high - low)
                break
        # check if the message contains end of message character and break the loop
        if message.endswith("_"):
            break
    return message

def decode_bin(encoded_message, frequencies, cumulative_frequencies):
    message = ""
    interval = int(encoded_message, 2) / (2 ** len(encoded_message))
    while True:
        for char, freq in frequencies.items():
            if cumulative_frequencies[char] <= interval < cumulative_frequencies[char] + freq:
                message += char
                low = cumulative_frequencies[char] 
                high = (cumulative_frequencies[char] + freq)
                interval = (interval - low) / (high - low)
                break
        # check if the message contains end of message character and break the loop
        if message.endswith("_"):
            break
    return message

def decode_with_length(encoded_message, frequencies, cumulative_frequencies, length):
    message = ""
    interval = encoded_message
    while len(message) < length:
        for char, freq in frequencies.items():
            if cumulative_frequencies[char] <= interval < cumulative_frequencies[char] + freq:
                message += char
                low = cumulative_frequencies[char]
                high = (cumulative_frequencies[char] + freq)
                interval = (interval - low) / (high - low)
                break
    return message


if __name__ == "__main__":
    # use _ as end of message character
    original_msg = "AABBBBBBBC"
    print("Original message:", original_msg)


    # prepare arithmetic coding
    frequencies = get_character_counts(original_msg)
    print("Character Frequencies:", frequencies)
    # calculate the total number of characters
    total = sum(frequencies.values())
    # calculate probabilities
    for char, freq in frequencies.items():
        frequencies[char] = freq / total
    print("Character probabilities:", frequencies)
    # calculate the cumulative frequencies
    frequencies = dict(sorted(frequencies.items(), key=lambda item: item[0], reverse=False))
    cumulative_frequencies = {}
    cumulative_frequency = 0
    for char, freq in frequencies.items():
        cumulative_frequencies[char] = cumulative_frequency
        cumulative_frequency += freq

    # run arithmetic coding
    original_msg ="ABC"
    arithmetic_code = encode(original_msg, frequencies, cumulative_frequencies)
    print("Arithmetic Code:", arithmetic_code)
    print("Encoded message:", get_code_from_interval(arithmetic_code))

    # test decoding
    decoded_msg = decode_with_length(arithmetic_code, frequencies, cumulative_frequencies, len(original_msg))
    print("Decoded message:", decoded_msg)
    # if the decoding fails, the precision might be the issue
    print("Message Decoded Successfully? {result}".format(result=original_msg == decoded_msg))

    # test binary decoding
    # decoded_msg = decode_bin(get_code_from_interval(arithmetic_code), frequencies, cumulative_frequencies)
    # print("Decoded message:", decoded_msg)
    # # if the decoding fails, the precision might be the issue
    # print("Message Decoded Successfully? {result}".format(result=original_msg == decoded_msg))
