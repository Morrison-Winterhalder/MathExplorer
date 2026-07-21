HIERARCHY = {

    "Sequence Families": {
        "parent": None,
        "children": [
            "Explicit",
            "Recursive",
            "Combinatorial",
        ],
    },

    "Explicit": {
        "parent": "Sequence Families",
        "children": [
            "Basic",
            "Figurate",
            "Special",
        ],
    },

    "Basic": {
        "parent": "Explicit",
        "children": [
            "Constant",
            "Arithmetic",
            "Geometric",
            "Polynomial",
        ],
    },

    "Figurate": {
        "parent": "Explicit",
        "children": [
            "Polygonal",
            "Centered Polygonal",
        ],
    },

    "Special": {
        "parent": "Explicit",
        "children": [
            "Factorials",
        ],
    },

    "Recursive": {
        "parent": "Sequence Families",
        "children": [
            "Linear Recurrence",
            "Collatz Stopping Times",
            "Happy Numbers",
            "Look-and-Say Numbers",
            "Motzkin Numbers",
            "Van Eck Numbers"
        ],
    },

    "Linear Recurrence": {
        "parent": "Recursive",
        "children": [
            "Fibonacci",
            "Lucas Numbers",
            "Pell Numbers",
            "Jacobsthal Numbers",
            "Tribonacci Numbers",
            "Tetranacci Numbers",
            "Padovan Numbers",
            "Perrin Numbers",
        ],
    },

    "Combinatorial": {
        "parent": "Sequence Families",
        "children": [
            "Catalan Numbers",
            "Bell Numbers",
            "Derangement Numbers",
            "Partition Numbers",
            "Schröder Numbers",
        ],
    },

    "Polynomial": {
        "parent": "Basic",
        "children": [
            "Cubes",
            "Squares",
            "Fifth Powers",
            "Fourth Powers",
            "Pronic Numbers",
        ],
    },

    "Polygonal": {
        "parent": "Figurate",
        "children": [
            "Triangular Numbers",
            "Pentagonal Numbers",
            "Hexagonal Numbers",
            "Heptagonal Numbers",
            "Octagonal Numbers",
            "Nonagonal Numbers",
            "Decagonal Numbers",
        ],
    },

    "Centered Polygonal": {
        "parent": "Figurate",
        "children": [
            "Centered Triangular Numbers",
            "Centered Square Numbers",
            "Centered Pentagonal Numbers",
            "Centered Hexagonal Numbers",
        ],
    },
}