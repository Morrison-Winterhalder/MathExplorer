"""
Recognizers for triangular numbers.

Examples:
    - Identify triangular numbers
"""

from math import isqrt

NAME = "Triangular"

def is_triangular(sequence):
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

def fit_triangular(sequence):
    if is_triangular(sequence) is not True:
        return None

    return {}

def evaluate_triangular(_,n):
    return n * (n + 1) // 2

def complexity(_):
    return 2

fit = fit_triangular
evaluate = evaluate_triangular
recognize = is_triangular