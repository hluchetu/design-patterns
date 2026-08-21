from typing import Protocol

from pipeline.RAG.domain.document import Document
from pipeline.RAG.domain.model_response import ModelResponse
from pipeline.RAG.domain.question import Question


class GenerateResponse(Protocol):
    def __call__(
        self,
        question: Question,
        documents: tuple[Document, ...],
    ) -> ModelResponse:
        ...


class ResponseGenerator:
    def __init__(self, generate: GenerateResponse) -> None:
        self.generate = generate

    def generate_response(
        self,
        question: Question,
        documents: tuple[Document, ...],
    ) -> ModelResponse:
        return self.generate(
            question,
            documents,
        )
