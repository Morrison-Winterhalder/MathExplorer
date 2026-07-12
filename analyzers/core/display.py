from analyzers.core.formatter import yes_no, pretty
from analyzers.core.confidence_formatter import explain_confidence

def print_sequence_classification(report):

    print("Sequence Classification")
    print("-----------------------")

    family_name = report.family_name
    formula = report.formula
    confidence = report.confidence
    parameters = report.parameters

    print()
    print("Family")
    print("------")
    print(family_name)

    print()
    print("Hierarchy")
    print("---------")
    print(report.hierarchy)

    print()

    if formula is not None:
        print(f"Formula{'':<9}: {formula}")

    if confidence is not None:
        print(
            f"{'Confidence':<16}: "
            f"{report.confidence_score:.1f}% "
            f"({report.confidence_label})"
        )
    print()

    explanation = explain_confidence(confidence)

    print("Confidence Factors")
    print("------------------")

    for reason in explanation:
        print(reason)

    if parameters:
        print()
        print("Parameters")
        print("----------")

        for key, value in parameters.items():
            print(f"{key:<16}: {pretty(value)}")


    print()

def print_explanation(report):

    explanation = report.explanation

    if not explanation:
        return

    print("Explanation")
    print("-----------")

    print(explanation["Summary"])
    print()

    for reason in explanation["Reasons"]:
        print(f"• {reason}")

    print()

def print_recognition_scores(report):
    ranking = report.ranking
    best_fit = report.best_fit
    parameters = report.parameters

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
    if best_fit is not None:
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
    else:
        print(f"{'Winner(s)':<12}: None")
        print(f"{'Runner-Up':<12}: None")

    print()


def print_predictions(report):
    print("Predictions")
    print("-----------")

    predictions = report.next_terms

    if predictions is None:
        print("Next Terms      : None")
    else:
        print(f"{'Next Terms':<16}: {pretty(predictions)}")

    print()

def print_verification(report):
    print("Verification")
    print("------------")

    verified = report.verified

    if verified is None:
        print("Verified       : Unknown")
    else:
        print(f"{'Verified':<16}: {yes_no(verified)}")

    print()

def print_basic_information(report):
    print("Basic Information")
    print("-----------------")

    info = report.basic_information

    for key, value in info.items():
        print(f"{key:<16}: {pretty(value)}")

    print()

def print_properties(report):
    family = report.family

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

    print(f"Monotonic           : {report.monotonic}")
    print(f"Bounded             : {report.bounded}")
    print(f"Oscillating         : {report.oscillating}")
    print(f"Periodic            : {report.periodic}")

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

    transformations = report.transformations

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
        print(report.developer_model)