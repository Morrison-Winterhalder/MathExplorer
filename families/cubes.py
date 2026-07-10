from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Cubes"
DESCRIPTION = "Perfect cube numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40
PARENT = "Polynomial"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = integer_nth_root(term,3)

        if root**3 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**3

def formula(_):
    expression = "n^3"
    return format_formula(expression)

def complexity(_):
    return 3

def explain(_):
    return [
        "Every term is a perfect cube.",
        "The sequence matches the formula n³ exactly."
    ]