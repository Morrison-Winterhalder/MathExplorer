from analyzers.core.transformations import first_ratios
from analyzers.explanation_engine.observation import Observation


def format_ratios(values):

    return ", ".join(
        str(value)
        for value in values
    )


def ratio_reasons(sequence, analysis):

    observations = []

    ratios = first_ratios(sequence)

    if not ratios:
        return observations

    if len(set(ratios)) == 1:

        observations.append(
            Observation(
                text=f"Consecutive ratios: {format_ratios(ratios)}.",
                category="ratio",
                importance=8,
                type="evidence",
            )
        )

        observations.append(
            Observation(
                text="Constant ratios indicate exponential behavior.",
                category="ratio",
                importance=10,
                type="reason",
            )
        )

    return observations