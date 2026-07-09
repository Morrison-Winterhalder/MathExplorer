from math import isqrt

NAME = "Triangular"
DESCRIPTION = "Terms are triangular numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40


def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        if term < 0:
            return False

        value = 8 * term + 1
        root = isqrt(value)

        if root * root != value:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (n + 1) // 2


def formula(_):
    return "a(n) = n(n + 1)/2"


def complexity(_):
    return 2