def determine_confidence(sequence, report):
    if len(sequence) == 1:
        return "Very Low"
    
    if len(sequence) == 2:
        return "Low"

    confidence = 0
    confidence += len(sequence)
    if report["Verification"]["Verified"]:
        confidence += 2
    sequence_type = report["Sequence Classification"]["Type"]
    if sequence_type in ("Polynomial","Arithmetic","Geometric"):
        confidence += 2


    if confidence >= 9:
        return "Certain"
    elif confidence >= 7:
        return "High"
    elif confidence >= 5:
        return "Medium"
    elif confidence >= 3:
        return "Low"
    else:
        return "Very Low"