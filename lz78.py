class LZ78:
    def __init__(self):
        self.dictionary = {}
        self.data = ""
        self.result = []

    def compress(self, data):
        self.dictionary = {}
        self.data = data
        self.result = []
        current_string = ""
        dict_size = 1

        for char in data:
            combined_string = current_string + char
            if combined_string in self.dictionary:
                current_string = combined_string
            else:
                if current_string:
                    self.result.append((self.dictionary[current_string], char))
                else:
                    self.result.append((0, char))
                self.dictionary[combined_string] = dict_size
                dict_size += 1
                current_string = ""

        if current_string:
            self.result.append((self.dictionary[current_string], ""))

        return self.result

    def decompress(self, compressed_data):
        self.dictionary = {0: ""}
        self.result = ""
        dict_size = 1

        for index, char in compressed_data:
            entry = self.dictionary[index] + char
            self.result += entry
            self.dictionary[dict_size] = entry
            dict_size += 1

        return self.result

# Example usage:
lz78 = LZ78()
original_data = "AABABBABBAABA"
print("Original Data:", original_data)
compressed = lz78.compress(original_data)
print("Compressed:", compressed)
print("Dictionary:", lz78.dictionary)
decompressed = lz78.decompress(compressed)
print("Decompressed:", decompressed)