from analyzers.sequence_analysis import analyze_sequence
from .test_sequences import TEST_SEQUENCES

def run_recovery_tests():
    for test in TEST_SEQUENCES:
        report = analyze_sequence(test["sequence"])

        assert (
            report["Sequence Classification"]["Formula"] == test["formula"]
        ), (
            f"Recovery failed for {test['name']}\n"
            f"Sequence: {test['sequence']}\n"
            f"Expected: {test['formula']}\n"
            f"Got:      {report['Sequence Classification']['Formula']}"
        )

    print("Recovery tests passed.")