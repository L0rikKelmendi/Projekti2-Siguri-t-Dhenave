# Ky funksion gjeneron një tabelë 26x26 që përfaqëson Vigenere cipher.
# Çdo rresht përfaqëson një shifër të Cezarit me një vlerë të ndryshëm.

def generate_vigenere_table():
    table = [[0] * 26 for _ in range(26)] # Inicializon tabelën me zero
    for i in range(26):
        for j in range(26):
            table[i][j] = (i + j) % 26 # Plotëson tabelën me vlerat e duhura sipas Vigenere cipher.
    return table

# Ky funksion gjeneron një çelës për shifrën Vigenere bazuar në një vlerë seed.
# Nëse seed-i është një numër i plotë, ai gjeneron një çelës të rastësishëm të gjatësisë së specifikuar duke përdorur modulin 'random'.
# Nëse seed-i është një varg, ai konverton çdo karakter në vlerën e tij ASCII dhe zbret 65 (vlera ASCII e 'A') për të marrë vlerën kryesore.

def generate_key(seed, length):
    if isinstance(seed, int):
        import random
        random.seed(seed)
        key = [random.randint(0, 25) for _ in range(length)] # Gjeneron një çelës të rastësishëm ( random ).
    elif isinstance(seed, str):
        key = [ord(char) - 65 for char in seed.upper()] # Konverton çdo karakter në vlerën e tij ASCII dhe i zbret 65.
    return key


# Ky funksion enkripton një mesazh me tekst të thjeshtë (plain) duke përdorur shifrën Vigenere.
# Përsëritet mbi çdo karakter në tekstin e thjeshtë (plain), dhe nëse karakteri është alfabetik,
# Aplikon shifrën Vigenere duke përdorur vlerën e çelësit përkatës.
# Vlera kryesore përcaktohet nga pozicioni i karakterit në modulin e tekstit të thjeshtë, gjatësia e tekstit.
# Karakteret e enrkiptuara më pas i shtohet vargut të tekstit të enkriptuar.

def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            key_index = i % len(key) # Përcaktoni vlerën kryesore bazuar në pozicionin e karakterit.
            shift = key[key_index]
            if plaintext[i].islower():
                ciphertext += chr((ord(plaintext[i]) - 97 + shift) % 26 + 97) # Aplikoni shifrën Vigenere për shkronjat e vogla.
            else:
                ciphertext += chr((ord(plaintext[i]) - 65 + shift) % 26 + 65) # Aplikoni shifrën Vigenere për shkronjat e mëdha.
        else:
            ciphertext += plaintext[i] # Shton karaktere jo alfabetike ashtu siç janë.
    return ciphertext

# Ky funksion deshifron një mesazh të enkriptuar me tekst duke përdorur Vigenere cipher.
# Funksionon në mënyrë të ngjashme me funksionin 'encrypt', por zbaton inversin e shifrës Vigenere për çdo karakter.
def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            key_index = i % len(key) # Përcaktoni vlerën e qelsit bazuar në pozicionin e karakterit.
            shift = key[key_index]
            if ciphertext[i].islower():
                plaintext += chr((ord(ciphertext[i]) - 97 - shift) % 26 + 97) # Aplikoni shifrën e kundërt (inverse) Vigenere për shkronjat e vogla.
            else:
                plaintext += chr((ord(ciphertext[i]) - 65 - shift) % 26 + 65) # Aplikoni shifrën e kundërt Vigenere për shkronjat e mëdha.
        else:
            plaintext += ciphertext[i] # Shkruaj karakteret jo alfabetike ashtu siç janë
    return plaintext
