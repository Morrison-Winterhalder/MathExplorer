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

FAMILY_MAP = {
    family.NAME: family
    for family in FAMILIES
}

def get_family(name):
    return FAMILY_MAP.get(name)