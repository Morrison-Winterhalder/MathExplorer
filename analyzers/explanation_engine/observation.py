from dataclasses import dataclass


@dataclass
class Observation:

    text: str

    category: str

    importance: int = 5

    type: str = "reason"

    confidence: str = "observed"
    
    fact: str | None = None