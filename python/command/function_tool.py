from collections.abc import Callable
from dataclasses import dataclass

from command.domain.tool_result import ToolResult

ToolFunction = Callable[...,str]

@dataclass(frozen = True)
class FunctionTool:
    name:str
    function:ToolFunction

    def call(
        self,
        arguments:dict[str,str],
            )-> ToolResult:

                output = self.function(**arguments)
                return ToolResult(
                    status = "success",
                    output = output
                )


def tool(function:ToolFunction)->FunctionTool:
        return FunctionTool(
            name = function.__name__,
            function = function
)
