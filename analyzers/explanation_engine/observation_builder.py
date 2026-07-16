from analyzers.explanation_engine.observation import Observation
from analyzers.core.properties import (
    is_increasing,
)


def observation_reasons(sequence, analysis):

    observations = []


    # -----------------------------
    # Monotonic behavior
    # -----------------------------

    if is_increasing(sequence):

        observations.append(
            Observation(
                text="The sequence is strictly increasing.",
                category="property",
                importance=3,
                type="observation",
                fact="increasing_sequence",
            )
        )


    # -----------------------------
    # Integer values
    # -----------------------------

    if all(
        isinstance(x, int)
        for x in sequence
    ):

        observations.append(
            Observation(
                text="All observed terms are integers.",
                category="property",
                importance=2,
                type="observation",
                fact="integer_sequence",
            )
        )


    # -----------------------------
    # Length information
    # -----------------------------

    if len(sequence) >= 5:

        observations.append(
            Observation(
                text=(
                    "The sequence contains enough terms "
                    "for structural analysis."
                ),
                category="property",
                importance=3,
                type="observation",
                fact="sufficient_terms",
            )
        )


    return observations