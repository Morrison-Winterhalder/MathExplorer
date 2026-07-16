from analyzers.explanation_engine.explanation_builder import build_explanation

def update_explanation(sequence, analysis):

    if analysis.family is None:
        analysis.explanation = None
        return

    analysis.explanation = build_explanation(sequence, analysis)