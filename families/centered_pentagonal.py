from math import sqrt
from analyzers.core.formatter import format_formula

NAME = "Centered Pentagonal"
DESCRIPTION = "Centered pentagonal numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 45
PARENT = "Centered Polygonal"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        d = 25 + 40 * (term - 1)
        if d < 0:
            return False
        root = sqrt(d)

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
    return (5 * n * (n - 1)) // 2 + 1

def formula(_):
    return format_formula("5n(n-1)/2+1")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered pentagonal number.",
        "The sequence matches the centered pentagonal number formula exactly."
    ]