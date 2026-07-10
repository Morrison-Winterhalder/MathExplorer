def recover_formula(sequence, report):

    classification = report["Sequence Classification"]

    family = classification["Family"]
    parameters = classification["Parameters"]

    if family is None:
        return

    report["Analysis Trace"].append({
        "stage": "recovery",
        "event": "recovery_started",
        "family": family.NAME,
    })

    report["Sequence Classification"]["Formula"] = (
        family.formula(parameters)
    )

    report["Analysis Trace"].append({
        "stage": "recovery",
        "event": "formula_recovered",
        "formula": report["Sequence Classification"]["Formula"],
    })