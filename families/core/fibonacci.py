from families.core.recurrence import evaluate_linear_recurrence
from analyzers.core.formatter import format_recurrence

NAME = "Fibonacci"
DESCRIPTION = "Each term is the sum of the two preceding terms."
REPRESENTATION = "Recursive"
CATEGORY = "Recursive"
SPECIFICITY = 50
PARENT = "Linear Recurrence"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = "A000045"
ALIASES = [
    "Fibonacci Numbers",
    "Fibonacci Sequence",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Recurrence"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Fibonacci",
    "Recurrence",
)

TRAITS = {
    "construction": "linear_recurrence",
    "order": 2,
    "growth": "exponential",
}

RELATED = [
    "Lucas Numbers",
    "Pell Numbers",
]

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
        return False

    if sequence[:2] not in ([0, 1], [1, 1]):
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": sequence[:2],
        "RecurrenceCoefficients": [1, 1]
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return format_recurrence("a(n-1)+a(n-2)")


def complexity(_):
    return 2

def explain(_):

    return [
        "Each term is the sum of the two preceding terms."
    ]