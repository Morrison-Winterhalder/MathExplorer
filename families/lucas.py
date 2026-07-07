def is_lucas(sequence):
    if len(sequence) < 3:
        return False

    if sequence[0] != 2 or sequence[1] != 1:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False

    return True