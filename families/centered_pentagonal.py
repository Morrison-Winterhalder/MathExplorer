from math import sqrt
from analyzers.core.formatter import format_formula

NAME = "Centered Pentagonal Numbers"
DESCRIPTION = "Numbers that form centered pentagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 45
PARENT = "Centered Polygonal"

# Mathematical Metadata
OEIS = "A005891"
ALIASES = [
    "Centered Pentagon Numbers",
    "Centered Pentagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

TAGS = (
    "Centered",
    "Figurate",
    "Polygonal",
    "Pentagonal",
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
        d = 25 + 40 * (term - 1)
        if d < 0:
            return False
        root = sqrt(d)

        if not root.is_integer():
            return False

        n = (5 + root) / 10

        if not n.is_integer():
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return (5 * n * (n - 1)) // 2 + 1

def formula(_):
    return format_formula("5n(n-1)/2+1")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a centered pentagonal number.",
        "The sequence matches the centered pentagonal number formula exactly."
    ]