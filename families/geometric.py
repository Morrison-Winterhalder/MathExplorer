from families import constant
from analyzers.core.transformations import first_ratios
from analyzers.core.utilities import pretty
from analyzers.core.formatter import format_formula

NAME = "Geometric"
DESCRIPTION = "Constant ratios."
REPRESENTATION = "Explicit"
CATEGORY = "Geometric"
SPECIFICITY = 20
PARENT = "Explicit"
NATURAL_FAMILY = True

# Mathematical Metadata
OEIS = None
ALIASES = [
    "Geometric Progression",
]

CLOSED_FORM = True
EVALUATION_METHOD = "Explicit"

FAMILY_TYPE = "Sequence"

TAGS = (
    "Exponential",
    "Geometric",
)

TRAITS = {
    "growth": "exponential",
    "construction": "explicit",
    "domain": "numbers",
}

RELATED = [
    "Arithmetic",
]

DOMAIN = "Real Numbers"
GROWTH = "Exponential"

MONOTONIC = None
BOUNDED = None
OSCILLATING = None
PERIODIC = False

FORMULA_TYPE = REPRESENTATION
REQUIRES_PARAMETERS = True
PARAMETER_NAMES = (
    "First Term",
    "Ratio",
)

MIN_TERMS = 3
RECOGNITION_METHOD = "Constant Ratio"
RELIABILITY = "Exact"


def recognize(sequence):
    if len(sequence) < 2:
        return None

    ratios = first_ratios(sequence)

    if None in ratios:
        return None

    return constant.recognize(ratios)


def fit(sequence):
    if len(sequence) < 2:
        return None

    ratios = first_ratios(sequence)

    if None in ratios:
        return None

    if constant.recognize(ratios) is not True:
        return None

    return {
        "First Term": sequence[0],
        "Ratio": ratios[0]
    }


def evaluate(parameters, n):
    return (
        parameters["First Term"]
        * parameters["Ratio"] ** (n - 1)
    )


def formula(parameters):

    a = pretty(parameters["First Term"])
    r = pretty(parameters["Ratio"])

    expression = f"{a}·{r}^(n-1)"

    return format_formula(expression)


def complexity(_):
    return 1

def explain(parameters):
    return [
        f"The sequence has a constant ratio of {parameters['Ratio']}.",
        "Each term is obtained by multiplying the previous term by the common ratio."
    ]