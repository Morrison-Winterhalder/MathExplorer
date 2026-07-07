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
    {
        "name": "Polynomial (Cubic)",
        "sequence": [0, 11, 46, 117, 236],
        "type": "Polynomial",
        "formula": "a(n) = 2n^3 - 3n + 1",
        "prediction": [415, 666, 1001],
        "verified": True,
    },
    {
        "name": "Geometric (Ratio 3)",
        "sequence": [5, 15, 45, 135, 405],
        "type": "Geometric",
        "formula": "a(n) = 5 · 3^(n-1)",
        "prediction": [1215, 3645, 10935],
        "verified": True,
    },
    {
        "name": "Pentagonal",
        "sequence": [1, 5, 12, 22, 35],
        "type": "Pentagonal",
        "formula": "a(n) = n(3n-1)/2",
        "prediction": [51, 70, 92],
        "verified": True,
    }
]