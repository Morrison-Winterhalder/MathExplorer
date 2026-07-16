from analyzers.explanation_engine.reasoning import ReasoningStep


def hierarchy_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "The selected family belongs to a broader "
            "mathematical hierarchy."
        ),
        conclusion=(
            "The classification is consistent with "
            "the recognized structure."
        ),
        category="classification",
        confidence="high",
        priority=9,
        fact=observation.fact,
    )


def family_definition_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "The defining rule of the family directly "
            "describes the observed sequence."
        ),
        conclusion=(
            "The sequence satisfies the defining "
            "properties of the selected family."
        ),
        category="classification",
        confidence="high",
        priority=10,
        fact=observation.fact,
    )


def constant_first_difference_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "Constant first differences indicate "
            "linear behavior."
        ),
        conclusion=(
            "Linear families become strong candidates."
        ),
        category="mathematical",
        confidence="high",
        priority=8,
        fact=observation.fact,
    )


def constant_second_difference_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "The rate of change of the sequence's growth "
            "remains constant."
        ),
        conclusion=(
            "The sequence is consistent with a quadratic family."
        ),
        category="mathematical",
        confidence="high",
        priority=10,
        fact=observation.fact,
    )


def constant_third_difference_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "Constant third differences indicate "
            "cubic behavior."
        ),
        conclusion=(
            "Cubic families become strong candidates."
        ),
        category="mathematical",
        confidence="high",
        priority=10,
        fact=observation.fact,
    )

def first_difference_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "The difference between consecutive terms "
            "remains constant."
        ),
        conclusion=(
            "Linear behavior is supported by the sequence."
        ),
        category="mathematical",
        confidence="medium",
        priority=7,
        fact=observation.fact,
    )


def second_difference_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "Second differences describe the change "
            "in first differences."
        ),
        conclusion=(
            "Quadratic behavior is supported by "
            "the sequence."
        ),
        category="mathematical",
        confidence="high",
        priority=9,
        fact=observation.fact,
    )


def increasing_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "The terms consistently increase."
        ),
        conclusion=(
            "The sequence demonstrates monotonic growth."
        ),
        category="property",
        confidence="medium",
        priority=3,
        fact=observation.fact,
    )


def integer_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "The sequence lies within the integer domain."
        ),
        conclusion=(
            "Integer-based mathematical families remain valid candidates."
        ),
        category="property",
        confidence="medium",
        priority=2,
        fact=observation.fact,
    )

def growth_rule(observation):

    return ReasoningStep(
        observation=observation.text,
        implication=(
            "Observed growth matches the expected "
            "behavior of the recognized family."
        ),
        conclusion=(
            "The classification is supported by "
            "growth analysis."
        ),
        category="verification",
        confidence="high",
        priority=6,
        fact=observation.fact,
    )


RULES = {

    "family_hierarchy":
        hierarchy_rule,

    "family_definition":
        family_definition_rule,

    "constant_first_difference":
        constant_first_difference_rule,

    "constant_second_difference":
        constant_second_difference_rule,

    "constant_third_difference":
        constant_third_difference_rule,

    "increasing_sequence":
        increasing_rule,

    "integer_sequence":
        integer_rule,

    "linear_growth":
        growth_rule,

    "quadratic_growth":
        growth_rule,

    "cubic_growth":
        growth_rule,

    "exponential_growth":
        growth_rule,
}


def get_rule(fact):

    return RULES.get(fact)