import numpy as np

def cross_product(vector_a, vector_b):
    return np.cross(vector_a, vector_b)

# Example usage
vector_u = [1, 0, 0]
vector_v = [0, np.sqrt(3)/2, -1/2]
vector_w = [0, 1/2, np.sqrt(3)/2]
result = cross_product(vector_u, vector_v)
print(f"Cross product of {vector_u} and {vector_v} is {result}")
result = cross_product(vector_u, vector_w)
print(f"Cross product of {vector_u} and {vector_w} is {result}")
result = cross_product(vector_v, vector_w)
print(f"Cross product of {vector_v} and {vector_w} is {result}")

vector_a = [0, 1, 1]
vector_b = [2, 0, -1]
result = cross_product(vector_a, vector_b)
print(f"Cross product of {vector_a} and {vector_b} is {result}")