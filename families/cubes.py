NAME = "Cubes"
DESCRIPTION = "Perfect cube numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = round(term ** (1/3))

        if root**3 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**3

def formula(_):
    return "a(n)=n³"

def complexity(_):
    return 3