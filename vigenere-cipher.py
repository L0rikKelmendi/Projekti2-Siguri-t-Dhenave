# 1. Hapi pare - gjenerojme celesin nga keystream duke perdorur nje int32 ose string si seed.
    import random
    
    def generate_keystream(seed, length):
    if isinstance(seed, int):
        # Të zbatohet kufiri 32-bit në seed
        seed = seed % (2**32)
        random.seed(seed)
        keystream = [random.randint(0, 255) for _ in range(length)]
        elif isinstance(seed, str):
        keystream = [ord(char) for char in seed]
          while len(keystream) < length:
            keystream.extend([ord(char) for char in seed])
        keystream = keystream[:length]
    else:
        raise TypeError("Fara duhet të jetë ose një numër i plotë ose një varg")
    return keystream

def vigenere_encrypt(plaintext, keystream):
    ciphertext = []
    for i, char in enumerate(plaintext):
        key = keystream[i % len(keystream)]
        encrypted_char = (char + key) % 256  # Use XOR instead of addition
        ciphertext.append(encrypted_char)
    return bytes(ciphertext)



