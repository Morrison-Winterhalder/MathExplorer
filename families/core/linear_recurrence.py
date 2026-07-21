NAME = "Linear Recurrence"
DESCRIPTION = "Sequences generated from linear recurrence relations."
REPRESENTATION = "Category"
CATEGORY = "Recursive"
SPECIFICITY = 30
PARENT = "Recursive"

FAMILY_TYPE = "Category"

CHILDREN = [
    "Fibonacci Numbers",
    "Lucas Numbers",
    "Pell Numbers",
    "Jacobsthal Numbers",
    "Tribonacci Numbers",
    "Tetranacci Numbers",
    "Padovan Numbers",
    "Perrin Numbers",
]

TAGS = (
    "Linear",
    "Recurrence",
)

TRAITS = {
    "construction": "recurrence",
    "relation": "linear",
}

RELATED = [
    "Recursive",
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
    return "Linear Recurrence Family"


def complexity(parameters):
    return 2


def explain(parameters):
    return [
        "This is a parent category for recursive sequence families.",
        "Child families include Fibonacci, Lucas, Pell, and Jacobsthal sequences."
    ]