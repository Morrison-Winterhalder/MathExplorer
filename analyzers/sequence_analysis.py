from analyzers.pipeline.classify import update_classification
from analyzers.pipeline.recovery import recover_formula
from analyzers.pipeline.verification import finalize_report
from analyzers.pipeline.confidence import update_confidence
from analyzers.core.report import initialize_report
from analyzers.pipeline.scoring import update_scores

def analyze_sequence(sequence):
    if not sequence:
        return None
    report = initialize_report(sequence)
    update_scores(sequence, report)
    update_classification(sequence, report)
    update_confidence(sequence, report)
    recover_formula(sequence, report)
    finalize_report(sequence, report)
    return report