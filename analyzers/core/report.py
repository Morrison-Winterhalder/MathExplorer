from analyzers.core.transformations import first_differences, first_ratios
from analyzers.core.properties import is_decreasing, is_increasing, is_unique
from analyzers.core.properties import determine_monotonic
from analyzers.core.analysis import SequenceAnalysis

def initialize_analysis(sequence):

    analysis = SequenceAnalysis(sequence)

    # -------------------------------------------------
    # Immutable sequence information
    # -------------------------------------------------

    analysis.basic_information = {
        "Length": len(sequence),
        "Minimum": min(sequence),
        "Maximum": max(sequence)
    }

    # -------------------------------------------------
    # Generic mathematical properties
    # -------------------------------------------------

    analysis.properties = {
        "Increasing": is_increasing(sequence),
        "Decreasing": is_decreasing(sequence),
        "Unique": is_unique(sequence),
        "Monotonic": determine_monotonic(sequence),
    }

    # -------------------------------------------------
    # Universal transformations
    # -------------------------------------------------


    analysis.transformations = {
        "First Differences": first_differences(sequence),
        "Second Differences": first_differences(first_differences(sequence)),
        "First Ratios": first_ratios(sequence),
    }

    return analysis