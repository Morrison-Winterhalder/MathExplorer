from math import isclose
from analyzers.pipeline.evaluation import EVALUATION_HANDLERS
from analyzers.pipeline.prediction import predict_terms



def verify_sequence(sequence,report):
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification.get("Parameters")

    evaluator = EVALUATION_HANDLERS.get(sequence_type)

    if evaluator is None:
        return {
            "Verified": None,
            "Generated": None
        }
    
    generated = [
    evaluator(parameters, n)
    for n in range(1, len(sequence) + 1)
    ]

    verified = all(
    isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
    for a, b in zip(generated, sequence)
    )

    return {"Verified":verified,"Generated":generated}

    


def finalize_report(sequence, report):

    classification = report["Sequence Classification"]

    if "Parameters" not in classification:
        report["Verification"]["Verified"] = None
        report["Predictions"]["Next Terms"] = None
        return

    verification = verify_sequence(sequence, report)

    report["Verification"]["Verified"] = verification["Verified"]

    report["Predictions"]["Next Terms"] = predict_terms(
        sequence,
        report,
        number_of_terms=5
    )