def recover_formula(sequence, report):

    classification = report["Sequence Classification"]

    family = classification["Family"]
    parameters = classification.get("Parameters", {})

    if family is None:
        return

    report["Analysis Trace"].append({
        "stage": "recovery",
        "event": "recovery_started",
        "family": family.NAME,
    })

    try:
        formula = family.formula(parameters)

    except (KeyError, TypeError):
        formula = None

    report["Sequence Classification"]["Formula"] = formula

    report["Analysis Trace"].append({
        "stage": "recovery",
        "event": "formula_recovered",
        "formula": formula,
    })