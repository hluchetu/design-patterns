from abc import ABC, abstractmethod

class ChatModel(ABC):
        @abstractmethod
        def generate(self,prompt:str)->str:
            pass


class Openai(ChatModel):
    def generate(self,prompt:str)->str:
        return f"OpenAI response to: {prompt}"



class Anthropic(ChatModel):
    def generate(self, prompt: str) -> str:
        return f"Anthropic response to: {prompt}"


class DeepSeek(ChatModel):
    def generate(self, prompt: str) -> str:
        return f"DeepSeek response to: {prompt}"


class AIChat:
    def __init__(self,strategy:ChatModel)->None:
        self.strategy = strategy

    def ask(self,prompt:str)->str:
        return self.strategy.generate(prompt)


chat = AIChat(Anthropic())
print(chat.ask("What is the Strategy pattern?"))
