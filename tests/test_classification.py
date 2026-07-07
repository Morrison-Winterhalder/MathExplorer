from analyzers.sequence_analysis import analyze_sequence
from .test_sequences import TEST_SEQUENCES

def run_classification_tests():
    for test in TEST_SEQUENCES:
        report = analyze_sequence(test["sequence"])

        assert (
            report["Sequence Classification"]["Type"] == test["type"]
        ), (
            f"Classification failed for {test['name']}\n"
            f"Sequence: {test['sequence']}\n"
            f"Expected: {test['type']}\n"
            f"Got:      {report['Sequence Classification']['Type']}"
        )

    print("Classification tests passed.")