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