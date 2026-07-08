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
    factorial
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
# Fibonacci
# ==========================================================

def test_fibonacci_fit():
    params = fibonacci.fit([1, 1, 2, 3, 5])
    assert params["Seeds"] == [1, 1]

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

def test_jacobsthal_evaluate():
    params = jacobsthal.fit([0, 1, 1, 3, 5])
    generated = [jacobsthal.evaluate(params, n) for n in range(1, 6)]
    assert generated == [0, 1, 1, 3, 5]

def test_jacobsthal_complexity():
    params = jacobsthal.fit([0, 1, 1, 3, 5])
    assert jacobsthal.complexity(params) >= 1

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