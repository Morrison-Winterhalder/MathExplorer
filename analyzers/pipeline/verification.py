from math import isclose
from analyzers.pipeline.prediction import predict_terms
from analyzers.core.mind_model import render_mind_model

def regenerate_sequence(sequence, analysis):

    family = analysis.family
    parameters = analysis.parameters

    return [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 1)
    ]

def verify_sequence(sequence, analysis):

    family = analysis.family
    parameters = analysis.parameters

    generated = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence)+1)
    ]

    return all(
        isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
        for a, b in zip(generated, sequence)
    )


def finalize_report(sequence, analysis):

    family = analysis.family
    parameters = analysis.parameters

    if (
        family is None
        or parameters is None
    ):

        analysis.analysis_trace.append({
            "stage": "verification",
            "event": "verification_skipped",
            "reason": "no_classification",
        })

        analysis.verification["Verified"] = None
        analysis.predictions["Next Terms"] = None
        return

    generated = regenerate_sequence(
        sequence,
        analysis
    )

    analysis.predictions["Next Terms"] = predict_terms(
        sequence,
        analysis,
        number_of_terms=5,
    )

    analysis.analysis_trace.append({
        "stage": "verification",
        "event": "verification_started",
        "family": analysis.family_name,
    })

    verified = verify_sequence(
        sequence,
        analysis,
    )

    analysis.verification["Verified"] = verified

    analysis.analysis_trace.append({
        "stage": "verification",
        "event": "verification_completed",
        "verified": verified,
        "generated": generated,
    })

    analysis.analysis_trace.append({
        "stage": "pipeline",
        "event": "analysis_completed",
    })

    analysis.developer_model = render_mind_model(analysis)