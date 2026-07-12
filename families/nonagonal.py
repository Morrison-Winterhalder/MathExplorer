from math import sqrt
from analyzers.core.formatter import format_formula

NAME = "Nonagonal Numbers"
DESCRIPTION = "Numbers that can be arranged into regular nonagonal patterns."
REPRESENTATION = "Explicit"
CATEGORY = "Figurate"
SPECIFICITY = 40
PARENT = "Polygonal"

# Mathematical Metadata
OEIS = "A001106"
ALIASES = [
    "Nonagon Numbers",
    "Enneagonal Numbers",
    "Nonagonal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

TAGS = (
    "Figurate",
    "Polygonal",
    "Nonagonal",
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
        discriminant = 49 + 56 * term
        if discriminant < 0:
            return False
        root = sqrt(discriminant)

        if not root.is_integer():
            return False

        n = (7 + root) / 14

        if not n.is_integer():
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (7 * n - 5) // 2

def formula(_):
    return format_formula("n(7n-5)/2")

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is a nonagonal number.",
        "The sequence matches the nonagonal number formula exactly."
    ]