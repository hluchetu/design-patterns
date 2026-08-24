from command.domain.tool_use import ToolUse
from command.function_tool import tool
from command.research_agent import ResearchAgent
from command.tool_runner import ToolRunner


@tool
def search(query: str) -> str:
    return f"Search results for: {query}"


def main() -> None:
    research_agent = ResearchAgent()

    research_tool = research_agent.as_tool()

    runner = ToolRunner(
        tools=(
            search,
            research_tool,
        )
    )

    search_request = ToolUse(
        name="search",
        arguments={
            "query": "Article 43",
        },
    )

    search_result = runner.run(search_request)

    print(search_result)

    research_request = ToolUse(
        name="research_agent",
        arguments={
            "message": "Research the right to housing",
        },
    )

    research_result = runner.run(research_request)

    print(research_result)


if __name__ == "__main__":
    main()
