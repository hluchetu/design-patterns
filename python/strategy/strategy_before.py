class AIChat:
    def __init__(self, provider: str = "openai"):
        self.provider = provider

    def ask(self, prompt: str) -> str:
        if self.provider == "openai":
            return self.call_openai(prompt)

        elif self.provider == "anthropic":
            return self.call_anthropic(prompt)

        elif self.provider == "deepseek":
            return self.call_deepseek(prompt)

        raise ValueError(f"Unknown provider: {self.provider}")

    def call_openai(self, prompt: str) -> str:
        return f"OpenAI response to: {prompt}"

    def call_anthropic(self, prompt: str) -> str:
        return f"Anthropic response to: {prompt}"

    def call_deepseek(self, prompt: str) -> str:
        return f"DeepSeek response to: {prompt}"


chat = AIChat("anthropic")
print(chat.ask("What is the Strategy pattern?"))
