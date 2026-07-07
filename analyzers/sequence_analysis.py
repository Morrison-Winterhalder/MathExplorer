from analyzers.pipeline.classify import classify_sequence
from analyzers.core.transformations import first_differences, nth_differences, first_ratios, subtract_sequences
from analyzers.pipeline.recovery import recover_arithmetic, recover_geometric, recover_polynomial
from analyzers.pipeline.verification import verify_sequence
from analyzers.pipeline.prediction import predict_terms
from analyzers.pipeline.confidence import determine_confidence
from analyzers.core.formatting import format_polynomial, clean_coefficients
from analyzers.core.report import initialize_report

def analyze_sequence(sequence):
    if sequence == []:
        return None
    report = initialize_report(sequence)
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
    