from families.recurrence import evaluate_linear_recurrence
from analyzers.core.formatter import format_recurrence

NAME = "Jacobsthal Numbers"
DESCRIPTION = "A sequence defined by a linear recurrence relation."
REPRESENTATION = "Recursive"
CATEGORY = "Recursive"
SPECIFICITY = 50
PARENT = "Linear Recurrence"

# Mathematical Metadata
OEIS = "A001045"
ALIASES = [
    "Jacobsthal Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Recurrence"

TAGS = (
    "Recursive",
    "Linear Recurrence",
    "Jacobsthal",
)

DOMAIN = "Integers"
GROWTH = "Exponential"

MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = False
PARAMETER_NAMES = ()

MIN_TERMS = 5
RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"


def recognize(sequence):
    if len(sequence) < 3:
        return None

    if sequence[:2] != [0, 1]:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + 2 * sequence[i - 2]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [1, 2]
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return format_recurrence("a(n-1)+2a(n-2)")


def complexity(_):
    return 2

def explain(_):
    return [
        "The sequence follows the Jacobsthal recurrence relation.",
        "Each term is determined by the previous two terms."
    ]