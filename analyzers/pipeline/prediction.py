from analyzers.pipeline.evaluation import evaluate_geometric, evaluate_polynomial, evaluate_triangular, EVALUATION_HANDLERS

def predict_terms(sequence,report,number_of_terms=5):
    n = len(sequence) + 1
    predictions = []
    classification = report["Sequence Classification"]
    sequence_type = classification["Type"]
    parameters = classification["Parameters"]
    for n in range(len(sequence)+1,len(sequence)+number_of_terms+1):
        if sequence_type == "Arithmetic":
            predictions.append(evaluate_polynomial(parameters,n))
        elif sequence_type == "Polynomial":
           predictions.append(evaluate_polynomial(parameters,n))
        elif sequence_type == "Triangular":
            predictions.append(evaluate_triangular(parameters, n))
        elif sequence_type == "Constant":
            predictions.append(parameters)
        elif sequence_type == "Geometric":
           predictions.append(evaluate_geometric(parameters,n))
    return predictions

# def predict_terms(sequence, report, number_of_terms=5):
#     classification = report["Sequence Classification"]
#     sequence_type = classification["Type"]
#     parameters = classification.get("Parameters")

#     evaluator = EVALUATION_HANDLERS.get(sequence_type)

#     if evaluator is None or parameters is None:
#         return []

#     return [
#         evaluator(parameters, n)
#         for n in range(len(sequence) + 1,
#                        len(sequence) + number_of_terms + 1)
    # ]