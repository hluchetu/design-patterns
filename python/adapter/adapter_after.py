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


class AnthropicAdapter:
    def get_system_message(
        self,
        messages: list[Message],
    ) -> str | None:
        return next(
            (
                message.content
                for message in messages
                if message.role == "system"
            ),
            None,
        )

    def serialize_messages(
        self,
        messages: list[Message],
    ) -> list[AnthropicMessage]:
        return [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
            if message.role != "system"
        ]

    def deserialize_response(
        self,
        response: AnthropicResponse,
    ) -> Message:
        text = " ".join(
            block["text"]
            for block in response["content"]
            if block["type"] == "text"
        )

        return Message(
            role="assistant",
            content=text,
        )


class AnthropicModel:
    def __init__(self) -> None:
        self.client = FakeAnthropicClient()
        self.adapter = AnthropicAdapter()

    def invoke(self, messages: list[Message]) -> Message:
        system = self.adapter.get_system_message(messages)

        anthropic_messages = self.adapter.serialize_messages(
            messages
        )

        response = self.client.create(
            system=system,
            messages=anthropic_messages,
        )

        return self.adapter.deserialize_response(response)


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
