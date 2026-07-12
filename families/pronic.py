from math import isqrt
from analyzers.core.formatter import format_recurrence

NAME = "Pronic Numbers"
DESCRIPTION = "Numbers formed by multiplying two consecutive integers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 50
PARENT = "Polynomial"

# Mathematical Metadata
OEIS = "A002378"
ALIASES = [
    "Oblong Numbers",
    "Heteromecic Numbers",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Polynomial"

TAGS = (
    "Polynomial",
    "Quadratic",
    "Product",
    "Pronic",
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
        value = 4 * term + 1
        if value < 0:
            return False
        root = isqrt(value)

        if root * root != value:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n * (n + 1)

def formula(_):
    return "a(n) = n(n + 1)"

def complexity(_):
    return 2

def explain(_):
    return [
        "Every term is the product of two consecutive integers.",
        "The sequence matches the pronic number formula n(n + 1)."
    ]