from math import factorial, isclose
from objects.classifiers import classify_sequence

def pretty(value):
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        return value

    elif isinstance(value, list):
        return [pretty(v) for v in value]

    elif isinstance(value, dict):
        return {k: pretty(v) for k, v in value.items()}

    return value

def clean_coefficients(coefficients, tol=1e-10):
    return [
        0 if abs(c) < tol else c
        for c in coefficients
    ]

def first_differences(sequence):
    if len(sequence) < 2:
        return []
    first_difference_sequence = []
    for i in range(0,len(sequence)-1):
        first_difference_sequence.append(sequence[i+1]-sequence[i])
    return first_difference_sequence

def nth_differences(sequence,n):
    if len(sequence) < 2:
        return []
    changing_sequence = sequence
    for _ in range(n):
        changing_sequence = first_differences(changing_sequence)
    return changing_sequence

def is_constant(sequence):
    if len(sequence) == 0:
        return None
    for value in sequence[1:]:
        if value != sequence[0]:
            return False
    return True

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

def format_polynomial(coefficients):
    polyList = []
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        if coefficient == 0:
            continue
        elif power == 0:
            polyList.append(str(pretty(coefficient)))
        elif power == 1:
            if coefficient == 1:
                polyList.append("n")
            elif coefficient == -1:
                polyList.append("-n")
            else:
                polyList.append(f"{pretty(coefficient)}n")
        else:
            if coefficient == 1:
                polyList.append(f"n^{pretty(power)}")
            elif coefficient == -1:
                polyList.append(f"-n^{pretty(power)}")
            else:
                polyList.append(f"{pretty(coefficient)}n^{pretty(power)}")
    polyList = pretty(polyList)
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
    if len(sequence) < 2:
        return None
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
    if len(sequence) < 2:
        return []
    return [first_differences(sequence)[0],(sequence[0]-first_differences(sequence)[0])]

def recover_geometric(sequence):
    if len(sequence) < 2:
        return None
    return f"{pretty(sequence[0])} · {pretty(first_ratios(sequence)[0])}^(n-1)"

def determine_confidence(sequence, report):
    if len(sequence) == 1:
        return "Very Low"
    
    if len(sequence) == 2:
        return "Low"

    confidence = 0
    confidence += len(sequence)
    if report["Verification"]["Verified"]:
        confidence += 2
    sequence_type = report["Sequence Classification"]["Type"]
    if sequence_type in ("Polynomial","Arithmetic","Geometric"):
        confidence += 2


    if confidence >= 9:
        return "Certain"
    elif confidence >= 7:
        return "High"
    elif confidence >= 5:
        return "Medium"
    elif confidence >= 3:
        return "Low"
    else:
        return "Very Low"

def verify_sequence(sequence,report):
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification.get("Parameters")

    if parameters is None:
        return {
            "Verified": None,
            "Generated": None
        }

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
    
    verified = all(isclose(a,b,rel_tol=1e-9, abs_tol=1e-9) for a, b in zip(generated,sequence))

    return {"Verified": verified,"Generated": generated}

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
    if sequence == []:
        return None
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
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    if report["Sequence Classification"]["Type"] == "Polynomial":
        coefficients = recover_polynomial(sequence)
        print(coefficients)
        coefficients = clean_coefficients(coefficients)
        print(coefficients)
        report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")
        report["Sequence Classification"]["Parameters"] = coefficients
    elif report["Sequence Classification"]["Type"] == "Arithmetic":
        coefficients = recover_arithmetic(sequence)
        report["Sequence Classification"]["Parameters"] = coefficients
        coefficients = clean_coefficients(coefficients)
        report["Sequence Classification"]["Formula"] = (f"a(n) = {format_polynomial(coefficients)}")
    elif report["Sequence Classification"]["Type"] == "Geometric":
        report["Sequence Classification"]["Formula"] = (f"a(n) = {recover_geometric(sequence)}")
        report["Sequence Classification"]["Parameters"] = {"First Term":sequence[0],"Ratio":first_ratios(sequence)[0]}
    elif report["Sequence Classification"]["Type"] == "Constant":
        report["Sequence Classification"]["Formula"] = (f"a(n) = {sequence[0]}")
        report["Sequence Classification"]["Parameters"] = sequence[0]

    if "Parameters" in classification:
        verification = verify_sequence(sequence, report)
        report["Verification"]["Verified"] = verification["Verified"]
        report["Predictions"]["Next Terms"] = predict_terms(
            sequence,
            report,
            number_of_terms=5)
    else:
        report["Verification"]["Verified"] = None
        report["Predictions"]["Next Terms"] = None

    report["Sequence Classification"]["Confidence"] = determine_confidence(sequence,report)
    return report

def print_report(report):
    print("""========================================
           MathExplorer Report 
========================================""")
    print()
    if report == None:
        print("Error: Cannot analyze an empty sequence")
        return
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
                print(f"{key:<20}: {pretty(value)}")
        print()
    