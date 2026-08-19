from __future__ import annotations

from typing import Protocol


class AgentState(Protocol):
    def handle(self, agent: Agent) -> None:
        ...


class Agent:
    def __init__(self) -> None:
        self.state: AgentState = IdleState()

    def change_state(self, state: AgentState) -> None:
        self.state = state

    def run(self) -> None:
        self.state.handle(self)


class IdleState:
    def handle(self, agent: Agent) -> None:
        print("Agent is starting")
        agent.change_state(ThinkingState())


class ThinkingState:
    def handle(self, agent: Agent) -> None:
        print("Agent is thinking")

        needs_tool = True

        if needs_tool:
            agent.change_state(UsingToolState())
        else:
            agent.change_state(FinishedState())


class UsingToolState:
    def handle(self, agent: Agent) -> None:
        print("Agent is using a tool")
        agent.change_state(ThinkingState())


class FinishedState:
    def handle(self, agent: Agent) -> None:
        print("Agent has finished")


def main() -> None:
    agent = Agent()

    agent.run()  # Idle -> Thinking
    agent.run()  # Thinking -> UsingTool
    agent.run()  # UsingTool -> Thinking

    # For demonstration, finish manually.
    agent.change_state(FinishedState())
    agent.run()


if __name__ == "__main__":
    main()
