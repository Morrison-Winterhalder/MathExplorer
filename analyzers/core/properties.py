from analyzers.core.transformations import first_differences

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