"""
MathExplorer Family Plugin Registry

Required Metadata:

    NAME
    DESCRIPTION
    REPRESENTATION
    CATEGORY
    SPECIFICITY
    PARENT

Required Interface:

    recognize()
    fit()
    evaluate()
    formula()
    complexity()
    explain()
"""

import importlib
import pkgutil
from pathlib import Path


class PluginError(Exception):
    """Raised when a family plugin does not implement the required interface."""
    pass


REQUIRED_METADATA = {
    "NAME",
    "DESCRIPTION",
    "REPRESENTATION",
    "CATEGORY",
    "SPECIFICITY",
    "PARENT",
}

REQUIRED_FUNCTIONS = {
    "recognize",
    "fit",
    "evaluate",
    "formula",
    "complexity",
    "explain",
}

_PACKAGE = "families"

EXCLUDED_MODULES = {
    "__init__",
    "registry",
    "recurrence",
}


def validate_metadata(module):

    missing = [
        attribute
        for attribute in REQUIRED_METADATA
        if not hasattr(module, attribute)
    ]

    if missing:

        missing.sort()

        raise PluginError(
            f'Family "{module.__name__}" is missing metadata:\n'
            + "\n".join(
                f"    {item}"
                for item in missing
            )
        )


def validate_interface(module):

    missing = [
        function
        for function in REQUIRED_FUNCTIONS
        if not hasattr(module, function)
    ]

    if missing:

        missing.sort()

        raise PluginError(
            f'Family "{module.__name__}" is missing functions:\n'
            + "\n".join(
                f"    {item}"
                for item in missing
            )
        )


def validate_family(module):

    validate_metadata(module)
    validate_interface(module)


def discover_families():

    families = []

    for module_info in pkgutil.iter_modules(
        [str(Path(__file__).parent)]
    ):

        module_name = module_info.name

        if module_name in EXCLUDED_MODULES:
            continue

        module = importlib.import_module(
            f"{_PACKAGE}.{module_name}"
        )

        validate_family(module)

        families.append(module)

    families.sort(
        key=lambda family: family.NAME
    )

    return families


def create_family_map(families):

    names = [
        family.NAME
        for family in families
    ]

    duplicates = {
        name
        for name in names
        if names.count(name) > 1
    }

    if duplicates:

        raise PluginError(
            f"Duplicate family names: {duplicates}"
        )

    return {
        family.NAME: family
        for family in families
    }


def validate_parents(families, family_map):

    for family in families:

        if family.PARENT is None:
            continue

        if family.PARENT not in family_map:

            raise PluginError(
                f'Family "{family.NAME}" has '
                f'invalid parent "{family.PARENT}"'
            )


FAMILIES = discover_families()

FAMILY_MAP = create_family_map(FAMILIES)

validate_parents(
    FAMILIES,
    FAMILY_MAP
)


def get_family(name, required=False):

    family = FAMILY_MAP.get(name)

    if family is None and required:

        raise PluginError(
            f"Unknown family: {name}"
        )

    return family


def get_metadata(family):

    return {
        key: value
        for key, value in vars(family).items()
        if key.isupper()
    }


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

    lines = [
        family.NAME
    ]

    indent = ""

    for parent in lineage:

        lines.append(
            f"{indent}└── {parent.NAME}"
        )

        indent += "    "

    return "\n".join(lines)