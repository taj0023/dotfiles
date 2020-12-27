state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def add_round_key(state, key):
    return bytes2matrix([(s^k) for s, k in list(zip(sum(state, []), sum(key, [])))])
    # XORing and matrix2bytes in same function.............YES I am a genius 


t = add_round_key(state, round_key)
print(bytes2matrix(t))
