def classify_constant(sequence, report):
    properties = report["Properties"]
    if not properties["Is Constant?"]:
        return None
    return {
        "Type": "Constant",
        "Degree": 0,
        "Common Difference": 0,
        "Common Ratio": 1,
        "Reason": "Sequence is constant."
    }

def classify_arithmetic(sequence, report):
    properties = report["Properties"]
    transformations = report["Transformations"]
    if not properties["Is Arithmetic?"]:
        return None
    return {
        "Type": "Arithmetic",
        "Common Difference": transformations["First Differences"][0],
        "Common Ratio": None,
        "Reason": "First differences are constant."
    }

def classify_geometric(sequence, report):
    properties = report["Properties"]
    transformations = report["Transformations"]
    if not properties["Is Geometric?"]:
        return None
    return {
        "Type": "Geometric",
        "Degree": None,
        "Common Difference": None,
        "Common Ratio": transformations["First Ratios"][0],
        "Reason": "First ratios are constant."
    }

def classify_triangular(sequence, report):
    properties = report["Properties"]
    transformations = report["Transformations"]

    if not properties["Is Triangular?"]:
        return None

    return {
        "Type": "Triangular",
        "Degree": 2,
        "Common Difference": None,
        "Common Ratio": None,
        "Reason": "All terms are triangular numbers."
    }

def classify_pentagonal(sequence, report):
    properties = report["Properties"]

    if not properties["Is Pentagonal?"]:
        return None

    return {
        "Type": "Pentagonal",
        "Degree": 2,
        "Reason": "All terms are pentagonal numbers."
    }

def classify_fibonacci(sequence, report):
    properties = report["Properties"]

    if not properties["Is Fibonacci?"]:
        return None

    return {
        "Type": "Fibonacci",
        "Degree": None,
        "Reason": "Each term is the sum of the previous two."
    }

def classify_lucas(sequence, report):
    properties = report["Properties"]

    if not properties["Is Lucas?"]:
        return None

    return {
        "Type": "Lucas",
        "Degree": None,
        "Reason": "Each term is the sum of the previous two, beginning with 2 and 1."
    }

def classify_pell(sequence, report):
    properties = report["Properties"]

    if not properties["Is Pell?"]:
        return None

    return {
        "Type": "Pell",
        "Degree": None,
        "Reason": "Each term satisfies P(n)=2P(n-1)+P(n-2)."
    }

def classify_jacobsthal(sequence, report):
    properties = report["Properties"]

    if not properties["Is Jacobsthal?"]:
        return None

    return {
        "Type": "Jacobsthal",
        "Degree": None,
        "Reason": "Each term satisfies J(n)=J(n-1)+2J(n-2)."
    }

def classify_factorial(sequence, report):
    properties = report["Properties"]

    if not properties["Is Factorial?"]:
        return None

    return {
        "Type": "Factorial",
        "Degree": None,
        "Reason": "Terms equal n!."
    }

def classify_polynomial(sequence, report):
    properties = report["Properties"]
    degree = properties["Polynomial Degree"]
    if degree is None:
        return None
    return {
        "Type": "Polynomial",
        "Degree": degree,
        "Common Difference": None,
        "Common Ratio": None,
        "Reason": "Nth differences become constant."
    }

CLASSIFICATION_HANDLERS = (
    classify_constant,
    classify_arithmetic,
    classify_geometric,
    classify_triangular,
    classify_pentagonal,
    classify_fibonacci,
    classify_lucas,
    classify_pell,
    classify_jacobsthal,
    classify_factorial,
    classify_polynomial
)

def classify_sequence(sequence, report):
    for classifier in CLASSIFICATION_HANDLERS:
        result = classifier(sequence, report)
        if result is not None:
            return result
    return {
        "Type": "Unknown",
        "Degree": None,
        "Common Difference": None,
        "Common Ratio": None,
        "Reason": "No implemented classifier matched."
    }