from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BeforeModelCall:
    messages: list[str]
    step: int


@dataclass(frozen=True, slots=True)
class AfterModelCall:
    response: str
    step: int
    duration_ms: float


@dataclass(frozen=True, slots=True)
class BeforeToolCall:
    tool_name: str
    arguments: dict[str, str]
    step: int


@dataclass(frozen=True, slots=True)
class AfterToolCall:
    tool_name: str
    result: str
    step: int
    duration_ms: float
