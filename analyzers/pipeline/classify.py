from families import registry

def update_classification(sequence, analysis):

    analysis.analysis_trace.append({
        "stage": "classification",
        "event": "classification_started",
    })

    best_fit = analysis.recognition_scores["Best Fit"]

    if best_fit is None:
        analysis.classification = {
            "Type": "Unknown",
            "Family": None,
            "Hierarchy": None,
            "Tied Families": [],
            "Parameters": None,
            "Confidence": None,
            "Reason": "No family successfully recognized the sequence."
        }

        analysis.analysis_trace.append({
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

    analysis.classification = {
        "Type": primary["Family"].NAME,
        "Family": primary["Family"],
        "Hierarchy": registry.build_family_tree(
            primary["Family"]
        ),
        "Tied Families": [winner["Family"] for winner in winners],
        "Parameters": primary["Parameters"],
        "Confidence": None,
        "Metadata": primary["Metadata"],
    }

    analysis.analysis_trace.append({
        "stage": "classification",
        "event": "classification_completed",
        "family": primary["Family"].NAME,
        "tied_families": [
            winner["Family"].NAME
            for winner in winners
        ]
    })