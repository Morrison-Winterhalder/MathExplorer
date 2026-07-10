from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Octagonal"
DESCRIPTION = "Octagonal figurate numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        value = 3 * term + 1
        if value < 0:
            return False
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
    return format_formula("n(3n-2)")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is an octagonal number.",
        "The sequence matches the octagonal number formula exactly."
    ]