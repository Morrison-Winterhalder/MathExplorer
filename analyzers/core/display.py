from analyzers.core.formatter import yes_no, pretty
from analyzers.core.properties import determine_monotonic
from analyzers.core.confidence_formatter import explain_confidence

def print_sequence_classification(report):
    classification = report["Sequence Classification"]

    print("Sequence Classification")
    print("-----------------------")

    family = classification.get("Family")
    tied_families = classification.get("Tied Families", [])

    family = classification.get("Family")

    family_name = family.NAME if family else "Unknown"

    print()
    print("Family")
    print("------")
    print(family_name)

    print()
    print("Hierarchy")
    print("---------")
    print(classification["Hierarchy"])

    # if tree is None:
    #     print("Unknown")
    # else:
    #     print(tree)

    print()

    formula = classification.get("Formula")
    if formula is not None:
        print(f"Formula{'':<9}: {formula}")

    confidence = classification.get("Confidence")
    if confidence is not None:
        score = confidence["Score"]
        if confidence.get("Tied"):
            label = "Ambiguous"
        else:
            label = confidence["Label"]
        print(f"{'Confidence':<16}: {score:.1f}% ({label})")
    print()

    print()

    explanation = explain_confidence(report["Sequence Classification"]["Confidence"])

    print("Confidence Factors")
    print("------------------")

    for reason in explanation:
        print(reason)
    
    parameters = classification.get("Parameters")
    if parameters:
        print()
        print("Parameters")
        print("----------")

        if isinstance(parameters, dict):
            for key, value in parameters.items():
                print(f"{key:<16}: {pretty(value)}")
        else:
            print(pretty(parameters))

    print()

def print_explanation(report):

    explanation = report.get("Explanation")

    if explanation is None:
        return

    print("Explanation")
    print("-----------")

    print(explanation["Summary"])
    print()

    for reason in explanation["Reasons"]:
        print(f"• {reason}")

    print()

def print_recognition_scores(report):
    recognition = report["Recognition Scores"]
    ranking = recognition.get("Ranking") or []
    best_fit = recognition.get("Best Fit")
    classification = report["Sequence Classification"]
    parameters = classification.get("Parameters")

    print("Recognition Scores")
    print("------------------")

    if not ranking:
        print("No recognized families.\n")
        return

    row = "{:<5}{:<35}{:<10}{:<10}{:<10}{:<4}{:<4}"

    print(row.format("Rank", "Family", "RRN", "NRMSE", "R²", "Cx", "Sp"))
    print("-" * len(row.format("Rank", "Family", "RRN", "NRMSE", "R²", "Cx", "Sp")))

    for rank, score in enumerate(ranking, start=1):
        family = score["Family"]

        print(
            row.format(
                rank,
                family.NAME,
                f"{score['RRN']:.4f}",
                f"{score['NRMSE']:.4f}",
                f"{score['R2']:.4f}",
                family.complexity(parameters),
                family.SPECIFICITY
            )
        )

    print()
    print()
    winner_names = ", ".join(
        winner["Family"].NAME
        for winner in best_fit["Winners"]
    )

    print(f"{'Winner(s)':<12}: {winner_names}")

    runner_up = best_fit.get("Runner Up")

    if runner_up is None:
        print(f"{'Runner-Up':<12}: None")
    else:
        print(f"{'Runner-Up':<12}: {runner_up.NAME}")

    print()


def print_predictions(report):
    print("Predictions")
    print("-----------")

    predictions = report["Predictions"]["Next Terms"]

    if predictions is None:
        print("Next Terms      : None")
    else:
        print(f"{'Next Terms':<16}: {pretty(predictions)}")

    print()

def print_verification(report):
    print("Verification")
    print("------------")

    verified = report["Verification"]["Verified"]

    if verified is None:
        print("Verified       : Unknown")
    else:
        print(f"{'Verified':<16}: {yes_no(verified)}")

    print()

def print_basic_information(report):
    print("Basic Information")
    print("-----------------")

    info = report["Basic Information"]

    for key, value in info.items():
        print(f"{key:<16}: {pretty(value)}")

    print()

def print_properties(report):
    family = report["Sequence Classification"]["Family"]
    properties = report["Properties"]

    if family is None:
        return

    print()
    print("Mathematical Properties")
    print("-----------------------")

    print(f"Representation      : {family.REPRESENTATION}")
    print(f"Parent Family       : {family.PARENT}")

    print()

    print(f"Domain              : {family.DOMAIN}")
    print(f"Growth              : {family.GROWTH}")

    print()

    print(
        f"Monotonic           : {properties.get('Monotonic', '-')}"
    )

    print(
        f"Bounded             : {properties.get('Bounded', '-')}"
    )

    print(
        f"Oscillating         : {properties.get('Oscillating', '-')}"
    )

    print(
        f"Periodic            : {properties.get('Periodic', '-')}"
    )

    print()

    print(f"Recognition Method  : {family.RECOGNITION_METHOD}")
    print(f"Reliability         : {family.RELIABILITY}")
    print(f"Minimum Terms       : {family.MIN_TERMS}")

    print()

    print(f"OEIS                : {family.OEIS if family.OEIS is not None else "-"}")

    print()

def print_transformations(report):
    print("Transformations")
    print("---------------")

    transformations = report["Transformations"]

    for key, value in transformations.items():
        if value is None:
            continue

        print(f"{key:<18}: {pretty(value)}")

    print()

def print_report(report, developer=False):
    print("""========================================
          MathExplorer Report
========================================""")
    print()
    if report is None:
        print("Error: Cannot analyze an empty sequence")
        return
    print_sequence_classification(report)
    print_explanation(report)
    print_recognition_scores(report)
    print_predictions(report)
    print_verification(report)
    print_basic_information(report)
    print_properties(report)
    print_transformations(report)
    if developer:
        print()
        print(report["Developer Mind-Model"])