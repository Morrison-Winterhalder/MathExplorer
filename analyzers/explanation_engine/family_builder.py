from analyzers.explanation_engine.observation import Observation


def family_reasons(analysis):

    family = analysis.family

    if family is None:
        return []

    if not hasattr(family, "explain"):
        return []

    explanation = family.explain(
        analysis.parameters
    )

    if not explanation:
        return []

    observations = []

    for reason in explanation:

        observations.append(
            Observation(
                text=reason,
                category="family",
                importance=8,
                type="reason",
                confidence="observed",
                fact="family_definition",
            )
        )

    return observations