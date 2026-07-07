def is_fibonacci(sequence):
    if len(sequence) < 3:
        return False

    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False

    return True