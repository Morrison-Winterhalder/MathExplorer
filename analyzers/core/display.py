from analyzers.core.formatter import yes_no, pretty
from analyzers.core.confidence_formatter import explain_confidence
from analyzers.explanation_engine.explanation_renderer import (
    render_explanation,
)
from analyzers.core.confidence_display import (
    print_confidence_reasoning,
)

def print_sequence_classification(report):

    print("Sequence Classification")
    print("-----------------------")

    family_name = report.family_name
    formula = report.formula

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

    print()

    if report.confidence is not None:

        print("Confidence")
        print("-" * 24)
        print()

        print(
            f"Score: {report.confidence_score:.1f}% "
            f"({report.confidence_label})"
        )

        print()

        print_confidence_reasoning(
            report.confidence
        )

    print()

def print_explanation(analysis):

    explanation = analysis.explanation

    if explanation is None:
        return

    print()
    print("Explanation")
    print("------------------------")
    print()

    print("Summary")
    print("-------")
    print(explanation["Summary"])
    print()

    # Future-proof grouping support
    if "Sections" in explanation:

        for section in explanation["Sections"]:

            print(section["Title"])
            print("-" * len(section["Title"]))

            for item in section["Items"]:
                print(f"• {item}")

            print()

    else:

        print("Reasons")
        print("-------")

        for observation in explanation["Reasons"]:
            print(f"• {observation.text}")

        print()

    print("Evidence")
    print("--------")

    for item in explanation["Evidence"]:
        print(f"• {item}")

    print()

    if explanation["Warnings"]:
        print("Notes")
        print("-----")

        for warning in explanation["Warnings"]:
            print(f"• {warning}")

        print()

def print_recognition_scores(report):
    ranking = report.ranking
    best_fit = report.best_fit
    parameters = report.parameters

    print("Candidate Comparison")
    print("--------------------")

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

        print()

        print("Summary")
        print("-------")

        print()

        print("Winner")
        print("------")
        print(winner_names)

        print()

        print("Runner-Up")
        print("---------")

        runner_up = best_fit.get("Runner Up")

        if runner_up is None:
            print("None")
        else:
            print(runner_up.NAME)

        print()


def print_predictions(report):

    print("Predictions")
    print("-----------")

    predictions = report.next_terms

    if predictions is None:
        print("No predictions available.")
        print()
        return

    print()

    print("Predicted Terms")
    print("---------------")

    start = len(report.sequence) + 1

    for i, value in enumerate(predictions):
        print(f"a({start+i}) = {pretty(value)}")

    print()

def print_verification(report):

    print("Verification")
    print("------------")
    print()

    verified = report.verified

    if verified is None:

        print("• Verification has not been performed.")

    elif verified:

        print("✓ Formula exactly reproduces every observed term.")

    else:

        print("✗ Formula does not reproduce every observed term.")

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

    print("Structural Analysis")
    print("-------------------")

    transformations = report.transformations

    # Difference-based analysis
    difference_keys = [
        "First Differences",
        "Second Differences",
        "Third Differences",
        "Fourth Differences",
    ]

    printed_difference_header = False

    for key in difference_keys:

        value = transformations.get(key)

        if value is None:
            continue

        if not printed_difference_header:
            print()
            print("Difference Tables")
            print("-----------------")
            printed_difference_header = True

        print(f"{key:<20}: {pretty(value)}")

    # Ratio-based analysis
    ratio_keys = [
        "First Ratios",
        "Second Ratios",
    ]

    printed_ratio_header = False

    for key in ratio_keys:

        value = transformations.get(key)

        if value is None:
            continue

        if not printed_ratio_header:
            print()
            print("Ratio Analysis")
            print("--------------")
            printed_ratio_header = True

        print(f"{key:<20}: {pretty(value)}")

    # Any future transformations automatically appear here
    used = set(difference_keys + ratio_keys)

    extras = [
        (key, value)
        for key, value in transformations.items()
        if key not in used and value is not None
    ]

    if extras:
        print()
        print("Additional Analysis")
        print("-------------------")

        for key, value in extras:
            print(f"{key:<20}: {pretty(value)}")

    print()

def print_report(report, developer=False):

    print("""========================================
          MathExplorer Report
========================================""")
    print()

    if report is None:
        print("Error: Cannot analyze an empty sequence")
        return

    # 1. Final answer
    print_sequence_classification(report)

    # 2. Mathematical reasoning
    print_explanation(report)

    # 3. Alternative candidates and why they lost
    print_recognition_scores(report)

    # 4. Predictions produced from the recovered formula
    print_predictions(report)

    # 5. Verification of those predictions
    print_verification(report)

    # 6. Mathematical description of the recognized family
    print_properties(report)

    # 7. Structural analysis that led to the classification
    print_transformations(report)

    # 8. Raw metadata (least important)
    print_basic_information(report)

    # 9. Developer trace
    if developer:
        print()
        print(report.developer_model)