from objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence, print_report, classify_sequence, recover_polynomial, format_polynomial, evaluate_polynomial, subtract_sequences, recover_arithmetic
from objects.classifiers import classify_sequence

sequence = [3, 6, 12, 24, 48]

report = analyze_sequence(sequence)

def poly(n):
    return 5*n + 2

print([poly(n) for n in range(1, 7)])

print(recover_arithmetic([7, 12, 17, 22, 27, 32]))

print_report(report)