from math import sqrt

NAME = "Pentagonal"

def is_pentagonal(sequence):
    if len(sequence) == 0:
        return None

    for value in sequence:
        discriminant = 1 + 24 * value
        root = sqrt(discriminant)

        if not root.is_integer():
            return False

        n = (1 + root) / 6

        if not n.is_integer():
            return False

    return True

def fit_pentagonal(sequence):
    if is_pentagonal(sequence) is not True:
        return None

    return {}

def evaluate_pentagonal(_, n):
    return n * (3 * n - 1) // 2

def complexity(_):
    return 2

fit = fit_pentagonal
evaluate = evaluate_pentagonal
recognize = is_pentagonal