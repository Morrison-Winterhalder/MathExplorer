from analyzers.core.report import initialize_analysis

from analyzers.pipeline.scoring import update_scores
from analyzers.pipeline.classify import update_classification
from analyzers.pipeline.explain import update_explanation

from analyzers.pipeline.recovery import recover_formula
from analyzers.pipeline.confidence import update_confidence
from analyzers.pipeline.verification import finalize_report


def analyze_sequence(sequence):
    """
    MathExplorer v3.0 Analysis Pipeline

    Observation
        ↓
    Recognition
        ↓
    Classification
        ↓
    Explanation
        ↓
    Formula Recovery
        ↓
    Confidence Assessment
        ↓
    Prediction & Verification
    """

    if not sequence:
        return None

    # -----------------------------------------
    # Initialize analysis
    # -----------------------------------------

    analysis = initialize_analysis(sequence)

    # -----------------------------------------
    # Observation / Recognition
    # -----------------------------------------

    update_scores(sequence, analysis)

    # -----------------------------------------
    # Classification
    # -----------------------------------------

    update_classification(sequence, analysis)

    # -----------------------------------------
    # Explanation Engine
    # -----------------------------------------

    update_explanation(sequence, analysis)

    # -----------------------------------------
    # Formula Recovery
    # -----------------------------------------

    recover_formula(sequence, analysis)

    # -----------------------------------------
    # Confidence Engine
    # -----------------------------------------

    update_confidence(sequence, analysis)

    # -----------------------------------------
    # Prediction & Verification
    # -----------------------------------------

    finalize_report(sequence, analysis)

    return analysis