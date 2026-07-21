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
from families.core.hierarchy import HIERARCHY


class PluginError(Exception):
    """Raised when a family plugin does not implement the required interface."""
    pass

class HierarchyNode:

    def __init__(
        self,
        name,
        parent,
        children
    ):

        self.NAME = name
        self.PARENT = parent
        self.CHILDREN = children

    def __repr__(self):

        return (
            f"HierarchyNode("
            f"{self.NAME!r}"
            f")"
        )
    
HIERARCHY_NODES = {

    name: HierarchyNode(
        name=name,
        parent=data["parent"],
        children=data["children"],
    )

    for name, data in HIERARCHY.items()
}

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

OPTIONAL_METADATA = {
    "AUTHOR": "MathExplorer",
    "VERSION": "1.0.0",
    "SOURCE": "Core",
    "PLUGIN": False,
    "ID": None,
}

CORE_PACKAGE = "families.core"
PLUGIN_PACKAGE = "families.plugins"

CORE_DIRECTORY = Path(__file__).parent / "core"
PLUGIN_DIRECTORY = Path(__file__).parent / "plugins"

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
        
    for field, default in OPTIONAL_METADATA.items():

        if not hasattr(module, field):

            setattr(module, field, default)

    # Default ID is derived from NAME if omitted
    if module.ID is None:

        module.ID = (
            module.NAME
            .lower()
            .replace(" ", "_")
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


def discover_package(directory, package):

    families = []

    for module_info in pkgutil.iter_modules([str(directory)]):

        module_name = module_info.name

        if module_name in EXCLUDED_MODULES:
            continue

        module = importlib.import_module(
            f"{package}.{module_name}"
        )

        validate_family(module)

        families.append(module)

    return families

def discover_core():

    return discover_package(
        CORE_DIRECTORY,
        CORE_PACKAGE,
    )

def discover_plugins():

    if not PLUGIN_DIRECTORY.exists():
        return []

    return discover_package(
        PLUGIN_DIRECTORY,
        PLUGIN_PACKAGE,
    )

def discover_families():

    families = (
        discover_core()
        + discover_plugins()
    )

    families.sort(
        key=lambda family: family.NAME
    )

    return families

CORE_NAMES = {
    family.NAME
    for family in discover_core()
}

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

def validate_ids(families):

    ids = [
        family.ID
        for family in families
    ]

    duplicates = {
        value
        for value in ids
        if ids.count(value) > 1
    }

    if duplicates:

        raise PluginError(
            f"Duplicate family IDs: {duplicates}"
        )

def validate_parents(families, family_map):

    for family in families:

        if family.PARENT is None:
            continue

        if (
            family.PARENT not in family_map
            and family.PARENT not in HIERARCHY
        ):
            raise PluginError(
                f'Family "{family.NAME}" has '
                f'invalid parent "{family.PARENT}"'
            )


FAMILIES = discover_families()

FAMILY_MAP = create_family_map(FAMILIES)

validate_ids(FAMILIES)

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


def validate_plugins(families):

    for family in families:

        if not family.PLUGIN:
            continue

        if family.NAME in CORE_NAMES:

            raise PluginError(
                f'Plugin "{family.NAME}" attempts to override a built-in family.'
            )
        
validate_plugins(FAMILIES)  

def print_registry_summary():

    core = sum(
        not family.PLUGIN
        for family in FAMILIES
    )

    plugins = sum(
        family.PLUGIN
        for family in FAMILIES
    )

    print()

    print("=" * 40)
    print("MathExplorer v3.0")
    print("=" * 40)

    print(f"Core Families : {core}")
    print(f"Plugins       : {plugins}")
    print(f"Total Loaded  : {len(FAMILIES)}")

    print("Registry initialized successfully.")

    print()

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

    if family.PARENT == "Sequence Families":
        return None

    if family.PARENT in FAMILY_MAP:
        return FAMILY_MAP[family.PARENT]

    return HIERARCHY_NODES.get(family.PARENT)

def get_lineage(family):

    lineage = []

    current = family

    while current.PARENT is not None:

        if current.PARENT == "Sequence Families":
            break

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

    representation = getattr(
        family,
        "REPRESENTATION",
        None
    )

    if (
        representation
        and representation not in [
            parent.NAME
            for parent in lineage
        ]
    ):

        lines.append(
            f"{indent}└── {representation}"
        )

        indent += "    "

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

    # --------------------------------------------------
    # Resolve the family name
    # --------------------------------------------------

    if hasattr(
        family,
        "NAME"
    ):

        name = family.NAME

        family_module = family

    else:

        name = family

        family_module = None


    # --------------------------------------------------
    # Direct hierarchy node
    # --------------------------------------------------

    if name in HIERARCHY:

        depth = 0

        current = name

        while (
            HIERARCHY[current]["parent"]
            is not None
        ):

            current = (
                HIERARCHY[current]["parent"]
            )

            depth += 1

        return depth


    # --------------------------------------------------
    # Loaded family not directly represented as a
    # hierarchy node
    # --------------------------------------------------

    if family_module is None:

        family_module = get_family(
            name
        )


    parent = getattr(
        family_module,
        "PARENT",
        None
    )


    # A loaded root family has depth zero.
    if parent is None:

        return 0


    # The family itself is one level below its
    # declared hierarchy parent.
    depth = 1

    current = parent


    while current in HIERARCHY:

        parent = (
            HIERARCHY[current]["parent"]
        )


        if parent is None:

            break


        current = parent

        depth += 1


    return depth

def get_siblings(family):

    if family.PARENT is None or family.PARENT == "Sequence Families":
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

print_registry_summary()