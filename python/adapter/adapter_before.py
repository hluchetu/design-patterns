from dataclasses import dataclass
from typing import Any


AnthropicMessage = dict[str, str]
AnthropicResponse = dict[str, list[dict[str, Any]]]


@dataclass
class Message:
    role: str
    content: str


class FakeAnthropicClient:
    def create(
        self,
        *,
        system: str | None,
        messages: list[AnthropicMessage],
    ) -> AnthropicResponse:
        print("Anthropic request:")
        print("system:", system)
        print("messages:", messages)

        return {
            "content": [
                {
                    "type": "text",
                    "text": "Hello from Anthropic",
                }
            ]
        }


class AnthropicModel:
    def __init__(self) -> None:
        self.client = FakeAnthropicClient()

    def invoke(self, messages: list[Message]) -> Message:
        system = next(
            (
                message.content
                for message in messages
                if message.role == "system"
            ),
            None,
        )

        anthropic_messages: list[AnthropicMessage] = [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
            if message.role != "system"
        ]

        response = self.client.create(
            system=system,
            messages=anthropic_messages,
        )

        text = " ".join(
            block["text"]
            for block in response["content"]
            if block["type"] == "text"
        )

        return Message(
            role="assistant",
            content=text,
        )


def main() -> None:
    messages = [
        Message(
            role="system",
            content="You are a helpful assistant.",
        ),
        Message(
            role="user",
            content="What is the Adapter pattern?",
        ),
    ]

    model = AnthropicModel()
    response = model.invoke(messages)

    print(response)


if __name__ == "__main__":
    main()
