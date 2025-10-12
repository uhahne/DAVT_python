import numpy as np

def gf_add(x, y, p):
    return x ^ y

def gf_sub(x, y, p):
    return x ^ y

def gf_mul(x, y, p):
    r = 0
    while y:
        if y & 1:
            r ^= x
        y >>= 1
        x <<= 1
        if x & (1 << p):
            x ^= 0x11b
    return r

def gf_div(x, y, p):
    r = 0
    while x >= y:
        shift = x.bit_length() - y.bit_length()
        r ^= 1 << shift
        x ^= y << shift
    return r

def gf_pow(x, power, p):
    r = 1
    for _ in range(power):
        r = gf_mul(r, x, p)
    return r

def gf_inv(x, p):
    return gf_pow(x, 2**p - 2, p)

def lagrange_interpolation(x, y, p):
    k = len(x)
    assert k == len(y)
    result = [0] * k
    for i in range(k):
        terms = [1]
        for j in range(k):
            if i != j:
                terms = np.convolve(terms, [gf_sub(0, x[j], p), 1])
                denom = gf_sub(x[i], x[j], p)
                terms = [gf_div(int(term), int(denom), p) for term in terms]
        result = [gf_add(result[j], gf_mul(terms[j], y[i], p), p) for j in range(k)]
    return result

def reed_solomon_encode(data, n, k, p):
    x = list(range(k))
    y = data
    poly = lagrange_interpolation(x, y, p)
    return poly + [0] * (n - k)

def reed_solomon_decode(data, n, k, p):
    x = list(range(n))
    y = data
    poly = lagrange_interpolation(x, y, p)
    return poly[:k]

# Example usage
p = 8  # GF(2^8)
data = [32, 45, 12, 89]
n = 7
k = 4

encoded = reed_solomon_encode(data, n, k, p)
print("Encoded:", encoded)

decoded = reed_solomon_decode(encoded, n, k, p)
print("Decoded:", decoded)