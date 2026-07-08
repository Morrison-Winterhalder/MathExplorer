def predict_terms(sequence, report, number_of_terms=5):
    classification = report["Sequence Classification"]

    family = classification["Family"]
    parameters = classification["Parameters"]

    if family is None or parameters is None:
        return []

    return [
        family.evaluate(parameters, n)
        for n in range(
            len(sequence) + 1,
            len(sequence) + number_of_terms + 1
        )
    ]