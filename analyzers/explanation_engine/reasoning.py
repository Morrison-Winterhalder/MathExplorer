from dataclasses import dataclass


@dataclass
class ReasoningStep:

    observation: str

    implication: str

    conclusion: str

    category: str

    confidence: str = "high"

    fact: str = ""

    priority: int = 0