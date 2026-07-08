from families.constant import is_constant
from analyzers.core.transformations import first_ratios

NAME = "Geometric"

def is_geometric(sequence):
    if len(sequence) < 2:
        return None
    ratios = first_ratios(sequence)
    if None in ratios:
        return None
    return is_constant(ratios)
    
def fit_geometric(sequence):
    if is_geometric(sequence) is not True:
        return None

    ratio = first_ratios(sequence)[0]

    return {
        "First Term": sequence[0],
        "Ratio": ratio
    }

def evaluate_geometric(parameters,n):
    first_term = parameters["First Term"]
    ratio = parameters["Ratio"]
    return first_term * (ratio ** (n - 1))

def complexity(_):
    return 1

fit = fit_geometric
evaluate = evaluate_geometric
recognize = is_geometric