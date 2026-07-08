def update_classification(sequence, report):

    best_fit = report["Recognition Scores"]["Best Fit"]

    if best_fit is None:
        report["Sequence Classification"] = {
            "Type": "Unknown",
            "Family": None,
            "Parameters": None,
            "Confidence": None,
            "Reason": "No family successfully recognized the sequence."
        }
        return

    winner = best_fit["Winner Score"]

    report["Sequence Classification"] = {
        "Type": winner["Family"].NAME,
        "Family": winner["Family"],
        "Parameters": winner["Parameters"],
        "Confidence": None
    }