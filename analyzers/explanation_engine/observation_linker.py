from dataclasses import dataclass


@dataclass
class ObservationLink:

    source: str
    target: str
    relationship: str
    confidence: str = "high"


def build_links(observations):

    links = []

    facts = {
        obs.fact: obs
        for obs in observations
        if obs.fact
    }


    # Difference reasoning

    if (
        "second_difference" in facts
        and
        "constant_second_difference" in facts
    ):

        links.append(
            ObservationLink(
                source="second_difference",
                target="constant_second_difference",
                relationship="supports"
            )
        )


    # Growth reasoning

    if (
        "quadratic_growth" in facts
        and
        "family_definition" in facts
    ):

        links.append(
            ObservationLink(
                source="quadratic_growth",
                target="family_definition",
                relationship="supports"
            )
        )


    # Hierarchy reasoning

    if (
        "family_hierarchy" in facts
        and
        "family_definition" in facts
    ):

        links.append(
            ObservationLink(
                source="family_hierarchy",
                target="family_definition",
                relationship="contextualizes"
            )
        )


    return links