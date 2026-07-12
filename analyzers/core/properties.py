def is_increasing(sequence):
    if len(sequence) < 2:
        return None
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return False
    return True

def is_decreasing(sequence):
    if len(sequence) < 2:
        return None
    for i in range(len(sequence)-1):
        if sequence[i] <= sequence[i+1]:
            return False
    return True

def is_unique(sequence):
    if len(sequence) < 2:
        return None
    return (len(sequence) == len(set(sequence)))

def determine_monotonic(sequence):

    increasing = all(
        sequence[i] < sequence[i+1]
        for i in range(len(sequence)-1)
    )

    decreasing = all(
        sequence[i] > sequence[i+1]
        for i in range(len(sequence)-1)
    )

    constant = all(
        sequence[i] == sequence[i+1]
        for i in range(len(sequence)-1)
    )

    if constant:
        return "Constant"

    if increasing:
        return "Increasing"

    if decreasing:
        return "Decreasing"

    return "Not Monotonic"