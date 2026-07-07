from analyzers.pipeline.classify import classify_sequence
from analyzers.core.transformations import first_differences, nth_differences, first_ratios, subtract_sequences
from analyzers.pipeline.recovery import recover_formula
from analyzers.pipeline.verification import verify_sequence
from analyzers.pipeline.prediction import predict_terms
from analyzers.pipeline.confidence import determine_confidence
from analyzers.core.formatting import format_polynomial, clean_coefficients
from analyzers.core.report import initialize_report

def analyze_sequence(sequence):
    if not sequence:
        return None
    report = initialize_report(sequence)
    report["Sequence Classification"] = classify_sequence(sequence, report)
    recover_formula(sequence, report)
    classification = report["Sequence Classification"]
    if "Parameters" in classification:
        verification = verify_sequence(sequence, report)
        report["Verification"]["Verified"] = verification["Verified"]
        report["Predictions"]["Next Terms"] = predict_terms(sequence, report, number_of_terms=5)
    else:
        report["Verification"]["Verified"] = None
        report["Predictions"]["Next Terms"] = None
    classification["Confidence"] = determine_confidence(sequence, report)
    return report