from .test_classification import run_classification_tests
from .test_recovery import run_recovery_tests
from .test_verification import run_verification_tests
from .test_prediction import run_prediction_tests

def run_all_tests():
    print("Running MathExplorer test suite...\n")

    run_classification_tests()
    run_recovery_tests()
    run_verification_tests()
    run_prediction_tests()

    print("\nAll tests passed!")

run_all_tests()

"""
python3 -m tests.run_tests
"""

feat(v1.5): Add factorial sequence support
- Added factorial family recognition
- Added factorial classification
- Added factorial recovery
- Added factorial evaluation
- Added regression tests for factorial sequences
- Completed the planned v1.5 feature set

release(v1.5): Finalize Version 1.5
MathExplorer v1.5

Completed support for:
- Constant
- Arithmetic
- Geometric
- Polynomial
- Triangular
- Pentagonal
- Fibonacci
- Lucas
- Pell
- Jacobsthal
- Factorial

Highlights:
- Modular pipeline architecture
- Generic linear recurrence engine
- Family-based recognition system
- Recovery, prediction, verification, and evaluation handlers
- Full automated regression test suite