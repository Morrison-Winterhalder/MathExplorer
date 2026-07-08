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