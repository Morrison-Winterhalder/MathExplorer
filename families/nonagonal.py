from math import sqrt

NAME = "Nonagonal"
DESCRIPTION = "Nonagonal figurate numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        discriminant = 49 + 56 * term
        root = sqrt(discriminant)

        if not root.is_integer():
            return False

        n = (7 + root) / 14

        if not n.is_integer():
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (7 * n - 5) // 2

def formula(_):
    return "a(n) = n(7n - 5)/2"

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a nonagonal number.",
        "The sequence matches the nonagonal number formula exactly."
    ]