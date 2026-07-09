NAME = "Fourth Powers"
DESCRIPTION = "Fourth powers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = round(term ** 0.25)

        if root**4 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**4

def formula(_):
    return "a(n)=n⁴"

def complexity(_):
    return 4