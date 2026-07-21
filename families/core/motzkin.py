from analyzers.core.formatter import format_formula


NAME = "Motzkin Numbers"
DESCRIPTION = "Counts non-crossing paths and related combinatorial structures."
REPRESENTATION = "Recursive"
CATEGORY = "Combinatorial"
SPECIFICITY = 60
PARENT = "Recursive"
NATURAL_FAMILY = True


# Mathematical Metadata
OEIS = "A001006"

ALIASES = [
    "Motzkin Sequence",
]


CLOSED_FORM = True
EVALUATION_METHOD = "Recursive Relation"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Combinatorial",
    "Recursive",
)


TRAITS = {
    "growth": "combinatorial",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Catalan Numbers",
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



def motzkin_number(n):

    if n == 1:
        return 1

    if n == 2:
        return 1

    previous_two = 1
    previous_one = 1

    for k in range(3, n + 1):

        current = (
            ((2 * k - 1) * previous_one)
            +
            ((3 * k - 6) * previous_two)
        ) // (k + 1)

        previous_two = previous_one
        previous_one = current

    return previous_one



def recognize(sequence):

    if len(sequence) < MIN_TERMS:
        return None

    for index, value in enumerate(sequence, start=1):

        if value != motzkin_number(index):
            return None

    return True



def fit(sequence):

    if recognize(sequence) is not True:
        return None

    return {}



def evaluate(parameters, n):

    return motzkin_number(n)



def formula(parameters):

    return format_formula(
        "M(n)=((2n-1)M(n-1)+(3n-6)M(n-2))/(n+1)"
    )



def complexity(_):

    return 2



def explain(parameters):

    return [
        "The sequence matches the Motzkin recurrence.",
        "Motzkin numbers count several combinatorial structures including non-crossing paths and polygon triangulations."
    ]