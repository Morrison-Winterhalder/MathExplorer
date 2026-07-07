from math import isclose
from analyzers.pipeline.classify import classify_sequence
from analyzers.core.transformations import first_differences, nth_differences, first_ratios, subtract_sequences
from analyzers.pipeline.evaluation import evaluate_geometric, evaluate_polynomial, geometric_sum
from analyzers.core.utilities import pretty

def clean_coefficients(coefficients, tol=1e-10):
    return [
        0 if abs(c) < tol else c
        for c in coefficients
    ]

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
    