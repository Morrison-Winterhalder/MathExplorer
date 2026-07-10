from families import constant
from analyzers.core.transformations import first_ratios

NAME = "Geometric"
DESCRIPTION = "Constant ratios between consecutive terms."
REPRESENTATION = "Explicit"
CATEGORY = "Geometric"
SPECIFICITY = 20
PARENT = None


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
    a = parameters["First Term"]
    r = parameters["Ratio"]

    return f"a(n) = {a} · {r}^(n-1)"


def complexity(_):
    return 1

def explain(parameters):
    return [
        f"The sequence has a constant ratio of {parameters['Ratio']}.",
        "Each term is obtained by multiplying the previous term by the common ratio."
    ]