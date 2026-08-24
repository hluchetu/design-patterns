from dataclasses import dataclass

@dataclass(frozen = True)
class ToolUse:
    name:str
    arguments:dict[str,str]
