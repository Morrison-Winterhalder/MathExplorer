from math import factorial

def is_factorial(sequence):
    if not sequence:
        return False

    for i, value in enumerate(sequence, start=1):
        if value != factorial(i):
            return False

    return True