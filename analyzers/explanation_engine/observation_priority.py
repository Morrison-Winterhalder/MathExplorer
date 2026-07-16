def prioritize_observations(observations):

    return sorted(
        observations,
        key=lambda observation: observation.importance,
        reverse=True,
    )

def observation_group(reason):

    if "differences:" in reason:
        return "difference_evidence"

    if "Constant first differences" in reason:
        return "difference_reason"

    if "Constant second differences" in reason:
        return "difference_reason"

    if "Constant third differences" in reason:
        return "difference_reason"

    if "ratios:" in reason:
        return "ratio_evidence"

    if "Constant ratios" in reason:
        return "ratio_reason"

    return "general"