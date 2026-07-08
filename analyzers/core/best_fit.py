def residuals(sequence, predicted):
    return [
        actual - predicted
        for actual, predicted in zip(sequence, predicted)
    ]

def best_fit(sequence, family):
    parameters = family.fit(sequence)

    if parameters is None:
        return None

    predicted = [
        family.evaluate(parameters, n)
        for n in range(1, len(sequence) + 1)
    ]

    return {
        "Parameters": parameters,
        "Predicted": predicted,
        "Residuals": residuals(sequence,predicted)
    }