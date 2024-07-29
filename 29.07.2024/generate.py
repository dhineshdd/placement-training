import random

def generate_random_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]
