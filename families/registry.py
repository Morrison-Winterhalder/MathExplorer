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
from families.hierarchy import HIERARCHY


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
    "FAMILY_TYPE",
    "TAGS",
    "TRAITS",
    "RELATED",
}
REQUIRED_FUNCTIONS = {
    "recognize",
    "fit",
    "evaluate",
    "formula",
    "complexity",
    "explain",
}

EXPECTED_METADATA_TYPES = {
    "NAME": str,
    "DESCRIPTION": str,
    "REPRESENTATION": str,
    "CATEGORY": str,
    "SPECIFICITY": int,
    "PARENT": (str, type(None)),
    "FAMILY_TYPE": str,
    "TAGS": tuple,
    "TRAITS": dict,
    "RELATED": list,
}

_PACKAGE = "families"

EXCLUDED_MODULES = {
    "__init__",
    "registry",
    "recurrence",
    "hierarchy"
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
    
    for field, expected_type in EXPECTED_METADATA_TYPES.items():

        value = getattr(module, field)

        if not isinstance(value, expected_type):

            raise PluginError(
                f'{module.NAME}: "{field}" must be {expected_type}'
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

def validate_related(families, family_map):

    for family in families:

        for related in family.RELATED:

            if related == family.NAME:
                raise PluginError(
                    f"{family.NAME} cannot relate to itself."
                )

            if related not in family_map:
                raise PluginError(
                    f"{family.NAME}: unknown related family '{related}'."
                )

        if len(family.RELATED) != len(set(family.RELATED)):
            raise PluginError(
                f"{family.NAME} has duplicate RELATED entries."
            )


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

def validate_hierarchy(families):

    for family in families:

        if family.NAME not in HIERARCHY:
            continue

        expected_parent = HIERARCHY[family.NAME]["parent"]

        if expected_parent is None:
            continue

        if family.PARENT != expected_parent:

            raise PluginError(
                f'Hierarchy mismatch:\n'
                f'Family: {family.NAME}\n'
                f'Expected parent: {expected_parent}\n'
                f'Actual parent: {family.PARENT}'
            )

validate_hierarchy(
    FAMILIES
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

def get_children(name):

    children = []

    for family in FAMILIES:

        if family.PARENT == name:

            children.append(
                family
            )

    return children

def get_depth(family):

    depth = 0

    current = family

    while current.PARENT is not None:

        parent = get_parent(current)

        if parent is None:
            break

        depth += 1
        current = parent

    return depth

def get_siblings(family):

    if family.PARENT is None:
        return []

    return [
        candidate
        for candidate in FAMILIES
        if candidate.PARENT == family.PARENT
        and candidate.NAME != family.NAME
    ]

def get_related(family):

    return [
        FAMILY_MAP[name]
        for name in family.RELATED
    ]