# from analyzers.objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.display import print_report

sequence = [0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5]

# 1, 6, 16, 31, 51, 76

report = analyze_sequence(sequence)

print_report(report,developer=True)
