from families.recurrence import evaluate_linear_recurrence

NAME = "Pell"
DESCRIPTION = "Each term equals twice the previous term plus the one before."
REPRESENTATION = "Recurrence"
CATEGORY = "Recurrence"
SPECIFICITY = 50
PARENT = "Linear Recurrence"


def recognize(sequence):
    if len(sequence) < 3:
        return None

    if sequence[:2] != [0, 1]:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != 2 * sequence[i - 1] + sequence[i - 2]:
            return False

    return True


def fit(sequence):
    if recognize(sequence) is not True:
        return None

    return {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [2, 1]
    }


def evaluate(parameters, n):
    return evaluate_linear_recurrence(parameters, n)


def formula(_):
    return "a(n) = 2a(n-1) + a(n-2)"


def complexity(_):
    return 2

def explain(_):
    return [
        "The sequence follows the Pell recurrence relation.",
        "Each term is generated from the previous two Pell numbers."
    ]