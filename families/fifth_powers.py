from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Fifth Powers"
DESCRIPTION = "Fifth powers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40
PARENT = "Polynomial"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = integer_nth_root(term,5)

        if root**5 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**5

def formula(_):
    expression = "n^5"
    return format_formula(expression)

def complexity(_):
    return 5

def explain(_):
    return [
        "Every term is a perfect fifth power.",
        "The sequence matches the formula n⁵ exactly."
    ]