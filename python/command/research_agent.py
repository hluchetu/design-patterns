from command.agent_tool import AgentTool


class ResearchAgent:
    def run(self, message: str) -> str:
        return f"Research completed for: {message}"

    def as_tool(
        self,
        *,
        name: str = "research_agent",
    ) -> AgentTool:
        return AgentTool(
            name=name,
            agent=self,
        )
