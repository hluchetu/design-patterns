from collections.abc import Callable


ModelStrategy = Callable[[str], str]


def call_openai(prompt: str) -> str:
    return f"OpenAI response to: {prompt}"


def call_anthropic(prompt: str) -> str:
    return f"Anthropic response to: {prompt}"


def call_deepseek(prompt: str) -> str:
    return f"DeepSeek response to: {prompt}"


class AIChat:
    def __init__(self, strategy: ModelStrategy):
        self.strategy = strategy

    def ask(self, prompt: str) -> str:
        return self.strategy(prompt)


chat = AIChat(call_anthropic)
print(chat.ask("What is the Strategy pattern?"))
