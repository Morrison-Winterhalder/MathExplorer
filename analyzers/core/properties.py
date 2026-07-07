from analyzers.core.transformations import first_differences, first_ratios

def is_constant(sequence):
    if len(sequence) == 0:
        return None
    for value in sequence[1:]:
        if value != sequence[0]:
            return False
    return True

def is_arithmetic(sequence):
    if len(sequence) < 2:
        return None
    return is_constant(first_differences(sequence))

def is_geometric(sequence):
    if len(sequence) < 2:
        return None
    ratios = first_ratios(sequence)
    if None not in ratios:
        return is_constant(ratios)
    else:
        return None
    
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

def polynomial_degree(sequence):
    if len(sequence) < 2:
        return None
    degree = 0
    while True:
        print("Degree:",degree,"Sequence:",sequence)
        status = is_constant(sequence)
        if status is False:
            sequence = first_differences(sequence)
            degree += 1
        elif status is None:
            return None
        else:
            break
    return degree