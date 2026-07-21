from math import comb

NAME = "Catalan Numbers"
DESCRIPTION = "The Catalan sequence."
REPRESENTATION = "Recursive"
CATEGORY = "Combinatorial"
SPECIFICITY = 60
PARENT = "Combinatorial"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000108"
ALIASES = [
    "Catalan",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Closed Form"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Recursive",
    "Combinatorial",
    "Catalan",
)

TRAITS = {
    "growth": "super-polynomial",
    "construction": "recursive",
    "domain": "integers",
}

RELATED = [
    "Fibonacci",
]

DOMAIN = "Integers"
GROWTH = "Combinatorial"

MONOTONIC = True 
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

MIN_TERMS = 4
RECOGNITION_METHOD = "Direct Formula"
RELIABILITY = "Exact"


def recognize(sequence):

    for i, value in enumerate(sequence):
        if value != evaluate({}, i + 1):
            return None

    return True


def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {}


def evaluate(parameters, n):

    k = n - 1

    return comb(2 * k, k) // (k + 1)


def formula(parameters):

    return "C(n) = (1/(n+1))·binomial(2n,n)"


def complexity(_):
    return 2


def explain(parameters):
    return [
        "Every term matches the Catalan number formula.",
        "Catalan numbers count many combinatorial structures such as binary trees, Dyck paths, and balanced parenthesizations."
    ]