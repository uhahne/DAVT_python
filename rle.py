def rle_encode(data):
    encoding = ''
    i = 0

    while i < len(data):
        count = 1

        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1

        encoding += str(count) + data[i]
        i += 1

    return encoding

def rle_decode(data):
    decoding = ''
    i = 0

    while i < len(data):
        count = int(data[i])
        i += 1
        decoding += data[i] * count
        i += 1

    return decoding

# Example usage:
if __name__ == "__main__":
    original_string = "AAAABBBCCDAA"
    encoded_string = rle_encode(original_string)
    decoded_string = rle_decode(encoded_string)

    print(f"Original: {original_string}")
    print(f"Encoded: {encoded_string}")
    print(f"Decoded: {decoded_string}")