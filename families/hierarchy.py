HIERARCHY = {

    "Sequence Families": {
        "parent": None,
        "children": [
            "Explicit",
            "Recursive",
        ],
    },

    "Explicit": {
        "parent": None,
        "children": [
            "Basic",
            "Figurate",
            "Special",
        ],
    },

    "Basic": {
        "parent": "Explicit",
        "children": [
            "Constant Numbers",
            "Arithmetic Numbers",
            "Geometric Numbers",
            "Polynomial Numbers",
        ],
    },

    "Figurate": {
        "parent": "Explicit",
        "children": [
            "Polygonal",
            "Centered Polygonal",
        ],
    },

    "Polygonal": {
        "parent": "Figurate",
        "children": [
            "Triangular Numbers",
            "Square Numbers",
            "Pentagonal Numbers",
            "Hexagonal Numbers",
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

    "Special": {
        "parent": "Explicit",
        "children": [
            "Factorial Numbers",
        ],
    },

    "Recursive": {
        "parent": None,
        "children": [
            "Linear Recurrence",
        ],
    },

    "Linear Recurrence": {
        "parent": "Recursive",
        "children": [
            "Fibonacci Numbers",
            "Lucas Numbers",
            "Pell Numbers",
            "Jacobsthal Numbers",
            "Tribonacci Numbers",
            "Tetranacci Numbers",
            "Padovan Numbers",
            "Perrin Numbers",
        ],
    },
}