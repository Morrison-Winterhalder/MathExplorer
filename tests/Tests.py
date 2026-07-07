import os
import sys

print("cwd =", os.getcwd())
print("sys.path[0] =", sys.path[0])
from analyzers.sequence_analysis import recover_polynomial, evaluate_polynomial

tests = [
    [1, -2, 3, -4],      # n^3 - 2n^2 + 3n - 4
    [-1, 1, -1, 1, -1, 1],
    [3, 0, 0, -5, 0, 0, 2],
]

for coeffs in tests:
    sequence = [
        evaluate_polynomial(coeffs, n)
        for n in range(1, 8)
    ]

    recovered = recover_polynomial(sequence)

    print("Original :", coeffs)
    print("Recovered:", recovered)
    print()