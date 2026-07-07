from math import factorial
from objects.classifiers import classify_sequence

def pretty_number(x): # FOR LATER
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x

def first_differences(sequence):
    first_difference_sequence = []
    for i in range(0,len(sequence)-1):
        first_difference_sequence.append(sequence[i+1]-sequence[i])
    return first_difference_sequence

def nth_differences(sequence,n):
    changing_sequence = sequence
    for _ in range(n):
        changing_sequence = first_differences(changing_sequence)
    return changing_sequence

def is_constant(sequence):
    if len(sequence) < 2:
        return None
    for i in range(1,len(sequence)):
        if sequence[i] != sequence[0]:
            return False
    return True

def polynomial_degree(sequence):
    degree = 0
    while True:
        status = is_constant(sequence)
        if status is False:
            sequence = first_differences(sequence)
            degree += 1
        elif status is None:
            return None
        else:
            break
    return degree

def first_ratios(sequence):
    if len(sequence) < 2:
        return []
    ratios = []
    for i in range(len(sequence)-1):
        if sequence[i] == 0:
            ratios.append(None)
        else:
            ratios.append((sequence[i+1])/(sequence[i]))
    return ratios

def is_arithmetic(sequence):
    return is_constant(first_differences(sequence))

def is_geometric(sequence):
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
    return (len(sequence) == len(set(sequence)))

def format_polynomial(coefficients):
    polyList = []
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        if coefficient == 0:
            continue
        elif power == 0:
            polyList.append(str(coefficient))
        elif power == 1:
            if coefficient == 1:
                polyList.append("n")
            elif coefficient == -1:
                polyList.append("-n")
            else:
                polyList.append(f"{coefficient}n")
        else:
            if coefficient == 1:
                polyList.append(f"n^{power}")
            elif coefficient == -1:
                polyList.append(f"-n^{power}")
            else:
                polyList.append(f"{coefficient}n^{power}")
    polyString = " + ".join(polyList)
    polyString = polyString.replace("+ -", "- ")
    if not polyList:
        return "0"
    return polyString

def evaluate_polynomial(coefficients,n):
    value = 0
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        value += (coefficient)*((n)**power)
    return value

def geometric_sum(coefficients,n):
    value = 0
    coefficient = coefficients[0]
    rate = coefficients[1]
    for i in range(n):
        value += (coefficient)*(rate)**(i)
    return value

def evaluate_geometric(parameters,n):
    first_term = parameters["First Term"]
    ratio = parameters["Ratio"]
    return first_term * (ratio ** (n - 1))

def subtract_sequences(Seq1,Seq2):
    subSeq = []
    for i in range(len(Seq1)):
        subSeq.append(Seq1[i]-Seq2[i])
    return subSeq


def recover_polynomial(sequence):
    degree = polynomial_degree(sequence)
    coefficients = [0] * (degree + 1)
    remaining = sequence.copy()
    while degree >= 0:
        index = len(coefficients) - degree - 1
        constant_difference = nth_differences(remaining,degree)[0]
        leading = constant_difference / factorial(degree)
        temp_coefficients = [0] * len(coefficients)
        coefficients[index] = leading
        temp_coefficients[index] = leading
        generated = []
        for n in range(1, len(sequence) + 1):
            generated.append(evaluate_polynomial(temp_coefficients, n))
        remaining = subtract_sequences(remaining,generated)
        degree -= 1
    return coefficients

def recover_arithmetic(sequence):
    return [first_differences(sequence)[0],(sequence[0]-first_differences(sequence)[0])]

def recover_geometric(sequence):
    return f"{sequence[0]} · {first_ratios(sequence)[0]}^(n-1)"

def verify_sequence(sequence,report):
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification["Parameters"]
    if sequence_type == "Arithmetic":
        generated = []
        for n in range(1,len(sequence)+1):
            generated.append(evaluate_polynomial(parameters, n))
    elif sequence_type == "Polynomial":
        generated = []
        for n in range(1,len(sequence)+1):
            generated.append(evaluate_polynomial(parameters, n))
    elif sequence_type == "Geometric":
        generated = []
        for n in range(1,len(sequence)+1):
            generated.append(evaluate_geometric(parameters, n))
    elif sequence_type == "Constant":
        generated = [parameters] * len(sequence)
    else:
        return {"Verified": False, "Generated": None}
    return {"Verified":generated == sequence,"Generated": generated}

def predict_terms(sequence,report,number_of_terms=5):
    n = len(sequence) + 1
    predictions = []
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification["Parameters"]
    for n in range(len(sequence)+1,len(sequence)+number_of_terms+1):
        if sequence_type == "Arithmetic":
            predictions.append(evaluate_polynomial(parameters,n))
        elif sequence_type == "Polynomial":
           predictions.append(evaluate_polynomial(parameters,n))
        elif sequence_type == "Constant":
            predictions.append(parameters)
        elif sequence_type == "Geometric":
           predictions.append(evaluate_geometric(parameters,n))
    return predictions

def yes_no(value):
    if value is True:
        return "Yes"
    elif value is False:
        return "No"
    else:
        return "Unknown"

def analyze_sequence(sequence):
    report = {
        "Sequence Classification": {},

        "Verification" : {},

        "Predictions": {},

        "Basic Information": {
            "Length": len(sequence),
            "Minimum": min(sequence),
            "Maximum": max(sequence)
        },
        "Properties": {
            "Is Constant?": is_constant(sequence),
            "Is Increasing?": is_increasing(sequence),
            "Is Decreasing?": is_decreasing(sequence),
            "Is Each Term Unique?": is_unique(sequence),
            "Is Arithmetic?": is_arithmetic(sequence),
            "Is Geometric?": is_geometric(sequence),
            "Polynomial Degree": polynomial_degree(sequence),
        },
        "Transformations": {
            "First Differences": first_differences(sequence),
            "First Ratios": first_ratios(sequence)
        }
        
    }
    report["Sequence Classification"] = classify_sequence(sequence,report)
    if report["Sequence Classification"]["Type"] == "Polynomial":
        coefficients = recover_polynomial(sequence)
        report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")
        report["Sequence Classification"]["Parameters"] = coefficients
    if report["Sequence Classification"]["Type"] == "Arithmetic":
        coefficients = recover_arithmetic(sequence)
        report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")
        report["Sequence Classification"]["Parameters"] = coefficients
    if report["Sequence Classification"]["Type"] == "Geometric":
        report["Sequence Classification"]["Formula"] = (f"a(n) = {recover_geometric(sequence)}")
        report["Sequence Classification"]["Parameters"] = {"First Term":sequence[0],"Ratio":first_ratios(sequence)[0]}
    if report["Sequence Classification"]["Type"] == "Constant":
        report["Sequence Classification"]["Formula"] = (f"a(n) = {sequence[0]}")
        report["Sequence Classification"]["Parameters"] = sequence[0]

    report["Verification"]["Verified"] = verify_sequence(sequence,report)["Verified"]

    report["Predictions"]["Next Terms"] = predict_terms(sequence,report,number_of_terms=5)
    return report

def print_report(report):
    print("""========================================
           MathExplorer Report 
========================================""")
    for section, values in report.items():
        print(section.title())
        print("-" * len(section))
        for key, value in values.items():
            if key == "Parameters":
                continue

            if isinstance(value,bool):
                print(f"{key:<20}: {yes_no(value)}")
            elif value is None:
                continue
            else:
                print(f"{key:<20}: {value}")
        print()
    