from math import isqrt

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
    return "a(n) = n² + (n-1)²"

def complexity(_):
    return 2