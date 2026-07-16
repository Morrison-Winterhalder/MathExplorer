from analyzers.core.trace import first_event
from analyzers.explanation_engine.observation import Observation


def specificity_reasons(analysis):

    observations = []

    tie = first_event(
        analysis,
        event="tie_detected",
    )

    resolution = first_event(
        analysis,
        event="tie_resolved",
    )

    if tie:

        tied = [
            name
            for name in tie["families"]
            if name != analysis.family.NAME
        ]

        if tied:

            observations.append(
                Observation(
                    text=f"{', '.join(tied)} also matched exactly.",
                    category="specificity",
                    importance=7,
                    type="reason",
                )
            )

    if resolution:

        observations.append(
            Observation(
                text=(
                    f"{analysis.family.NAME} was selected because "
                    "it is the more specific family."
                ),
                category="specificity",
                importance=9,
                type="reason",
            )
        )

    return observations