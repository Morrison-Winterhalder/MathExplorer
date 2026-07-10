from math import isclose
from analyzers.pipeline.prediction import predict_terms
from analyzers.core.mind_model import render_mind_model

def regenerate_sequence(sequence, report):
    classification = report["Sequence Classification"]

    family = classification["Family"]
    parameters = classification["Parameters"]

    return [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 1)
    ]

def verify_sequence(sequence, report):

    classification = report["Sequence Classification"]

    family = classification["Family"]
    parameters = classification["Parameters"]

    generated = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence)+1)
    ]

    return all(
        isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
        for a, b in zip(generated, sequence)
    )


def finalize_report(sequence, report):

    classification = report["Sequence Classification"]

    if (
        classification["Family"] is None
        or classification["Parameters"] is None
    ):

        report["Analysis Trace"].append({
            "stage": "verification",
            "event": "verification_skipped",
            "reason": "no_classification",
        })

        report["Verification"]["Verified"] = None
        report["Predictions"]["Next Terms"] = None
        return

    generated = regenerate_sequence(
        sequence,
        report
    )

    report["Predictions"]["Next Terms"] = predict_terms(
        sequence,
        report,
        number_of_terms=5,
    )

    report["Analysis Trace"].append({
        "stage": "verification",
        "event": "verification_started",
        "family": classification["Family"].NAME,
    })

    verified = verify_sequence(
        sequence,
        report,
    )

    report["Verification"]["Verified"] = verified

    report["Analysis Trace"].append({
        "stage": "verification",
        "event": "verification_completed",
        "verified": verified,
        "generated": generated,
    })

    report["Analysis Trace"].append({
        "stage": "pipeline",
        "event": "analysis_completed",
    })

    report["Developer Mind-Model"] = render_mind_model(report)