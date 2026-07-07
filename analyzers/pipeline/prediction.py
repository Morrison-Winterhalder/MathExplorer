from analyzers.pipeline.evaluation import EVALUATION_HANDLERS

def predict_terms(sequence, report, number_of_terms=5):
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification.get("Parameters")

    evaluator = EVALUATION_HANDLERS.get(sequence_type)

    if evaluator is None:
        return []

    return [
        evaluator(parameters, n)
        for n in range(
            len(sequence)+1,
            len(sequence)+number_of_terms+1
        )
    ]