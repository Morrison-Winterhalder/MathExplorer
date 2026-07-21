NAME = "Recursive"
DESCRIPTION = "Sequence families defined through recurrence relationships."
REPRESENTATION = "Category"
CATEGORY = "Structural"
SPECIFICITY = 10
PARENT = "Sequence Families"

FAMILY_TYPE = "Root"

CHILDREN = [
    "Linear Recurrence",
]

TAGS = (
    "Recursive",
    "Recurrence",
)

TRAITS = {
    "construction": "recurrence",
    "representation": "recursive",
    "domain": "varied",
}

RELATED = [
    "Explicit",
]

DOMAIN = "Integers"
GROWTH = "Variable"

MONOTONIC = None
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = True
PARAMETER_NAMES = (
    "Coefficients",
    "Initial Values",
)

CLOSED_FORM = False
EVALUATION_METHOD = "Recurrence"

MIN_TERMS = 3
RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"


def recognize(sequence):
    return False


def fit(sequence):
    return None


def evaluate(parameters, n):
    return None


def formula(parameters):
    return "Recursive Family"


def complexity(parameters):
    return 0


def explain(parameters):
    return [
        "This is a parent category for recursively defined sequence families.",
        "Child families include linear recurrence sequences such as Fibonacci, Lucas, Pell, and Jacobsthal."
    ]