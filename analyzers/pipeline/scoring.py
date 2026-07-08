def normalize_error(error,scale=1.0):
    return 1 / (1+ error / scale)

def score_constant(sequence, report):
    if report["Properties"]["Is Constant?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Constant",
        "Score": score
    }

def score_arithmetic(sequence, report):
    pass

def score_geometric(sequence, report):
    if report["Properties"]["Is Geometric?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Geometric",
        "Score": score
    }

def score_polynomial(sequence, report):
    properties = report["Properties"]
    degree = properties["Polynomial Degree"]
    if degree is None:
        score = 0.0
    else:
        score = 1.0

    return {
        "Type": "Polynomial",
        "Score": score
    }

def score_triangular(sequence, report):
    if report["Properties"]["Is Triangular?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Triangular",
        "Score": score
    }

def score_pentagonal(sequence, report):
    if report["Properties"]["Is Pentagonal?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Pentagonal",
        "Score": score
    }

def score_pell(sequence, report):
    if report["Properties"]["Is Pell?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Pell",
        "Score": score
    }

def score_lucas(sequence, report):
    if report["Properties"]["Is Lucas?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Lucas",
        "Score": score
    }

def score_jacobsthal(sequence, report):
    if report["Properties"]["Is Jacobsthal?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Jacobsthal",
        "Score": score
    }

def score_fibonacci(sequence, report):
    if report["Properties"]["Is Fibonacci?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Fibonacci",
        "Score": score
    }

def score_factorial(sequence, report):
    if report["Properties"]["Is Factorial?"]:
        score = 1.0
    else:
        score = 0.0

    return {
        "Type": "Factorial",
        "Score": score
    }

SCORE_HANDLERS = [
    score_constant,
    score_arithmetic,
    score_geometric,
    score_polynomial,
    score_triangular,
    score_pentagonal,
    score_pell,
    score_lucas,
    score_jacobsthal,
    score_fibonacci,
    score_factorial
]



def score_sequence(sequence, report):
    scores = {}

    for scorer in SCORE_HANDLERS:
        result = scorer(sequence, report)
        scores[result["Type"]] = result["Score"]

    return scores