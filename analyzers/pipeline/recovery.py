from analyzers.core.analysis import SequenceAnalysis


def recover_formula(sequence, analysis):

    family = analysis.family
    parameters = analysis.parameters or {}

    if family is None:
        analysis.analysis_trace.append({
            "stage": "recovery",
            "event": "recovery_skipped",
            "reason": "no_classification",
        })
        return

    analysis.analysis_trace.append({
        "stage": "recovery",
        "event": "recovery_started",
        "family": family.NAME,
    })

    try:
        formula = family.formula(parameters)

    except (KeyError, TypeError):
        formula = None

    analysis.formula = formula

    analysis.analysis_trace.append({
        "stage": "recovery",
        "event": "formula_recovered",
        "formula": formula,
    })