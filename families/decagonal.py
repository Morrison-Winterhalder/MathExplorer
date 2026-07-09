from math import isqrt

NAME = "Decagonal"
DESCRIPTION = "Decagonal figurate numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        value = 4 * term + 4
        root = isqrt(value)

        if root * root != value:
            return False

        if (2 + root) % 4 != 0:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (4 * n - 3)

def formula(_):
    return "a(n) = n(4n - 3)"

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a decagonal number.",
        "The sequence matches the decagonal number formula exactly."
    ]