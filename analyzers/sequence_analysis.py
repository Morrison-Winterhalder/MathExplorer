from analyzers.pipeline.classify import classify_sequence
from analyzers.pipeline.recovery import recover_formula
from analyzers.pipeline.verification import finalize_report
from analyzers.pipeline.confidence import update_confidence
from analyzers.core.report import initialize_report

def analyze_sequence(sequence):
    if not sequence:
        return None
    report = initialize_report(sequence)
    classification = classify_sequence(sequence, report)
    report["Sequence Classification"] = classification
    recover_formula(sequence, report)
    finalize_report(sequence,report)
    update_confidence(sequence,report)
    return report