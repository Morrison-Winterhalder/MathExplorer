from math import sqrt

NAME = "Centered Triangular"
DESCRIPTION = "Centered triangular numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        d = 9 + 24 * (term - 1)
        root = sqrt(d)

        if not root.is_integer():
            return False

        n = (3 + root) / 6

        if not n.is_integer():
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return (3 * n * (n - 1)) // 2 + 1

def formula(_):
    return "a(n) = 3n(n-1)/2 + 1"

def complexity(_):
    return 2