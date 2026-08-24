from dataclasses import dataclass
from typing import Literal

ToolStatus = Literal[
    "success",
    "error"
]

@dataclass(frozen = True)
class ToolResult:
    status:ToolStatus
    output:str
