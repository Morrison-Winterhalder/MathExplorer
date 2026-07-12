NAME = "Explicit"
DESCRIPTION = "Families defined by direct formulas rather than previous terms."
REPRESENTATION = "Explicit"

CATEGORY = "Explicit"
SPECIFICITY = 10
PARENT = None

DOMAIN = "Integers"
GROWTH = "Variable"

MONOTONIC = None
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

CLOSED_FORM = True
EVALUATION_METHOD = "Direct Formula"

MIN_TERMS = 1
RECOGNITION_METHOD = "Formula Based"
RELIABILITY = "Exact"


def recognize(sequence):
    return False


def fit(sequence):
    return None


def evaluate(parameters, n):
    return None


def formula(parameters):
    return "Explicit Family"


def complexity(parameters):
    return 0


def explain(parameters):
    return [
        "This is a parent category for explicitly defined sequence families.",
        "Child families include arithmetic, geometric, polynomial, and figurate sequences."
    ]