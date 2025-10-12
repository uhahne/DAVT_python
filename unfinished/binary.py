def float_to_binary(num, precision=10):
    if num >= 1 or num <= 0:
        return "ERROR"

    binary = "0."
    while num > 0:
        if len(binary) >= precision + 2:
            break

        num *= 2
        if num >= 1:
            binary += "1"
            num -= 1
        else:
            binary += "0"

    return binary

# Example usage:
print(float_to_binary(0.173))