from math import factorial

NAME = "Factorial"
DESCRIPTION = "Terms equal successive factorials."
REPRESENTATION = "Explicit"
CATEGORY = "Combinatorial"
SPECIFICITY = 50
PARENT = None

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for i, value in enumerate(sequence, start=1):
        if value != factorial(i):
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return factorial(n)


def formula(_):
    return "a(n) = n!"


def complexity(_):
    return 2

def explain(_):
    return [
        "Each term is the factorial of a consecutive integer.",
        "The sequence grows by repeated multiplication."
    ]