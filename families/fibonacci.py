from families.recurrence import evaluate_linear_recurrence

NAME = "Fibonacci"

def is_fibonacci(sequence):
    if len(sequence) < 3:
        return None

    if sequence[0] != 0 or sequence[1] != 1:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False

    return True

def fit_fibonacci(sequence):
    if not is_fibonacci(sequence):
        return None

    return {
        "Seeds": [0, 1],
        "RecurrenceCoefficients": [1, 1]
    }

evaluate = evaluate_linear_recurrence

def complexity(_):
    return 2

fit = fit_fibonacci
recognize = is_fibonacci