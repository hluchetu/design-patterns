from typing import Protocol


from pipeline.RAG.domain.message import MessageInput
from pipeline.RAG.domain.question import Question


class RewriteQuestion(Protocol):
    def __call__(self,message:str,history:tuple[str,...])->str:
        ...


class QuestionRefiner:
    def __init__(self,rewrite:RewriteQuestion)->None:
        self.rewrite = rewrite

    def refine(self,message:MessageInput)->Question:

        if not message.history:
            return Question(
                original= message.message,
                standalone=message.message
            )

        standalone = self.rewrite(
        message.message,
        message.history
      )

        if not standalone.strip():
            standalone = message.message

        return Question(
            original = message.message,
            standalone = standalone
        )
