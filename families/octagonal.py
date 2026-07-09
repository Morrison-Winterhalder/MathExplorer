from math import isqrt

NAME = "Octagonal"
DESCRIPTION = "Octagonal figurate numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        value = 3 * term + 1
        root = isqrt(value)

        if root * root != value:
            return False

        if (1 + root) % 3 != 0:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (3 * n - 2)

def formula(_):
    return "a(n) = n(3n - 2)"

def complexity(_):
    return 2