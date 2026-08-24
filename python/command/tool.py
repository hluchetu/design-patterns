from typing import Protocol

from command.domain.tool_result import ToolResult


class Tool(Protocol):
    @property
    def name(self) -> str:
        ...

    def call(
        self,
        arguments: dict[str, str],
    ) -> ToolResult:
        ...
