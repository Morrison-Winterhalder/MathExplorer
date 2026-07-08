from analyzers.core.transformations import first_differences, first_ratios
from analyzers.core.properties import is_decreasing, is_increasing, is_unique
from families.triangular import is_triangular
from families.pentagonal import is_pentagonal
from families.fibonacci import is_fibonacci
from families.lucas import is_lucas
from families.pell import is_pell
from families.jacobsthal import is_jacobsthal
from families.factorial import is_factorial
from families.constant import is_constant
from families.arithmetic import is_arithmetic
from families.geometric import is_geometric
from families.polynomial import polynomial_degree

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
            "Is Constant?": is_constant(sequence),
            "Is Increasing?": is_increasing(sequence),
            "Is Decreasing?": is_decreasing(sequence),
            "Is Each Term Unique?": is_unique(sequence),
            "Is Arithmetic?": is_arithmetic(sequence),
            "Is Geometric?": is_geometric(sequence),
            "Polynomial Degree": polynomial_degree(sequence),
            "Is Triangular?": is_triangular(sequence),
            "Is Pentagonal?": is_pentagonal(sequence),
            "Is Fibonacci?": is_fibonacci(sequence),
            "Is Lucas?": is_lucas(sequence),
            "Is Pell?": is_pell(sequence),
            "Is Jacobsthal?": is_jacobsthal(sequence),
            "Is Factorial?": is_factorial(sequence)
        },
        "Transformations": {
            "First Differences": first_differences(sequence),
            "First Ratios": first_ratios(sequence)
        }
        
    }