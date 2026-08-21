from dataclasses import dataclass

@dataclass(frozen = True)
class PolicyDecision:
    allowed:bool
    reason:str | None = None
