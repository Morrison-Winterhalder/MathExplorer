from analyzers.core.transformations import nth_differences
from analyzers.explanation_engine.observation import Observation


def format_difference(values):

    return ", ".join(
        str(value)
        for value in values
    )


def difference_reasons(sequence, analysis, suppress_polynomial=False):

    observations = []

    if suppress_polynomial:
        return observations

    # -----------------------------
    # First Differences
    # -----------------------------

    first = nth_differences(sequence, 1)

    if first:

        observations.append(
            Observation(
                text=f"First differences: {format_difference(first)}.",
                category="difference",
                importance=7,
                type="evidence",
                confidence="observed",
                fact="first_difference",
            )
        )

        if len(set(first)) == 1:

            observations.append(
                Observation(
                    text="Constant first differences indicate linear behavior.",
                    category="difference",
                    importance=10,
                    type="reason",
                    confidence="observed",
                    fact="constant_first_difference",
                )
            )

    # -----------------------------
    # Second Differences
    # -----------------------------

    second = nth_differences(sequence, 2)

    if second:

        observations.append(
            Observation(
                text=f"Second differences: {format_difference(second)}.",
                category="difference",
                importance=8,
                type="evidence",
                confidence="observed",
                fact="second_difference",
            )
        )

        if len(set(second)) == 1:

            observations.append(
                Observation(
                    text="Constant second differences indicate quadratic behavior.",
                    category="difference",
                    importance=10,
                    type="reason",
                    confidence="observed",
                    fact="constant_second_difference",
                )
            )

    # -----------------------------
    # Third Differences
    # -----------------------------

    third = nth_differences(sequence, 3)

    if (
        third
        and not (
            second
            and len(set(second)) == 1
        )
    ):

        observations.append(
            Observation(
                text=f"Third differences: {format_difference(third)}.",
                category="difference",
                importance=9,
                type="evidence",
                confidence="observed",
                fact="third_difference",
            )
        )

        if len(set(third)) == 1:

            observations.append(
                Observation(
                    text="Constant third differences indicate cubic behavior.",
                    category="difference",
                    importance=10,
                    type="reason",
                    confidence="observed",
                    fact="constant_third_difference",
                )
            )

    return observations