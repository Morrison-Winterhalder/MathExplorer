def update_classification(sequence, report):

    best_fit = report["Recognition Scores"]["Best Fit"]

    if best_fit is None:
        report["Sequence Classification"] = {
            "Type": "Unknown",
            "Family": None,
            "Tied Families": [],
            "Parameters": None,
            "Confidence": None,
            "Reason": "No family successfully recognized the sequence."
        }
        return

    winners = best_fit["Winners"]

    primary = min(
        winners,
        key=lambda winner: winner["Family"].complexity(
            winner["Parameters"]
        )
    )

    report["Sequence Classification"] = {
        "Type": primary["Family"].NAME,
        "Family": primary["Family"],
        "Tied Families": [winner["Family"] for winner in winners],
        "Parameters": primary["Parameters"],
        "Confidence": None
    }