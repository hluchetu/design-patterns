from command.domain.tool_result import ToolResult
from command.domain.tool_use import ToolUse
from command.tool import Tool

class ToolRunner:
    def __init__(
        self,
        tools:tuple[Tool,...],
        )-> None:
            self.tools = {
                tool.name: tool for tool in tools
            }
    def run(self,tool_use:ToolUse)->ToolResult:
        tool = self.tools.get(tool_use.name)

        if tool is None:
            return ToolResult(
                status = "error",
                output = f"Tool {tool_use.name !r} is not registered."
            )
        try:
            return tool.call(tool_use.arguments)
        except Exception as error:
            return ToolResult(
                status = "error",
                output = str(error)
            )
