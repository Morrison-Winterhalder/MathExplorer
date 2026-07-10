# from analyzers.objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.display import print_report

sequence = [2,6,18,54,162]

report = analyze_sequence(sequence)

print_report(report, developer=False)


# sequence = [0.5*(n)**2 + 0.5*n for n in range(1, 8)]
# print(sequence)