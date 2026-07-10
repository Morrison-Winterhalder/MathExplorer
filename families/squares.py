from math import isqrt

NAME = "Squares"
DESCRIPTION = "Perfect square numbers."
REPRESENTATION = "Explicit"
CATEGORY = "Polynomial"
SPECIFICITY = 40
PARENT = "Polynomial"

def recognize(sequence):
    if len(sequence) == 0:
        return None

    for term in sequence:
        if term < 0:
            return False

        root = isqrt(term)

        if root * root != term:
            return False

    return True

def fit(sequence):
    if recognize(sequence) is not True:
        return None
    return {}

def evaluate(_, n):
    return n*n

def formula(_):
    return "a(n) = n²"

def complexity(_):
    return 2

def explain(_):

    return [
        "Every term is a perfect square.",
        "The sequence matches the formula n² exactly."
    ]