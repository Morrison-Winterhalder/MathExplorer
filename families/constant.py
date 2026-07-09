NAME = "Constant"
DESCRIPTION = "All terms are equal."
REPRESENTATION = "Explicit"
CATEGORY = "Constant"
SPECIFICITY = 20
PARENT = "Arithmetic"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for value in sequence[1:]:
        if value != sequence[0]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Value": sequence[0]
    }


def evaluate(parameters, n):
    return parameters["Value"]

def formula(parameters):
    return f"a(n) = {parameters['Value']}"

def complexity(_):
    return 0
