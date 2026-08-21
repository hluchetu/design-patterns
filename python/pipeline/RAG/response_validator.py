from pipeline.RAG.domain.chat_result import ChatResult
from pipeline.RAG.domain.document import Document
from pipeline.RAG.domain.model_response import ModelResponse


class ResponseValidator:
    def validate(
        self,
        response: ModelResponse,
        documents: tuple[Document, ...],
    ) -> ChatResult:
        if not response.output_text.strip():
            return ChatResult(
                status="unsupported",
                output_text="The model returned an empty response.",
            )

        if not response.document_ids:
            return ChatResult(
                status="unsupported",
                output_text="The model did not reference any documents.",
            )

        available_document_ids = {
            document.source
            for document in documents
        }

        unknown_document_ids = tuple(
            document_id
            for document_id in response.document_ids
            if document_id not in available_document_ids
        )

        if unknown_document_ids:
            return ChatResult(
                status="unsupported",
                output_text="The model referenced unknown documents.",
            )

        return ChatResult(
            status="completed",
            output_text=response.output_text,
            document_ids=response.document_ids,
        )
