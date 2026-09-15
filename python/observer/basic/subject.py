from __future__ import annotations

from collections.abc import Callable


type Observer = Callable[[str, str], None]


class MessageSignal:
    """Subject that notifies observers when a message is sent."""

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        """Register an observer."""
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        """Remove an observer if it is registered."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, sender: str, message: str) -> None:
        """Notify every registered observer."""
        for observer in self._observers:
            observer(sender, message)
