from analyzers.core.formatter import format_formula
from analyzers.core.utilities import pretty


NAME = "Derangement Numbers"
DESCRIPTION = "Permutations with no fixed points."
REPRESENTATION = "Recursive"
CATEGORY = "Combinatorial"
SPECIFICITY = 60
PARENT = "Combinatorial"
NATURAL_FAMILY = True


# Mathematical Metadata
OEIS = "A000166"

ALIASES = [
    "Subfactorials",
    "Rencontres Numbers",
]


CLOSED_FORM = True
EVALUATION_METHOD = "Recursive Relation"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Combinatorial",
    "Recursive",
    "Permutation",
)


TRAITS = {
    "growth": "combinatorial",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Factorial Numbers",
    "Bell Numbers",
]


DOMAIN = "Integers"
GROWTH = "Combinatorial"


MONOTONIC = True
BOUNDED = False
OSCILLATING = False
PERIODIC = False


FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = False

PARAMETER_NAMES = (
)


MIN_TERMS = 5

RECOGNITION_METHOD = "Recursive Relation"
RELIABILITY = "Exact"



def derangement_number(n):

    if n == 1:
        return 0

    if n == 2:
        return 1

    d1 = 0   # D(1)
    d2 = 1   # D(2)

    for k in range(3, n + 1):

        current = (k - 1) * (d1 + d2)

        d1 = d2
        d2 = current

    return d2


def recognize(sequence):

    if len(sequence) < MIN_TERMS:
        return None

    for index, value in enumerate(sequence, start=1):

        if value != derangement_number(index):
            return None

    return True



def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {}



def evaluate(parameters, n):

    return derangement_number(n)



def formula(parameters):

    return format_formula(
        "D(n)=(n-1)(D(n-1)+D(n-2))"
    )



def complexity(_):

    return 2



def explain(parameters):

    return [
        "The sequence matches the derangement recurrence.",
        "Derangement numbers count permutations where no element remains in its original position."
    ]