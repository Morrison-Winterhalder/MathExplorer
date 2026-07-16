"""
Confidence Pipeline Stage
"""

from analyzers.confidence_engine.factors import *

from analyzers.confidence_engine.scorer import (
    calculate_confidence,
)

from analyzers.confidence_engine.builder import (
    build_confidence,
)




def update_confidence(sequence, report):
    winner = report.best_fit["Winners"][0]
    runner = report.best_fit["Runner Up Score"]

    winner_error = winner["RRN"]
    runner_error = float("inf") if runner is None else runner["RRN"]

    family = winner["Family"]
    parameters = winner["Parameters"]

    factors = [

        fit_factor(winner_error),

        competition_factor(winner, runner, winner_error, runner_error),

        hierarchy_factor(family),

        observation_factor(report),

        sample_size_factor(len(sequence)),

        complexity_factor(
            family.complexity(
                report.best_fit["Winners"][0]["Parameters"]
            )
        ),

        prediction_verification_factor(report),

        generalization_factor(report),

        naturalness_factor(family),

    ]

    confidence = calculate_confidence(
        factors
    )


    # --------------------------------------------------
    # Record confidence reasoning into the Analysis Trace
    # --------------------------------------------------

    report.analysis_trace.append({

        "stage": "confidence",

        "event": "reasoning_generated",

        "primary": [

            factor

            for factor in confidence["Factors"]

            if factor["impact"] >= 20

        ],

        "supporting": [

            factor

            for factor in confidence["Factors"]

            if 0 < factor["impact"] < 20

        ],

        "uncertainty": [

            factor

            for factor in confidence["Factors"]

            if factor["impact"] <= 0

        ],

    })


    # --------------------------------------------------
    # Build user-facing confidence report
    # --------------------------------------------------

    confidence = build_confidence(
        confidence
    )

    report.analysis_trace.append({

        "stage": "confidence",

        "event": "reasoning_generated",

        "primary": [

            factor

            for factor in confidence["Factors"]

            if factor["impact"] >= 20

        ],

        "supporting": [

            factor

            for factor in confidence["Factors"]

            if 0 < factor["impact"] < 20

        ],

        "uncertainty": [

            factor

            for factor in confidence["Factors"]

            if factor["impact"] <= 0

        ],

    })

    confidence = build_confidence(
        confidence
    )

    report.confidence = confidence