NAME = "Constant"

def is_constant(sequence):
    if len(sequence) == 0:
        return None

    for value in sequence[1:]:
        if value != sequence[0]:
            return False

    return True


def fit_constant(sequence):
    if is_constant(sequence) is not True:
        return None

    return {
        "Value": sequence[0]
    }


def evaluate_constant(parameters, n):
    return parameters["Value"]

def complexity(_):
    return 0

fit = fit_constant
evaluate = evaluate_constant
recognize = is_constant