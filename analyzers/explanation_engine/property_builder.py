from analyzers.explanation_engine.observation import Observation
from analyzers.core.properties import (
    is_increasing,
    is_decreasing,
)


def property_reasons(sequence, analysis):

    observations = []

    if is_increasing(sequence):

        observations.append(
            Observation(
                text="The sequence is strictly increasing.",
                category="property",
                importance=3,
                type="observation",
            )
        )

    elif is_decreasing(sequence):

        observations.append(
            Observation(
                text="The sequence is strictly decreasing.",
                category="property",
                importance=3,
                type="observation",
            )
        )

    if all(isinstance(x, int) for x in sequence):

        observations.append(
            Observation(
                text="All observed terms are integers.",
                category="property",
                importance=2,
                type="observation",
            )
        )

    return observations