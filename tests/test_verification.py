from analyzers.sequence_analysis import analyze_sequence
from .test_sequences import TEST_SEQUENCES

def run_verification_tests():
    for test in TEST_SEQUENCES:
        report = analyze_sequence(test["sequence"])

        assert (
            report["Verification"]["Verified"] == test["verified"]
        ), (
            f"Verification failed for {test['name']}\n"
            f"Sequence: {test['sequence']}\n"
            f"Expected: {test['verified']}\n"
            f"Got:      {report['Verification']['Verified']}"
        )

    print("Verification tests passed.")