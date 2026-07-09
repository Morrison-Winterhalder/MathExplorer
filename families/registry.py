"""
MathExplorer Family Plugin

Required Metadata:

    NAME
    DESCRIPTION
    REPRESENTATION

Required interface:
    recognize()
    fit()
    evaluate()
    formula()
    complexity()
"""

class PluginError(Exception):
    """Raised when a family plugin does not implement the required interface."""

import importlib
import pkgutil
from pathlib import Path

REQUIRED_ATTRIBUTES = {
    "NAME",
    "DESCRIPTION",
    "REPRESENTATION",
    "CATEGORY",
    "SPECIFICITY",
    "PARENT",
    "recognize",
    "fit",
    "evaluate",
    "formula",
    "complexity",
}

_PACKAGE = "families"

EXCLUDED_MODULES = {
    "__init__",
    "registry",
    "recurrence",
}

def validate_family(module):

    missing = [
        attribute
        for attribute in REQUIRED_ATTRIBUTES
        if not hasattr(module, attribute)
    ]

    if missing:

        missing.sort()

        missing_text = "\n    ".join(missing)

        raise PluginError(
            f'Family "{module.__name__}" is missing:\n'
            f"    {missing_text}"
        )

FAMILIES = []

for module_info in pkgutil.iter_modules([str(Path(__file__).parent)]):

    module_name = module_info.name

    if module_name in EXCLUDED_MODULES:
        continue

    module = importlib.import_module(
        f"{_PACKAGE}.{module_name}"
    )

    validate_family(module)

    FAMILIES.append(module)


FAMILIES.sort(key=lambda family: family.NAME)

FAMILY_MAP = {
    family.NAME: family
    for family in FAMILIES
}

def get_family(name):
    return FAMILY_MAP.get(name)

def get_parent(family):

    if family.PARENT is None:
        return None

    return FAMILY_MAP.get(family.PARENT)



def get_lineage(family):

    lineage = []

    current = family

    while current.PARENT is not None:

        parent = get_parent(current)

        if parent is None:
            break

        lineage.append(parent)

        current = parent

    return lineage

def build_family_tree(family):

    if family is None:
        return ""

    lineage = get_lineage(family)

    lines = [family.NAME]

    indent = ""

    for parent in lineage:
        lines.append(f"{indent}└── {parent.NAME}")
        indent += "    "

    return "\n".join(lines)