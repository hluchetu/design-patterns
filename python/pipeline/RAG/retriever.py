from typing import Protocol

from pipeline.RAG.domain.document import Document
from pipeline.RAG.domain.question import Question

class SearchDocuments(Protocol):
    def __call__(self,question:Question)->tuple[Document,...]:
        ...

class Retriever:
    def __init__(self,search:SearchDocuments)->None:
        self.search = search

    def retrieve(self,question:Question)->tuple[Document,...]:
        return self.search(question)
