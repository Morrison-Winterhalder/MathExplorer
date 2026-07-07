from math import isclose
from analyzers.pipeline.evaluation import evaluate_geometric, evaluate_polynomial
from analyzers.pipeline.prediction import predict_terms

def verify_sequence(sequence,report):
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification.get("Parameters")

    if parameters is None:
        return {
            "Verified": None,
            "Generated": None
        }

    if sequence_type == "Arithmetic":
        generated = []
        for n in range(1,len(sequence)+1):
            generated.append(evaluate_polynomial(parameters, n))
    elif sequence_type == "Polynomial":
        generated = []
        for n in range(1,len(sequence)+1):
            generated.append(evaluate_polynomial(parameters, n))
    elif sequence_type == "Geometric":
        generated = []
        for n in range(1,len(sequence)+1):
            generated.append(evaluate_geometric(parameters, n))
    elif sequence_type == "Constant":
        generated = [parameters] * len(sequence)
    else:
        return {"Verified": False, "Generated": None}
    
    verified = all(isclose(a,b,rel_tol=1e-9, abs_tol=1e-9) for a, b in zip(generated,sequence))

    return {"Verified": verified,"Generated": generated}

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