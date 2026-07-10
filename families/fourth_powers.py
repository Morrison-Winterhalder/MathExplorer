from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Fourth Powers"
DESCRIPTION = "Fourth powers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40
PARENT = "Polynomial"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = integer_nth_root(term, 4)

        if root is None:
            return False

        if root ** 4 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**4

def formula(_):
    expression = "n^4"
    return format_formula(expression)

def complexity(_):
    return 4

def explain(_):
    return [
        "Every term is a perfect fourth power.",
        "The sequence matches the formula n⁴ exactly."
    ]