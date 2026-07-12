from math import isqrt
from analyzers.core.formatter import format_formula

NAME = "Centered Square Numbers"
DESCRIPTION = "Numbers that form centered square patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 45
PARENT = "Centered Polygonal"

# Mathematical Metadata
OEIS = "A001844"
ALIASES = [
    "Centered Squares",
    "Centered Square Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

TAGS = (
    "Centered",
    "Figurate",
    "Polygonal",
    "Quadratic",
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

    if len(sequence) < MIN_TERMS:
        return None

    for n, term in enumerate(sequence, start=1):

        expected = n*n + (n-1)*(n-1)

        if term != expected:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n*n + (n-1)*(n-1)

def formula(_):
    return format_formula("n^2+(n-1)^2")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered square number.",
        "The sequence matches the centered square number formula exactly."
    ]