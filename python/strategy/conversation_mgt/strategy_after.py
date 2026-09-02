from abc import ABC, abstractmethod
from typing import override


class ConversationStrategy(ABC):
    @abstractmethod
    def prepare(self, messages: list[str]) -> list[str]:
        pass


class FullHistory(ConversationStrategy):
    @override
    def prepare(self, messages: list[str]) -> list[str]:
        return messages


class SlidingWindow(ConversationStrategy):
    def __init__(self, max_messages: int = 3) -> None:
        self.max_messages: int = max_messages

    @override
    def prepare(self, messages: list[str]) -> list[str]:
        return messages[-self.max_messages :]


class SummarizeOldMessages(ConversationStrategy):
    def __init__(self, keep_recent: int = 3) -> None:
        self.keep_recent: int = keep_recent

    @override
    def prepare(self, messages: list[str]) -> list[str]:
        old_messages = messages[: -self.keep_recent]
        recent_messages = messages[-self.keep_recent :]

        summary = "Summary: " + " | ".join(old_messages)
        return [summary, *recent_messages]


class Conversation:
    def __init__(self, strategy: ConversationStrategy) -> None:
        self.strategy: ConversationStrategy = strategy
        self.messages: list[str] = []

    def add(self, message: str) -> None:
        self.messages.append(message)

    def prepare(self) -> list[str]:
        return self.strategy.prepare(self.messages)


conversation = Conversation(SlidingWindow(max_messages=3))

conversation.add("User: My name is Amina")
conversation.add("Assistant: Nice to meet you")
conversation.add("User: I prefer Python")
conversation.add("Assistant: I'll use Python")
conversation.add("User: Explain the Strategy pattern")

for message in conversation.prepare():
    print(message)
