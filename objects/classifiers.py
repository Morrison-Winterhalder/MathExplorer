def classify_sequence(sequence, report):
    properties = report["Properties"]
    transformations = report["Transformations"]
    if properties["Is Constant?"] is True:
        return {"Type": "Constant",
                "Degree": 0,
                "Common Difference": 0,
                "Common Ratio": 1,
                "Confidence": "Certain",
                "Reason": "Sequence is constant."}
    elif properties["Is Arithmetic?"] is True:
        return {"Type": "Arithmetic",
                "Common Difference": transformations["First Differences"][0],
                "Common Ratio": None,
                "Confidence": "Certain",
                "Reason": "First differences are constant."}
    elif properties["Is Geometric?"] is True:
        return {"Type": "Geometric",
                "Degree": None,
                "Common Difference": None,
                "Common Ratio": transformations["First Ratios"][0],
                "Confidence": "Certain",
                "Reason": "First ratios are constant."}
    elif properties["Polynomial Degree"] is not None:
        return {"Type": "Polynomial",
                "Degree": properties["Polynomial Degree"],
                "Common Difference": None,
                "Common Ratio": None,
                "Confidence": "Certain",
                "Reason": "Nth differences become constant."}
    else:
        return {"Type": "Unknown",
                "Degree": None,
                "Common Difference": None,
                "Common Ratio": None,
                "Family": None,
                "Confidence": "Low",
                "Reason": "No implemented classifier matched."}