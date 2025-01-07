import random

# From wikipedia: https://en.wikipedia.org/wiki/Cyclic_redundancy_check

def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    print(input_padded_array)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]

def crc_check(input_bitstring, polynomial_bitstring, check_value):
    """Calculate the CRC check of a string of bits using a chosen polynomial."""
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
            = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ('1' not in ''.join(input_padded_array)[len_input:])

def addOneBitError(data):
    data = list(data)
    index = random.randint(0, len(data) - 1)
    data[index] = '1' if data[index] == '0' else '0'
    return ''.join(data)

# Example usage
data = "10001011" # Original data
key = "101011" # Prüfpolynom


print("Original data: ", data)
print("Key: ", key)
remainder = crc_remainder(data, key, '0')
print("Remainder: ", remainder)

if crc_check(data, key, remainder):
    print("No error detected in the received data.")
else:
    print("Error detected in the received data.")

# change encoded data to simulate error
wrong_data = addOneBitError(data)

if crc_check(wrong_data, key, remainder):
    print("No error detected in the received data.")
else:
    print("Error detected in the received data.")