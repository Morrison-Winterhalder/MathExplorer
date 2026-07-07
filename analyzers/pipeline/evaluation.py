def evaluate_polynomial(coefficients,n):
    value = 0
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        value += (coefficient)*((n)**power)
    return value

def geometric_sum(parameters,n):
    value = 0
    coefficient = parameters[0]
    rate = parameters[1]
    for i in range(n):
        value += (coefficient)*(rate)**(i)
    return value

def evaluate_geometric(parameters,n):
    first_term = parameters["First Term"]
    ratio = parameters["Ratio"]
    return first_term * (ratio ** (n - 1))

def evaluate_triangular(_,n):
    return n * (n + 1) // 2

def evaluate_pentagonal(_, n):
    return n * (3 * n - 1) // 2

def evaluate_constant(constant, n):
    return constant

def evaluate_fibonacci(parameters, n):
    a = parameters["First"]
    b = parameters["Second"]

    if n == 1:
        return a
    if n == 2:
        return b

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b

EVALUATION_HANDLERS = {
    "Constant": evaluate_constant,
    "Arithmetic": evaluate_polynomial,
    "Polynomial": evaluate_polynomial,
    "Geometric": evaluate_geometric,
    "Triangular": evaluate_triangular,
    "Pentagonal": evaluate_pentagonal,
    "Fibonacci": evaluate_fibonacci
}