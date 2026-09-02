class Conversation:
    def __init__(self, strategy: str) -> None:
        self.strategy: str = strategy
        self.messages: list[str] = []

    def add(self, message: str) -> None:
        self.messages.append(message)

    def prepare(self) -> list[str]:
        if self.strategy == "full":
            return self.messages

        elif self.strategy == "sliding_window":
            return self.messages[-3:]

        elif self.strategy == "summary":
            old_messages = self.messages[:-3]
            recent_messages = self.messages[-3:]

            summary = "Summary: " + " | ".join(old_messages)
            return [summary, *recent_messages]

        raise ValueError(f"Unknown strategy: {self.strategy}")


conversation = Conversation("sliding_window")

conversation.add("User: My name is Amina")
conversation.add("Assistant: Nice to meet you")
conversation.add("User: I prefer Python")
conversation.add("Assistant: I'll use Python")
conversation.add("User: Explain the Strategy pattern")

for message in conversation.prepare():
    print(message)
