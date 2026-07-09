from math import isqrt

NAME = "Pronic"
DESCRIPTION = "Pronic (oblong) numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 50
PARENT = "Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        value = 4 * term + 1
        root = isqrt(value)

        if root * root != value:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (n + 1)

def formula(_):
    return "a(n) = n(n + 1)"

def complexity(_):
    return 2