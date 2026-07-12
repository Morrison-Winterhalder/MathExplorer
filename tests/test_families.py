from families import (
    arithmetic,
    geometric,
    polynomial,
    constant,
    triangular,
    pentagonal,
    fibonacci,
    lucas,
    pell,
    jacobsthal,
    factorial,
    tribonacci,
    tetranacci,
    padovan,
    perrin,
    centered_triangular,
    centered_square,
    centered_pentagonal,
    centered_hexagonal,
)

# ==========================================================
# Arithmetic
# ==========================================================

def test_arithmetic_fit():
    params = arithmetic.fit([1, 3, 5, 7, 9])
    assert params["Difference"] == 2
    assert params["Intercept"] == -1

def test_arithmetic_evaluate():
    params = {"Difference": 2, "Intercept": -1}
    generated = [arithmetic.evaluate(params, n) for n in range(1, 6)]
    assert generated == [1, 3, 5, 7, 9]

def test_arithmetic_complexity():
    assert arithmetic.complexity({"Difference": 2, "Intercept": -1}) == 1

# ==========================================================
# Geometric
# ==========================================================

def test_geometric_fit():
    params = geometric.fit([2, 6, 18, 54, 162])
    assert params["First Term"] == 2
    assert params["Ratio"] == 3

def test_geometric_evaluate():
    params = {"First Term": 2, "Ratio": 3}
    generated = [geometric.evaluate(params, n) for n in range(1, 6)]
    assert generated == [2, 6, 18, 54, 162]

def test_geometric_complexity():
    assert geometric.complexity({"First Term": 2, "Ratio": 3}) == 1

# ==========================================================
# Polynomial
# ==========================================================

def test_polynomial_fit():
    params = polynomial.fit([1, 4, 9, 16, 25])
    assert len(params) == 3

def test_polynomial_evaluate():
    params = polynomial.fit([1, 4, 9, 16, 25])
    generated = [polynomial.evaluate(params, n) for n in range(1, 6)]
    assert generated == [1, 4, 9, 16, 25]

def test_polynomial_complexity():
    params = polynomial.fit([1, 4, 9, 16, 25])   # quadratic
    assert polynomial.complexity(params) == 4

# ==========================================================
# Constant
# ==========================================================

def test_constant_fit():
    params = constant.fit([7, 7, 7, 7])
    assert params["Value"] == 7

def test_constant_evaluate():
    params = {"Value": 7}
    generated = [constant.evaluate(params, n) for n in range(1, 5)]
    assert generated == [7, 7, 7, 7]

def test_constant_complexity():
    assert constant.complexity({"Value": 7}) == 0

# ==========================================================
# Triangular
# ==========================================================

def test_triangular_fit():
    params = triangular.fit([1, 3, 6, 10, 15])
    assert params is not None

def test_triangular_evaluate():
    params = triangular.fit([1, 3, 6, 10, 15])
    generated = [triangular.evaluate(params, n) for n in range(1, 6)]
    assert generated == [1, 3, 6, 10, 15]

def test_triangular_complexity():
    params = triangular.fit([1, 3, 6, 10, 15])
    assert triangular.complexity(params) >= 1

# ==========================================================
# Pentagonal
# ==========================================================

def test_pentagonal_fit():
    params = pentagonal.fit([1, 5, 12, 22, 35])
    assert params is not None

def test_pentagonal_evaluate():
    params = pentagonal.fit([1, 5, 12, 22, 35])
    generated = [pentagonal.evaluate(params, n) for n in range(1, 6)]
    assert generated == [1, 5, 12, 22, 35]

def test_pentagonal_complexity():
    params = pentagonal.fit([1, 5, 12, 22, 35])
    assert pentagonal.complexity(params) >= 1

# ==========================================================
# Centered Triangular
# ==========================================================

def test_centered_triangular_fit():
    params = centered_triangular.fit([1,4,10,19,31])
    assert params is not None


def test_centered_triangular_evaluate():
    params = centered_triangular.fit([1,4,10,19,31])

    generated = [
        centered_triangular.evaluate(params,n)
        for n in range(1,6)
    ]

    assert generated == [1,4,10,19,31]


def test_centered_triangular_complexity():
    params = centered_triangular.fit([1,4,10,19,31])
    assert centered_triangular.complexity(params) >= 1

# ==========================================================
# Centered Square
# ==========================================================

def test_centered_square_fit():
    params = centered_square.fit([1,5,13,25,41])
    assert params is not None


def test_centered_square_evaluate():
    params = centered_square.fit([1,5,13,25,41])

    generated = [
        centered_square.evaluate(params,n)
        for n in range(1,6)
    ]

    assert generated == [1,5,13,25,41]


def test_centered_square_complexity():
    params = centered_square.fit([1,5,13,25,41])
    assert centered_square.complexity(params) >= 1

# ==========================================================
# Centered Pentagonal
# ==========================================================

def test_centered_pentagonal_fit():
    params = centered_pentagonal.fit([1,6,16,31,51])
    assert params is not None


def test_centered_pentagonal_evaluate():
    params = centered_pentagonal.fit([1,6,16,31,51])

    generated = [
        centered_pentagonal.evaluate(params,n)
        for n in range(1,6)
    ]

    assert generated == [1,6,16,31,51]


def test_centered_pentagonal_complexity():
    params = centered_pentagonal.fit([1,6,16,31,51])
    assert centered_pentagonal.complexity(params) >= 1

# ==========================================================
# Centered Hexagonal
# ==========================================================

def test_centered_hexagonal_fit():
    params = centered_hexagonal.fit([1,7,19,37,61])
    assert params is not None


def test_centered_hexagonal_evaluate():
    params = centered_hexagonal.fit([1,7,19,37,61])

    generated = [
        centered_hexagonal.evaluate(params,n)
        for n in range(1,6)
    ]

    assert generated == [1,7,19,37,61]


def test_centered_hexagonal_complexity():
    params = centered_hexagonal.fit([1,7,19,37,61])
    assert centered_hexagonal.complexity(params) >= 1

# ==========================================================
# Fibonacci
# ==========================================================

def test_fibonacci_fit():
    params = fibonacci.fit([1, 1, 2, 3, 5])
    assert params["Seeds"] == [1, 1]
    assert params["RecurrenceCoefficients"] == [1,1]

def test_fibonacci_evaluate():
    params = fibonacci.fit([1, 1, 2, 3, 5])
    generated = [fibonacci.evaluate(params, n) for n in range(1, 6)]
    assert generated == [1, 1, 2, 3, 5]

def test_fibonacci_complexity():
    params = fibonacci.fit([1, 1, 2, 3, 5])
    assert fibonacci.complexity(params) >= 1

# ==========================================================
# Lucas
# ==========================================================

def test_lucas_fit():
    params = lucas.fit([2, 1, 3, 4, 7])
    assert params["Seeds"] == [2, 1]
    assert params["RecurrenceCoefficients"] == [1,1]

def test_lucas_evaluate():
    params = lucas.fit([2, 1, 3, 4, 7])
    generated = [lucas.evaluate(params, n) for n in range(1, 6)]
    assert generated == [2, 1, 3, 4, 7]

def test_lucas_complexity():
    params = lucas.fit([2, 1, 3, 4, 7])
    assert lucas.complexity(params) >= 1

# ==========================================================
# Pell
# ==========================================================

def test_pell_fit():
    params = pell.fit([0, 1, 2, 5, 12])
    assert params["Seeds"] == [0, 1]
    assert params["RecurrenceCoefficients"] == [2,1]

def test_pell_evaluate():
    params = pell.fit([0, 1, 2, 5, 12])
    generated = [pell.evaluate(params, n) for n in range(1, 6)]
    assert generated == [0, 1, 2, 5, 12]

def test_pell_complexity():
    params = pell.fit([0, 1, 2, 5, 12])
    assert pell.complexity(params) >= 1

# ==========================================================
# Jacobsthal
# ==========================================================

def test_jacobsthal_fit():
    params = jacobsthal.fit([0, 1, 1, 3, 5])
    assert params["Seeds"] == [0, 1]
    assert params["RecurrenceCoefficients"] == [1,2]

def test_jacobsthal_evaluate():
    params = jacobsthal.fit([0, 1, 1, 3, 5])
    generated = [jacobsthal.evaluate(params, n) for n in range(1, 6)]
    assert generated == [0, 1, 1, 3, 5]

def test_jacobsthal_complexity():
    params = jacobsthal.fit([0, 1, 1, 3, 5])
    assert jacobsthal.complexity(params) >= 1

# ==========================================================
# Tribonacci
# ==========================================================

def test_tribonacci_fit():
    params = tribonacci.fit([0,0,1,1,2,4,7])
    assert params["Seeds"] == [0,0,1]


def test_tribonacci_evaluate():
    params = tribonacci.fit([0,0,1,1,2,4,7])
    generated = [
        tribonacci.evaluate(params,n)
        for n in range(1,8)
    ]
    assert generated == [0,0,1,1,2,4,7]


def test_tribonacci_complexity():
    params = tribonacci.fit([0,0,1,1,2,4,7])
    assert tribonacci.complexity(params) >= 1

# ==========================================================
# Tetranacci
# ==========================================================

def test_tetranacci_fit():
    params = tetranacci.fit([0,0,0,1,1,2,4,8])
    assert params["Seeds"] == [0,0,0,1]
    assert params["RecurrenceCoefficients"] == [1,1,1,1]


def test_tetranacci_evaluate():
    params = tetranacci.fit([0,0,0,1,1,2,4,8])

    generated = [
        tetranacci.evaluate(params,n)
        for n in range(1,9)
    ]

    assert generated == [0,0,0,1,1,2,4,8]


def test_tetranacci_complexity():
    params = tetranacci.fit([0,0,0,1,1,2,4,8])
    assert tetranacci.complexity(params) >= 1

# ==========================================================
# Padovan
# ==========================================================

def test_padovan_fit():
    params = padovan.fit([1,1,1,2,2,3,4])
    assert params["Seeds"] == [1,1,1]
    assert params["RecurrenceCoefficients"] == [0,1,1]


def test_padovan_evaluate():
    params = padovan.fit([1,1,1,2,2,3,4])

    generated = [
        padovan.evaluate(params,n)
        for n in range(1,7)
    ]

    assert generated == [1,1,1,2,2,3]


def test_padovan_complexity():
    params = padovan.fit([1,1,1,2,2,3,4])
    assert padovan.complexity(params) >= 1

# ==========================================================
# Perrin
# ==========================================================

def test_perrin_fit():
    params = perrin.fit([3,0,2,3,2,5,5])

    assert params["Seeds"] == [3,0,2]
    assert params["RecurrenceCoefficients"] == [0,1,1]


def test_perrin_evaluate():
    params = perrin.fit([3,0,2,3,2,5,5])

    generated = [
        perrin.evaluate(params,n)
        for n in range(1,8)
    ]

    assert generated == [3,0,2,3,2,5,5]


def test_perrin_complexity():
    params = perrin.fit([3,0,2,3,2,5,5])
    assert perrin.complexity(params) >= 1

# ==========================================================
# Factorial
# ==========================================================

def test_factorial_fit():
    params = factorial.fit([1, 2, 6, 24, 120])
    assert params is not None

def test_factorial_evaluate():
    params = factorial.fit([1, 2, 6, 24, 120])
    generated = [factorial.evaluate(params, n) for n in range(1, 6)]
    assert generated == [1, 2, 6, 24, 120]

def test_factorial_complexity():
    params = factorial.fit([1, 2, 6, 24, 120])
    assert factorial.complexity(params) >= 1