from math import isclose
from analyzers.pipeline.prediction import predict_terms



def verify_sequence(sequence, report):
    classification = report["Sequence Classification"]
    family = classification["Family"]
    parameters = classification["Parameters"]

    generated = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 1)
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
        
        report["Verification"]["Verified"] = None
        report["Predictions"]["Next Terms"] = None
        return

    report["Verification"]["Verified"] = verify_sequence(
        sequence,
        report
    )

    report["Predictions"]["Next Terms"] = predict_terms(
        sequence,
        report,
        number_of_terms=5
    )