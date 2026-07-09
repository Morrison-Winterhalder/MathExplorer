from math import isqrt

NAME = "Pentagonal"
DESCRIPTION = "Terms are pentagonal numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"


def recognize(sequence):
    if len(sequence) == 0:
        return None

    for value in sequence:
        discriminant = 1 + 24 * value
        root = isqrt(discriminant)

        if root * root != discriminant:
            return False

        n = (1 + root) / 6

        if not n.is_integer():
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (3 * n - 1) // 2


def formula(_):
    return "a(n) = n(3n - 1)/2"


def complexity(_):
    return 2