# from analyzers.objects.sequences import prime_numbers, fibonacci, square_numbers
from analyzers.sequence_analysis import analyze_sequence
from analyzers.core.formatting import print_report

sequence = [1, 55, 1065, 6931, 28153, 86871, 223345]

report = analyze_sequence(sequence)

print_report(report)


# sequence = [2*n**6 - 5*n**4 + n**2 + 3 for n in range(1, 8)]
# print(sequence)