def print_confidence_reasoning(confidence):

    print()

    print("Reasoning")
    print("------------------")
    print()


    primary = [
        factor for factor in confidence["Factors"]
        if factor["name"] == "Exact Formula Match"
    ]


    structural = [
        factor for factor in confidence["Factors"]
        if factor["name"] in {
            "Natural Family",
            "Strong Generalization",
            "Hierarchy Consistency",
            "Simple Explanation",
        }
    ]


    evidence = [
        factor for factor in confidence["Factors"]
        if factor["name"] in {
            "Observed Evidence",
            "Adequate Evidence Sample",
            "Large Evidence Sample",
        }
    ]


    limitations = [
        factor for factor in confidence["Factors"]
        if factor["impact"] < 0
    ]


    notes = [
        factor for factor in confidence["Factors"]
        if factor["impact"] == 0
    ]


    if primary:

        print("Primary Classification")
        print("------------------")

        for factor in primary:
            print(f"✓ {factor['name']}")
            print(f"  {factor['reason']}")
            print()


    if structural:

        print("Why This Family Was Preferred")
        print("------------------")

        for factor in structural:
            print(f"✓ {factor['name']}")
            print(f"  {factor['reason']}")
            print()


    if evidence:

        print("Supporting Evidence")
        print("------------------")

        for factor in evidence:
            print(f"✓ {factor['name']}")
            print(f"  {factor['reason']}")
            print()


    if limitations:

        print("Alternative Explanations")
        print("------------------")

        for factor in limitations:
            print(f"• {factor['reason']}")
            print()


    if notes:

        print("Remaining Uncertainty")
        print("------------------")

        for factor in notes:
            print(f"• {factor['reason']}")
            print()