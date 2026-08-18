from typing import Protocol


class Receiver(Protocol):
    def __call__(self,sender:str,message:str)->None:
        ...


class Signal:
    def __init__(self)->None:
        self.receivers: list[Receiver] = []

    def connect(self,receiver: Receiver)->None:
        self.receivers.append(receiver)

    def send(self,sender:str,message:str)->None:
        for receiver in self.receivers:
            receiver(sender,message)


def display_message(sender:str,message:str)->None:
    print(f"{sender}:{message}")

class MessageLogger:
    def __call__(self,sender:str,message:str)->None:
        print(f"LOG:{sender} sent'{message}'")

message_sent = Signal()

message_sent.connect(display_message)
message_sent.connect(MessageLogger())


message_sent.send("Alice", "Hello!")
