from families import registry

def update_classification(sequence, report):

    report["Analysis Trace"].append({
        "stage": "classification",
        "event": "classification_started",
    })

    best_fit = report["Recognition Scores"]["Best Fit"]

    if best_fit is None:
        report["Sequence Classification"] = {
            "Type": "Unknown",
            "Family": None,
            "Hierarchy": None,
            "Tied Families": [],
            "Parameters": None,
            "Confidence": None,
            "Reason": "No family successfully recognized the sequence."
        }

        report["Analysis Trace"].append({
            "stage": "classification",
            "event": "classification_completed",
            "family": None,
        })
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
        "Hierarchy": registry.build_family_tree(
            primary["Family"]
        ),
        "Tied Families": [winner["Family"] for winner in winners],
        "Parameters": primary["Parameters"],
        "Confidence": None
    }

    report["Analysis Trace"].append({
        "stage": "classification",
        "event": "classification_completed",
        "family": primary["Family"].NAME,
        "tied_families": [
            winner["Family"].NAME
            for winner in winners
        ]
    })