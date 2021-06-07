import math


def add(vector1, vector2):
    return tuple(sum(x) for x in zip(vector1, vector2))


def sub(vector1, vector2):
    return tuple(x - y for x, y in zip(vector1, vector2))


def dist(vector1, vector2):
    return math.sqrt(sum((x - y)**2 for x, y in zip(vector1, vector2)))


def limit(vector, magnitude):
    current = math.sqrt(sum(element ** 2 for element in vector))
    if current > magnitude:
        return tuple(map(lambda x: x / (current / magnitude), vector))
    return vector
