from math import sqrt
from analyzers.core.formatter import format_formula

NAME = "Centered Triangular Numbers"
DESCRIPTION = "Numbers that form centered triangular patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 45
PARENT = "Centered Polygonal"

# Mathematical Metadata
OEIS = "A005448"
ALIASES = [
    "Centered Triangle Numbers",
    "Centered Triangular Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

TAGS = (
    "Centered",
    "Figurate",
    "Polygonal",
    "Triangular",
)

DOMAIN = "Integers"
GROWTH = "Quadratic"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

MIN_TERMS = 3
RECOGNITION_METHOD = "Direct Formula"
RELIABILITY = "Exact"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        d = 9 + 24 * (term - 1)
        if d < 0:
            return False
        root = sqrt(d)

        if not root.is_integer():
            return False

        n = (3 + root) / 6

        if not n.is_integer():
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return (3 * n * (n - 1)) // 2 + 1

def formula(_):
    return format_formula("3n(n-1)/2+1")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered triangular number.",
        "The sequence matches the centered triangular number formula exactly."
    ]