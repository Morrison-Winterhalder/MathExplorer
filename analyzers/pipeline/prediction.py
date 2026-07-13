def predict_terms(sequence, analysis, number_of_terms=5):

    family = analysis.family
    parameters = analysis.parameters

    if family is None or parameters is None:

        analysis.analysis_trace.append({
            "stage": "prediction",
            "event": "prediction_skipped",
            "reason": "no_classification",
        })

        return []

    analysis.analysis_trace.append({
        "stage": "prediction",
        "event": "prediction_started",
        "family": family.NAME,
        "terms_requested": number_of_terms,
        "starting_index": len(sequence) + 1,
    })

    analysis.analysis_trace.append({
        "stage": "prediction",
        "event": "formula_available",
        "family": family.NAME,
        "parameters": parameters,
    })

    predictions = [
        family.evaluate(parameters, n)
        for n in range(
            len(sequence) + 1,
            len(sequence) + number_of_terms + 1
        )
    ]

    analysis.analysis_trace.append({
        "stage": "prediction",
        "event": "predictions_generated",
        "count": len(predictions),
        "starting_index": len(sequence) + 1,
        "first_prediction": predictions[0] if predictions else None,
    })

    analysis.analysis_trace.append({
        "stage": "prediction",
        "event": "prediction_finalized",
    })

    return predictions