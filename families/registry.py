from . import constant
from . import arithmetic
from . import geometric
from . import polynomial
from . import triangular
from . import pentagonal
from . import fibonacci
from . import lucas
from . import pell
from . import jacobsthal
from . import factorial
from families.constant import evaluate_constant
from families.arithmetic import evaluate_arithmetic
from families.polynomial import evaluate_polynomial
from families.geometric import evaluate_geometric
from families.triangular import evaluate_triangular
from families.pentagonal import evaluate_pentagonal
from families.recurrence import evaluate_linear_recurrence
from families.factorial import evaluate_factorial

FAMILIES = [
    constant,
    arithmetic,
    polynomial,
    geometric,
    triangular,
    pentagonal,
    fibonacci,
    lucas,
    pell,
    jacobsthal,
    factorial
]


EVALUATION_HANDLERS = {
    "Constant": evaluate_constant,
    "Arithmetic": evaluate_arithmetic,
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

def get_family(name):
    for family in FAMILIES:
        if family.NAME == name:
            return family
    return None