def evaluate_polynomial(coefficients,n):
    value = 0
    for i, coefficient in enumerate(coefficients):
        power = len(coefficients) - 1 - i
        value += (coefficient)*((n)**power)
    return value

def geometric_sum(coefficients,n):
    value = 0
    coefficient = coefficients[0]
    rate = coefficients[1]
    for i in range(n):
        value += (coefficient)*(rate)**(i)
    return value

def evaluate_geometric(parameters,n):
    first_term = parameters["First Term"]
    ratio = parameters["Ratio"]
    return first_term * (ratio ** (n - 1))