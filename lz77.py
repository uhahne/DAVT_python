class LZ77Compressor:
    def __init__(self, window_size=20):
        self.window_size = window_size

    def compress(self, data):
        i = 0
        output_buffer = []

        while i < len(data):
            match = self.find_longest_match(data, i)

            if match:
                (best_match_distance, best_match_length) = match
                output_buffer.append((best_match_distance, best_match_length, data[i + best_match_length]))
                i += best_match_length + 1
            else:
                output_buffer.append((0, 0, data[i]))
                i += 1

        return output_buffer

    def decompress(self, compressed_data):
        decompressed_data = []
        for item in compressed_data:
            (distance, length, char) = item
            if distance == 0 and length == 0:
                decompressed_data.append(char)
            else:
                start = len(decompressed_data) - distance
                for i in range(length):
                    decompressed_data.append(decompressed_data[start + i])
                decompressed_data.append(char)

        return ''.join(decompressed_data)

    def find_longest_match(self, data, current_position):
        end_of_buffer = min(current_position + self.window_size, len(data) + 1)

        best_match_distance = -1
        best_match_length = -1

        for j in range(current_position + 2, end_of_buffer):
            start_index = max(0, current_position - self.window_size)
            substring = data[current_position:j]

            for i in range(start_index, current_position):
                match_length = 0
                while (match_length < len(substring) and
                       data[i + match_length] == substring[match_length]):
                    match_length += 1

                if match_length > best_match_length:
                    best_match_distance = current_position - i
                    best_match_length = match_length

        if best_match_distance > 0 and best_match_length > 0:
            return best_match_distance, best_match_length
        return None

if __name__ == "__main__":
    compressor = LZ77Compressor()
    data = "TOBEORNOTTOBEZ"
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)

    print("Original:", data)
    print("Compressed:", compressed)
    print("Decompressed:", decompressed)