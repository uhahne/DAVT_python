def compute_parity(binary_string):
    parity = 0
    for bit in binary_string:
        parity ^= int(bit)
    return parity

def compute_parity_in_one_line(binary_string):
    return sum(int(bit) for bit in binary_string) % 2 

# Example usage
binary_string = "10101101"
print(f"The parity of {binary_string} is {compute_parity(binary_string)}")
print(f"The parity of {binary_string} is {compute_parity_in_one_line(binary_string)}")