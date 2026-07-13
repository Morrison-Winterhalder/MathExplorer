from analyzers.pipeline.classify import update_classification
from analyzers.pipeline.recovery import recover_formula
from analyzers.pipeline.verification import finalize_report
from analyzers.pipeline.confidence import update_confidence
from analyzers.core.report import initialize_analysis
from analyzers.pipeline.scoring import update_scores
from analyzers.pipeline.explain import update_explanation

def analyze_sequence(sequence):
    if not sequence:
        return None
    analysis = initialize_analysis(sequence)
    update_scores(sequence, analysis)
    update_classification(sequence, analysis)
    update_explanation(sequence, analysis)
    update_confidence(sequence, analysis)
    recover_formula(sequence, analysis)
    finalize_report(sequence, analysis)
    return analysis