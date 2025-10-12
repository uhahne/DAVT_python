import math

# the message
message = 'DDDBBADDCCCBBADABB'

# compute the proportion of each sign in the message
def get_prop(message, sign ):
    return message.count(sign) / len(message)

# get the proportion of each sign in the message
pA = get_prop(message, 'A')
pB = get_prop(message, 'B')
pC = get_prop(message, 'C')
pD = get_prop(message, 'D')

print() # empty line
print('Probabilities:')
print(pA, pB, pC, pD)
print() # empty line

# compute the entropy
H = -pA * math.log2(pA) - pB * math.log2(pB) - pC * math.log2(pC) - pD * math.log2(pD)
print() # empty line
print('Entropy:')
print(H)
print() # empty line