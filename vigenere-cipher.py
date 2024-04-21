def generate_vigenere_table():
    table = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            table[i][j] = (i + j) % 26
    return table

def generate_key(seed, length):
    if isinstance(seed, int):
        import random
        random.seed(seed)
        key = [random.randint(0, 25) for _ in range(length)]
    elif isinstance(seed, str):
        key = [ord(char) - 65 for char in seed.upper()]
    return key
