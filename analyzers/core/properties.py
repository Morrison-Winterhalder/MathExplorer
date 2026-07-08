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