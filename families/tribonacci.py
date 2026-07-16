from families.recurrence import evaluate_linear_recurrence
from analyzers.core.formatter import format_formula

NAME = "Tribonacci Numbers"
DESCRIPTION = "A sequence where each term is the sum of the previous three terms."
REPRESENTATION = "Recursive"

CATEGORY = "Recursive"
SPECIFICITY = 55
PARENT = "Linear Recurrence"
NATURAL_FAMILY = True

OEIS = "A000073"
ALIASES = [
    "Tribonacci Sequence",
]

FAMILY_TYPE = "Sequence"

TAGS = (
    "Tribonacci",
    "Recurrence",
)

TRAITS = {
    "construction": "linear_recurrence",
    "order": 3,
    "growth": "exponential",
}

RELATED = [
    "Tetranacci Numbers",
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

MIN_TERMS = 6
RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"


def recognize(sequence):

    if len(sequence) < 4:
        return None

    if sequence[:3] != [0, 0, 1]:
        return False

    for i in range(3, len(sequence)):
        if sequence[i] != (
            sequence[i-1]
            + sequence[i-2]
            + sequence[i-3]
        ):
            return False

    return True


def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [0, 0, 1],
        "RecurrenceCoefficients": [1, 1, 1],
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return "a(n) = a(n - 1) + a(n - 2) + a(n - 3)"


def complexity(_):
    return 3


def explain(_):
    return [
        "The sequence follows the Tribonacci recurrence relation.",
        "Each term is generated from the previous three terms."
    ]