from math import sqrt

NAME = "Heptagonal"
DESCRIPTION = "Heptagonal figurate numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        discriminant = 40 + 40 * term
        root = sqrt(discriminant)

        if not root.is_integer():
            return False

        n = (5 + root) / 10

        if not n.is_integer():
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (5 * n - 3) // 2

def formula(_):
    return "a(n) = n(5n - 3)/2"

def complexity(_):
    return 2