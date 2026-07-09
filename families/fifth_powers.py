NAME = "Fifth Powers"
DESCRIPTION = "Fifth powers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        root = round(term ** 0.2)

        if root**5 != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n**5

def formula(_):
    return "a(n)=n⁵"

def complexity(_):
    return 5