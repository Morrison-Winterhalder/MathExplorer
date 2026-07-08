from math import factorial

NAME = "Factorial"

def is_factorial(sequence):
    if len(sequence) == 0:
        return None

    for i, value in enumerate(sequence, start=1):
        if value != factorial(i):
            return False

    return True

def fit_factorial(sequence):
    if not is_factorial(sequence):
        return None

    return {}

def evaluate_factorial(_, n):
    return factorial(n)

def complexity(_):
    return 2


fit = fit_factorial
evaluate = evaluate_factorial
recognize = is_factorial