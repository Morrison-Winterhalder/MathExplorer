from analyzers.explanation_engine.inference_rules import get_rule


def build_reasoning_chain(reasons):

    chain = []

    for observation in reasons:

        rule = get_rule(
            observation.fact
        )

        if rule:

            chain.append(
                rule(observation)
            )

    chain.sort(
        key=lambda step: step.priority,
        reverse=True,
    )

    return chain