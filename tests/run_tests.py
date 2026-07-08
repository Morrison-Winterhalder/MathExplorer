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