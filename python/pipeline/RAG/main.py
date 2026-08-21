from pipeline.RAG.chat_service import ChatService
from pipeline.RAG.domain.document import Document
from pipeline.RAG.domain.message import MessageInput
from pipeline.RAG.domain.model_response import ModelResponse
from pipeline.RAG.domain.question import Question
from pipeline.RAG.policy import RequestPolicy
from pipeline.RAG.question_refiner import QuestionRefiner
from pipeline.RAG.response_generator import ResponseGenerator
from pipeline.RAG.response_validator import ResponseValidator
from pipeline.RAG.retriever import Retriever


DOCUMENTS = (
    Document(
        source="article-43",
        text=(
            "Every person has the right to accessible "
            "and adequate housing."
        ),
    ),
    Document(
        source="article-47",
        text=(
            "Every person has the right to administrative "
            "action that is lawful and reasonable."
        ),
    ),
)


def rewrite_question(
    message: str,
    history: tuple[str, ...],
) -> str:
    context = " ".join(history)

    return f"{context} {message}"



def search_documents(
        question: Question,
    ) -> tuple[Document, ...]:
        query_words = {
            word.strip(".,?!()").lower()
            for word in question.standalone.split()
            if len(word.strip(".,?!()")) > 4
        }

        return tuple(
            document
            for document in DOCUMENTS
            if any(
                word in document.text.lower()
                for word in query_words
            )
        )

def generate_response(
    question: Question,
    documents: tuple[Document, ...],
) -> ModelResponse:
    context = " ".join(
        document.text
        for document in documents
    )

    return ModelResponse(
        output_text=(
            f"Question: {question.original}\n"
            f"Response: {context}"
        ),
        document_ids=tuple(
            document.source
            for document in documents
        ),
    )

def build_chat_service() -> ChatService:
    return ChatService(
        policy=RequestPolicy(),
        question_refiner=QuestionRefiner(
            rewrite=rewrite_question,
        ),
        retriever=Retriever(
            search=search_documents,
        ),
        response_generator=ResponseGenerator(
            generate=generate_response,
        ),
        response_validator=ResponseValidator(),
    )

def main() -> None:
    service = build_chat_service()

    message = MessageInput(
        message="What right do people have to housing?",
        history=(),
    )

    result = service.chat(message)

    print(f"Status: {result.status}")
    print(f"Output: {result.output_text}")
    print(f"Documents: {result.document_ids}")


if __name__ == "__main__":
    main()
