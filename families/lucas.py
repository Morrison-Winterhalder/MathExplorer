from families.recurrence import evaluate_linear_recurrence

NAME = "Lucas"

def is_lucas(sequence):
    if len(sequence) < 3:
        return None

    if sequence[0] != 2 or sequence[1] != 1:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False

    return True

def fit_lucas(sequence):
    if is_lucas(sequence) is not True:
        return None
    
    return {
        "Seeds": [2,1], 
        "RecurrenceCoefficients": [1,1]
    }

evaluate = evaluate_linear_recurrence

def complexity(_):
    return 2

fit = fit_lucas
recognize = is_lucas