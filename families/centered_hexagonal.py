from math import isqrt

NAME = "Centered Hexagonal"
DESCRIPTION = "Centered hexagonal numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 45
PARENT = "Centered Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        d = 12 * (term - 1) + 1
        root = isqrt(d)

        if root * root != d:
            return False

        if (1 + root) % 6 != 0:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return 3*n*(n-1)+1

def formula(_):
    return "a(n) = 3n(n-1)+1"

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered hexagonal number.",
        "The sequence matches the centered hexagonal number formula exactly."
    ]