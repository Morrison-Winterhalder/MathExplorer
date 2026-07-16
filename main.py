# from analyzers.objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.display import print_report

sequence = [1, 6, 16, 31, 51, 76]

# 1, 6, 16, 31, 51, 76

report = analyze_sequence(sequence)

# print_report(report, developer=False)

from analyzers.confidence_engine.factors import (
    fit_factor,
    competition_factor,
    hierarchy_factor,
    observation_factor,
    sample_size_factor,
    complexity_factor,
    prediction_factor,
    generalization_factor,
    naturalness_factor,
    prediction_verification_factor
)

from analyzers.confidence_engine.scorer import (
    calculate_confidence,
)


print("\nNEW CONFIDENCE ENGINE DEBUG")
print("----------------------------")


family = report.family

winner = report.best_fit["Winners"][0]
runner_up = report.best_fit["Runner Up Score"]
winner_error = winner["RRN"]

runner_error = (
    float("inf")
    if runner_up is None
    else runner_up["RRN"]
)


factors = [

    fit_factor(
        report.best_fit["Winners"][0]["RRN"]
    ),

    competition_factor(
        winner,
        runner_up,
        winner_error,
        runner_error
    ),

    hierarchy_factor(
        family
    ),

    observation_factor(
        report
    ),

    sample_size_factor(
        len(sequence)
    ),

    complexity_factor(
        family.complexity(
            report.best_fit["Winners"][0]["Parameters"]
        )
    ),

    generalization_factor(
        report
    ),

    naturalness_factor(
        report.family
    ),

    prediction_verification_factor(report),
    

]


confidence = calculate_confidence(
    factors
)


print(
    confidence
)

print_report(report,developer=True)