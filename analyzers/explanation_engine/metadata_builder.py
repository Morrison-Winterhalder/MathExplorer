from analyzers.explanation_engine.observation import Observation


def metadata_reasons(analysis):

    observations = []

    metadata = analysis.classification.get(
        "Metadata",
        {}
    )

    if not metadata:
        return observations

    growth = metadata.get("GROWTH")

    if growth:

        observations.append(
            Observation(
                text=f"The sequence demonstrates {growth.lower()} growth, matching the expected behavior of this family.",
                category="metadata",
                importance=6,
                type="reason",
                confidence="observed",
                fact=f"{growth.lower()}_growth",
            )
        )

    return observations