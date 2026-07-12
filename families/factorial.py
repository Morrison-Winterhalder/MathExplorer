from math import factorial
from analyzers.core.formatter import format_formula

NAME = "Factorials"
DESCRIPTION = "Products of consecutive positive integers."
REPRESENTATION = "Explicit"
CATEGORY = "Special"
SPECIFICITY = 50
PARENT = None

# Mathematical Metadata
OEIS = "A000142"
ALIASES = [
    "Factorial Numbers",
    "Factorial Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Factorial"

TAGS = (
    "Factorial",
    "Combinatorics",
)

DOMAIN = "Integers"
GROWTH = "Factorial"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

MIN_TERMS = 4
RECOGNITION_METHOD = "Factorial Formula"
RELIABILITY = "Exact"

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
    expression = "n!"
    return format_formula(expression)


def complexity(_):
    return 2

def explain(_):
    return [
        "Each term is the factorial of a consecutive integer.",
        "The sequence grows by repeated multiplication."
    ]