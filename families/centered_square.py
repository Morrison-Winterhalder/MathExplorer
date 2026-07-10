from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Centered Square"
DESCRIPTION = "Centered square numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 45
PARENT = "Centered Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        if term < 0:
            return False

        found = False

        root = isqrt(term)

        for n in (root, root + 1):
            if n * n + (n - 1) * (n - 1) == term:
                found = True
                break

        if not found:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n*n + (n-1)*(n-1)

def formula(_):
    return format_formula("n^2+(n-1)^2")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered square number.",
        "The sequence matches the centered square number formula exactly."
    ]