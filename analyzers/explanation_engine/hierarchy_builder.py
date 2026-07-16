from families import registry
from analyzers.explanation_engine.observation import Observation


def hierarchy_reasons(analysis):

    family = analysis.family

    if family is None:
        return []

    lineage = registry.get_lineage(family)

    if not lineage:
        return []

    parent = lineage[0]

    return [
        Observation(
            text=f"{family.NAME} is a subclass of the {parent.NAME} family.",
            category="hierarchy",
            importance=9,
            type="reason",
            confidence="observed",
            fact="family_hierarchy",
        )
    ]