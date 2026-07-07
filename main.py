# from analyzers.objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence, classify_sequence, recover_polynomial, format_polynomial, evaluate_polynomial, subtract_sequences, recover_arithmetic
from analyzers.pipeline.classify import classify_sequence
from analyzers.core.formatting import print_report

sequence = [-7, 5, 161, 833, 2753, 7133, 15785]

report = analyze_sequence(sequence)

sequence = [n**5 - 3*n**3 + 2*n - 7 for n in range(1, 8)]
print(sequence)

print_report(report)