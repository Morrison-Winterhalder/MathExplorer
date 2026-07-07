"""
Recognizers for specific mathematical sequence families.

Examples:
    - Triangular numbers
    - Fibonacci
    - Factorials
    - Figurate numbers
"""

from math import isqrt

def is_triangular(sequence):
    if len(sequence) < 2:
        return False

    for term in sequence:
        if term < 0:
            return False

        value = 8 * term + 1
        root = isqrt(value)

        if root * root != value:
            return False

    return True