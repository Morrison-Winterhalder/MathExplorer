CATEGORY_PRIORITY = {

    # Core mathematical evidence
    "mathematical": 1,

    # Growth / verification
    "verification": 2,

    # Classification
    "classification": 3,

    # General properties
    "property": 4,

}

FACT_PRIORITY = {
    "family_hierarchy": 1,
    "family_definition": 2,
}

def order_reasoning_chain(chain):

    return sorted(
        chain,
        key=lambda step: (
            CATEGORY_PRIORITY.get(step.category, 99),
            FACT_PRIORITY.get(getattr(step, "fact", ""), 99),
        )
    )