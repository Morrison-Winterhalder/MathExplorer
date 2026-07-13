# from analyzers.objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.display import print_report

sequence = [1, 6, 16, 31, 51, 76]

# 1, 6, 16, 31, 51, 76

report = analyze_sequence(sequence)

print_report(report, developer=True)


# sequence = [0.5*(n)**2 + 0.5*n for n in range(1, 8)]
# print(sequence)