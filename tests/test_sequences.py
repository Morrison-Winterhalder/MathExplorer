TEST_SEQUENCES = [
    {
        "name": "Constant",
        "sequence": [5, 5, 5],
        "type": "Constant",
        "formula": "a(n) = 5",
        "prediction": [5, 5, 5],
        "verified": True
    },
    {
        "name": "Arithmetic",
        "sequence": [2, 5, 8, 11],
        "type": "Arithmetic",
        "formula": "a(n) = 3n - 1",
        "prediction": [14, 17, 20],
        "verified": True
    },
    {
        "name": "Triangular",
        "sequence": [1, 3, 6, 10, 15],
        "type": "Triangular",
        "formula": "a(n) = n(n+1)/2",
        "prediction": [21, 28, 36],
        "verified": True
    },
]