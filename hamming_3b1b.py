from functools import reduce
import numpy as np

def hamming_syndrom(bits):
    return reduce(
        # Reduce by xor
        lambda x, y: x ^ y,
        # all indices of bits that are 1
        [i for i, b in enumerate(bits) if b]
    )

def hamming_correct(bits, syndrome):
    if syndrome == 0:
        return bits
    else:
        bits[syndrome] ^= 1
        return bits

def hamming_initial_correct(bits, syndrome):
    N = np.log2(len(bits) + 1).astype(int)
    # If the syndrome is 0, there is no error
    if syndrome == 0:
        return bits
    # go through all 1s of the binary syndrome 
    # and set the corresponding bit to the opposite
    for i in [2**i - 1 for i in range(N) if syndrome & 2**i]:
        bits[i+1] ^= 1
    return bits

def create_random_error(bits):
    import random
    # Create a random error
    error_index = random.randint(0, len(bits) - 1)
    bits[error_index] ^= 1
    print("Error index:", error_index)
    return bits

def print_bits_with_index(bits):
    # print all indices first in one line
    print("Index:", end=" ")
    for i in range(len(bits)):
        print(f"{i:2}", end=" ")
    print()
    # print all bits in the next line
    print("Bits:  ", end="")
    for bit in bits:
        print(f"{bit:2}", end=" ")
    print()

    
# Example usage
# Create a random 16-bit sequence
bits = np.random.randint(0, 2, 16)
print("Original bits:")
print_bits_with_index(bits)
# Compute the syndrome to find out if the sequence is a valid Hamming code
syndrome = hamming_syndrom(bits)
print("Syndrome:", bin(syndrome))
# Correct the bits if the syndrome is not 0
if syndrome != 0:
    print("Bits need to be corrected.")
    corrected_bits = hamming_initial_correct(bits, syndrome)
else:
    corrected_bits = bits
    print("No error detected.")
print("Corrected bits:")
print_bits_with_index(corrected_bits)
# Show that the bits are corrected
print("Now the syndrom is zero:", hamming_syndrom(corrected_bits))
# Create a random error
bits = create_random_error(bits)
print("Bits with random error:")
print_bits_with_index(bits)
syndrome = hamming_syndrom(bits)
print("Syndrome:", syndrome)
corrected_bits = hamming_correct(bits, syndrome)
print("Corrected bits:")
print_bits_with_index(corrected_bits)
syndrome = hamming_syndrom(bits)
print("Syndrome:", syndrome)