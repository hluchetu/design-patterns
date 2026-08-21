from pipeline.RAG.domain.chat_result import ChatResult
from pipeline.RAG.domain.message import MessageInput
from pipeline.RAG.policy import RequestPolicy
from pipeline.RAG.question_refiner import QuestionRefiner
from pipeline.RAG.retriever import Retriever
from pipeline.RAG.response_generator import ResponseGenerator
from pipeline.RAG.response_validator import ResponseValidator

class ChatService:
    def __init__(
        self,
        policy:RequestPolicy,
        question_refiner:QuestionRefiner,
        retriever:Retriever,
        response_generator:ResponseGenerator,
        response_validator:ResponseValidator,
    )->None:
        self.policy = policy
        self.question_refiner = question_refiner
        self.retriever = retriever
        self.response_generator = response_generator
        self.response_validator = response_validator


    def chat(self,message:MessageInput) ->ChatResult:
        policy_decision = self.policy.check(message)

        if not policy_decision.allowed:
            return ChatResult(
                status = "refused",
                output_text = (
                    policy_decision.reason
                    or "The request was refused"
                ),
            )

        question = self.question_refiner.refine(message)

        documents = self.retriever.retrieve(question)

        if not documents:
            return ChatResult(
                status="unsupported",
                output_text="No document was found"
            )

        model_response = self.response_generator.generate_response(
            question,
            documents
        )

        return self.response_validator.validate(
            model_response,
            documents,

)
