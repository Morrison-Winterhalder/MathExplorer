from math import sqrt

def pentagonal_number(n):
    return n * (3 * n - 1) // 2


def is_pentagonal(sequence):
    if not sequence:
        return False

    for value in sequence:
        discriminant = 1 + 24 * value
        root = sqrt(discriminant)

        if root != int(root):
            return False

        n = (1 + root) / 6

        if n != int(n):
            return False

    return True