from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def display_message(sender: str, message: str) -> None:
    """Observer that displays the message."""
    print(f"{sender} sent: {message}")


class MessageLogger:
    """Observer object that logs the message."""

    def __call__(self, sender: str, message: str) -> None:
        logger.info("Message received from %s: %s", sender, message)
