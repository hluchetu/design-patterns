from dataclasses import dataclass
from typing import Protocol

from command.domain.tool_result import ToolResult

class RunnableAgent(Protocol):
    def run(self,message:str)->str:
        ...

@dataclass(frozen = True)
class AgentTool:
    name:str
    agent:RunnableAgent

    def call(
        self,
        arguments:dict[str,str],
    )->ToolResult:
        message = arguments["message"]

        output = self.agent.run(message)

        return ToolResult(
            status = "success",
            output = output
        )
