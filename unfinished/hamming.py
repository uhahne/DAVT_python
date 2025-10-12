def calculate_parity_bits(data_bits):
    n = len(data_bits)
    r = 0

    while (2**r) < (n + r + 1):
        r += 1

    return r

def insert_parity_bits(data_bits, r):
    j = 0
    k = 1
    m = len(data_bits)
    res = ''

    for i in range(1, m + r + 1):
        if i == 2**j:
            res = res + '0'
            j += 1
        else:
            res = res + data_bits[-1 * k]
            k += 1

    return res[::-1]

def calculate_hamming_code(data_bits):
    m = len(data_bits)
    r = calculate_parity_bits(data_bits)
    arr = insert_parity_bits(data_bits, r)
    n = len(arr)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-1 * j])

        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]

    return arr

def main():
    data_bits = '10101'  # Example 5-bit data
    hamming_code = calculate_hamming_code(data_bits)
    print(f"Data bits: {data_bits}")
    print(f"Hamming code: {hamming_code}")

if __name__ == "__main__":
    main()