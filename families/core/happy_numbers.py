from analyzers.core.formatter import format_formula


NAME = "Happy Numbers"
DESCRIPTION = "Numbers whose digit-square process eventually reaches 1."
REPRESENTATION = "Recursive"
CATEGORY = "Special"
SPECIFICITY = 55
PARENT = "Recursive"
NATURAL_FAMILY = True


OEIS = "A007770"

ALIASES = [
    "Happy Integer Sequence",
]


CLOSED_FORM = False
EVALUATION_METHOD = "Digit Process"

FAMILY_TYPE = "Sequence"


TAGS = (
    "Recursive",
    "Digit",
)


TRAITS = {
    "growth": "irregular",
    "construction": "recursive",
    "domain": "integers",
}


RELATED = [
    "Integer Sequences",
]


DOMAIN = "Integers"
GROWTH = "Irregular"


MONOTONIC = None
BOUNDED = False
OSCILLATING = False
PERIODIC = False


FORMULA_TYPE = REPRESENTATION

REQUIRES_PARAMETERS = False

PARAMETER_NAMES = ()

MIN_TERMS = 5

RECOGNITION_METHOD = "Digit Transformation"
RELIABILITY = "Exact"



def is_happy(n):

    seen = set()

    while n != 1:

        if n in seen:
            return False

        seen.add(n)

        n = sum(
            int(digit) ** 2
            for digit in str(n)
        )

    return True



def recognize(sequence):

    expected = [
        n
        for n in range(1, 1000)
        if is_happy(n)
    ][:len(sequence)]

    return sequence == expected



def fit(sequence):

    if recognize(sequence):
        return {}

    return None



def evaluate(parameters, n):

    return [
        x
        for x in range(1, 1000)
        if is_happy(x)
    ][n-1]



def formula(parameters):

    return format_formula(
        "Repeated digit-square transformation"
    )



def complexity(_):

    return 2



def explain(parameters):

    return [
        "The sequence consists of numbers whose digit-square process reaches 1.",
        "Happy numbers are defined through repeated recursive digit transformations."
    ]