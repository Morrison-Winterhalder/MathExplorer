from analyzers.core.transformations import first_differences, first_ratios
from analyzers.core.properties import is_decreasing, is_increasing, is_unique
from families import triangular
from families import pentagonal
from families import fibonacci
from families import lucas
from families import pell
from families import jacobsthal
from families import factorial
from families import constant
from families import arithmetic
from families import geometric
from families import polynomial

def initialize_report(sequence):
    return {
        "Sequence Classification": {},

        "Recognition Scores": {},

        "Verification" : {},

        "Predictions": {},

        "Basic Information": {
            "Length": len(sequence),
            "Minimum": min(sequence),
            "Maximum": max(sequence)
        },
        "Properties": {
            "Is Constant?": constant.recognize(sequence),
            "Is Increasing?": is_increasing(sequence),
            "Is Decreasing?": is_decreasing(sequence),
            "Is Each Term Unique?": is_unique(sequence),
            "Is Arithmetic?": arithmetic.recognize(sequence),
            "Is Geometric?": geometric.recognize(sequence),
            "Polynomial Degree": polynomial.compute_degree(sequence),
            "Is Triangular?": triangular.recognize(sequence),
            "Is Pentagonal?": pentagonal.recognize(sequence),
            "Is Fibonacci?": fibonacci.recognize(sequence),
            "Is Lucas?": lucas.recognize(sequence),
            "Is Pell?": pell.recognize(sequence),
            "Is Jacobsthal?": jacobsthal.recognize(sequence),
            "Is Factorial?": factorial.recognize(sequence)
        },
        "Transformations": {
            "First Differences": first_differences(sequence),
            "First Ratios": first_ratios(sequence)
        }
        
    }