from analyzers.core.utilities import integer_nth_root
from analyzers.core.formatter import format_formula

NAME = "Squares"
DESCRIPTION = "Perfect square numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40
PARENT = "Polynomial"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        if term < 0:
            return False

        root = integer_nth_root(term,2)

        if root * root != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n*n

def formula(_):
    expression = "n^2"
    return format_formula(expression)

def complexity(_):
    return 2

def explain(_):

    return [
        "Every term is a perfect square.",
        "The sequence matches the formula n² exactly."
    ]