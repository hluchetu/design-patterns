from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    source: str
    text: str
