# this is the implementation of CRC-8 by Stefan Filipek from https://srfilipek.medium.com/on-correcting-bit-errors-with-crcs-1f1c98fc58b

def crc8_error_table(num_bytes: int, poly: int, rem: int=0):
    table = {}
    error = bytearray(num_bytes)

    for bit in range(num_bytes * 8):
        error[bit // 8] = 0x80 >> (bit % 8)
        syndrome = crc8(error, poly, rem)

        assert syndrome not in table
        table[syndrome] = bit

        error[bit // 8] = 0

    return table

def crc8(data: bytes, poly: int, rem: int=0):
    for byte in data:
        # Add the data and remainder from the last division operation
        rem ^= byte

        # Perform long division over this byte
        for _ in range(8):
            rem <<= 1

            # Should we subtract the divisor (polynomial)?
            if rem & 0x100:
                rem ^= poly | 0x100

    return rem

def print_bits(value: int, bits: int=8):
    """Prints the bits of an integer value."""
    print(f"{value:0{bits}b}")

poly = 0x31
message = b'foobar'
bad_1 = b'\xe6oobar' # Bit 0 flipped
bad_2 = b'foobas' # Bit 47 flipped
bad_3 = b'fonbar' # Bit 23 flipped
print_bits(poly)
#, message, bad_1, bad_2, bad_3)

check = crc8(message, poly)
bad_check_1 = crc8(bad_1, poly)
bad_check_2 = crc8(bad_2, poly)
bad_check_3 = crc8(bad_3, poly)
print(check, bad_check_1, bad_check_2, bad_check_3)

table = crc8_error_table(len(message), poly)
print(table[check ^ bad_check_1])
print(table[check ^ bad_check_2])
print(table[check ^ bad_check_3])

# Example from lecture
poly = 0x05
message = b'Hi'
bad = b'Hh' # Bit 15 flipped
print_bits(poly)
check = crc8(message, poly)
bad_check = crc8(bad, poly)
print(check, bad_check)
table = crc8_error_table(len(message), poly)
print(table[check ^ bad_check])
