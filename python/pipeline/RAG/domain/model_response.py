from dataclasses import dataclass


@dataclass(frozen=True)
class ModelResponse:
    output_text: str
    document_ids: tuple[str, ...] = ()
