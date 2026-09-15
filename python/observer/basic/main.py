from __future__ import annotations

import logging

from observer.basic.observers import MessageLogger, display_message
from observer.basic.subject import MessageSignal


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    message_signal = MessageSignal()

    message_signal.subscribe(display_message)
    message_signal.subscribe(MessageLogger())

    message_signal.notify("Alice", "Hello!")


if __name__ == "__main__":
    main()
