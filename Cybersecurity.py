def generate_keystream(seed, length):
    if isinstance(seed, int):
        # Të zbatohet kufiri 32-bit në seed
        seed = seed % (2**32)
        import random
        random.seed(seed)
        keystream = [random.randint(0, 255) for _ in range(length)]