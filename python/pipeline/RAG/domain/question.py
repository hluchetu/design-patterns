from dataclasses import dataclass

@dataclass(frozen = True)
class Question:
    original:str
    standalone:str
