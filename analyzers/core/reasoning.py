def build_reasoning(confidence):

    factors = confidence.get(
        "Factors",
        []
    )


    strengths = []
    limitations = []
    notes = []


    for factor in factors:

        impact = factor["impact"]

        if impact > 0:
            strengths.append(
                {
                    "name": factor["name"],
                    "reason": factor["reason"],
                    "impact": impact
                }
            )


        elif impact < 0:
            limitations.append(
                {
                    "name": factor["name"],
                    "reason": factor["reason"],
                    "impact": impact
                }
            )


        else:
            notes.append(
                {
                    "name": factor["name"],
                    "reason": factor["reason"]
                }
            )


    return {

        "Strengths": strengths,

        "Limitations": limitations,

        "Notes": notes,

    }