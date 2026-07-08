def residuals(sequence, generated):
    return [
        actual - predicted
        for actual, predicted in zip(sequence, generated)
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
        "Generated": predicted,
        "Residuals": residuals(sequence,predicted)
    }