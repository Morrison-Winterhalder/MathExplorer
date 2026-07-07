from math import factorial

# Explicit Formulas
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

def evaluate_factorial(parameters, n):
    return factorial(n)

# Recurrence Relations
def evaluate_linear_recurrence(parameters, n):

    seeds = parameters["Seeds"]
    coefficients = parameters["RecurrenceCoefficients"]

    if n <= len(seeds):
        return seeds[n-1]

    terms = seeds.copy()

    while len(terms) < n:

        next_term = 0

        # Combine the previous k terms
        for coefficient, previous in zip(
            coefficients,
            reversed(terms[-len(coefficients):])
        ):
            next_term += coefficient * previous

        terms.append(next_term)

    return terms[-1]


# Registry
EVALUATION_HANDLERS = {
    "Constant": evaluate_constant,
    "Arithmetic": evaluate_polynomial,
    "Polynomial": evaluate_polynomial,
    "Geometric": evaluate_geometric,
    "Triangular": evaluate_triangular,
    "Pentagonal": evaluate_pentagonal,
    "Fibonacci": evaluate_linear_recurrence,
    "Lucas": evaluate_linear_recurrence,
    "Pell": evaluate_linear_recurrence,
    "Jacobsthal": evaluate_linear_recurrence,
    "Factorial": evaluate_factorial
}