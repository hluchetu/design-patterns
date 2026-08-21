from dataclasses import dataclass
from typing import Literal


ChatStatus = Literal[
    "completed",
    "refused",
    "unsupported",
]


@dataclass(frozen=True)
class ChatResult:
    status: ChatStatus
    output_text: str
    document_ids: tuple[str, ...] = ()
