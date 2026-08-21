from dataclasses import dataclass


@dataclass(frozen = True)
class MessageInput:
    message:str
    history:tuple[str,...]
