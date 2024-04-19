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

# 2. Enkriptimi i plainteksitit, ku cdo karakter hyn vec e vec dhe iterohet ne fund me XOR per enkriptim me te sigurt.
    def vigenere_encrypt(plaintext, keystream):
        ciphertext = []
    for i, char in enumerate(plaintext):
        key = keystream[i % len(keystream)]
        encrypted_char = (char + key) % 256  # Perdorimi i XOR.
        ciphertext.append(encrypted_char)
    return bytes(ciphertext)

# 3. Dekriptimi i cipherteksit.
    def vigenere_decrypt(ciphertext, keystream):
        plaintext = []
    for i, char in enumerate(ciphertext):
        key =keystream[i% len(keystream)]
        decrypted_char = (char-key) % 256  # Perdorim XOR edhe ne dekriptim pasi perdorem edhe gjat enkriptimit, ashtu qe te jete simetrik.
        plaintext.append(decrypted_char)
    return bytes(plaintext)



