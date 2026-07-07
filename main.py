from objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence, print_report, classify_sequence, recover_polynomial, format_polynomial, evaluate_polynomial, subtract_sequences, recover_arithmetic
from objects.classifiers import classify_sequence

sequence = [-7, 5, 161, 833, 2753, 7133, 15785]

report = analyze_sequence(sequence)

sequence = [n**5 - 3*n**3 + 2*n - 7 for n in range(1, 8)]
print(sequence)

print_report(report)