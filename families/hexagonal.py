from analyzers.core.formatter import format_formula

NAME = "Hexagonal"
DESCRIPTION = "Hexagonal numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"


def recognize(sequence):
    if len(sequence) == 0:
        return None

    for n, value in enumerate(sequence, start=1):
        if value != evaluate({}, n):
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(_, n):
    return n * (2 * n - 1)


def formula(_):
    expression = "n(2n-1)"
    return format_formula(expression)


def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a hexagonal number.",
        "The sequence matches the hexagonal number formula exactly."
    ]