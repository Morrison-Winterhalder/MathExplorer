from analyzers.pipeline.classify import classify_sequence
from analyzers.core.transformations import first_differences, nth_differences, first_ratios, subtract_sequences
from analyzers.pipeline.evaluation import evaluate_geometric, evaluate_polynomial, geometric_sum
from analyzers.core.utilities import pretty
from analyzers.core.properties import is_arithmetic, is_constant, is_decreasing, is_geometric, is_increasing, is_unique, polynomial_degree
from analyzers.pipeline.recovery import recover_arithmetic, recover_geometric, recover_polynomial
from analyzers.pipeline.verification import verify_sequence
from analyzers.pipeline.prediction import predict_terms
from analyzers.pipeline.confidence import determine_confidence
from analyzers.core.formatting import format_polynomial, clean_coefficients

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
    