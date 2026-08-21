from pipeline.RAG.domain.message import MessageInput
from pipeline.RAG.domain.policy import PolicyDecision

class RequestPolicy:
    def check(self,message:MessageInput)->PolicyDecision:
        blocked_phrases = (
            "give me a legal advice",
            "tell me how to break the law"
        )

        normalized_messages =message.message.lower()

        for phrase in blocked_phrases:
            if phrase in normalized_messages:
                return PolicyDecision(
                    allowed = False,
                    reason = "The request is outside the supported scope"
                )

        return PolicyDecision(
            allowed = True
        )
