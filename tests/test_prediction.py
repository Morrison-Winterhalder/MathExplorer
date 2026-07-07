from analyzers.sequence_analysis import analyze_sequence
from .test_sequences import TEST_SEQUENCES

def run_prediction_tests():
    for test in TEST_SEQUENCES:
        report = analyze_sequence(test["sequence"])

        assert (
            report["Predictions"]["Next Terms"][:3] == test["prediction"]
        ), (
            f"Prediction failed for {test['name']}\n"
            f"Sequence: {test['sequence']}\n"
            f"Expected: {test['prediction']}\n"
            f"Got:      {report['Predictions']['Next Terms'][:3]}"
        )

    print("Prediction tests passed.")