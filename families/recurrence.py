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