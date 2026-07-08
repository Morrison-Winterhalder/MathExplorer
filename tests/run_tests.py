from analyzers.sequence_analysis import analyze_sequence


# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_pipeline():

    report = analyze_sequence([1, 3, 5, 7, 9])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Arithmetic"
    assert classification["Formula"] == "a(n) = 2n - 1"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [11, 13, 15, 17, 19]


# ==========================================================
# Geometric
# ==========================================================

def test_geometric_pipeline():

    report = analyze_sequence([2, 6, 18, 54, 162])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Geometric"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [486, 1458, 4374, 13122, 39366]


# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_pipeline():

    report = analyze_sequence([1, 4, 9, 16, 25])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Polynomial"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [36, 49, 64, 81, 100]


# ==========================================================
# Constant
# ==========================================================

def test_constant_pipeline():

    report = analyze_sequence([7, 7, 7, 7])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Constant"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [7, 7, 7, 7, 7]


# ==========================================================
# Triangular
# ==========================================================

def test_triangular_pipeline():

    report = analyze_sequence([1, 3, 6, 10, 15])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Triangular"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [21, 28, 36, 45, 55]


# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_pipeline():

    report = analyze_sequence([1, 5, 12, 22, 35])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Pentagonal"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [51, 70, 92, 117, 145]


# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_pipeline():

    report = analyze_sequence([1, 1, 2, 3, 5])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Fibonacci"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [8, 13, 21, 34, 55]


# ==========================================================
# Lucas
# ==========================================================

def test_lucas_pipeline():

    report = analyze_sequence([2, 1, 3, 4, 7])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Lucas"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [11, 18, 29, 47, 76]


# ==========================================================
# Pell
# ==========================================================

def test_pell_pipeline():

    report = analyze_sequence([0, 1, 2, 5, 12])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Pell"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [29, 70, 169, 408, 985]


# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_pipeline():

    report = analyze_sequence([0, 1, 1, 3, 5])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Jacobsthal"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [11, 21, 43, 85, 171]


# ==========================================================
# Factorial
# ==========================================================

def test_factorial_pipeline():

    report = analyze_sequence([1, 2, 6, 24, 120])

    classification = report["Sequence Classification"]

    assert classification["Family"].NAME == "Factorial"
    assert report["Verification"]["Verified"]
    assert report["Predictions"]["Next Terms"] == [720, 5040, 40320, 362880, 3628800]


# ==========================================================
# Empty Sequence
# ==========================================================

def test_empty_sequence():

    report = analyze_sequence([])

    assert report is None


# ==========================================================
# Unknown Sequence
# ==========================================================

def test_unknown_sequence():

    report = analyze_sequence([7, -3, 18, 2, 91])

    assert report is not None


# ==========================================================
# Long Sequence
# ==========================================================

def test_long_sequence():

    sequence = [n * n for n in range(1, 51)]

    report = analyze_sequence(sequence)

    assert report["Verification"]["Verified"]


# ==========================================================
# All Known Families
# ==========================================================

def test_all_known_sequences():

    sequences = [
        [1, 3, 5, 7, 9],
        [2, 6, 18, 54],
        [1, 4, 9, 16],
        [7, 7, 7, 7],
        [1, 3, 6, 10],
        [1, 5, 12, 22],
        [1, 1, 2, 3, 5],
        [2, 1, 3, 4, 7],
        [0, 1, 2, 5, 12],
        [0, 1, 1, 3, 5],
        [1, 2, 6, 24, 120],
    ]

    for sequence in sequences:

        report = analyze_sequence(sequence)

        assert report is not None
        assert report["Sequence Classification"]["Family"] is not None
        assert report["Verification"]["Verified"]
        assert report["Predictions"]["Next Terms"] is not None

        