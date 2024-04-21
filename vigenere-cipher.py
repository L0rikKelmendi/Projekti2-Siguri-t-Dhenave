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

def encrypt(plaintext, key):
    ciphertext = ""
    table = generate_vigenere_table()
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            key_index = i % len(key)
            shift = key[key_index]
            if plaintext[i].islower():
                ciphertext += chr((ord(plaintext[i]) - 97 + shift) % 26 + 97)
            else:
                ciphertext += chr((ord(plaintext[i]) - 65 + shift) % 26 + 65)
        else:
            ciphertext += plaintext[i]
    return ciphertext


