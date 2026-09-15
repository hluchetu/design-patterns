from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable


type EventType = type[object]
type Callback = Callable[[object], None]


class HookRegistry:
    """Routes each event to callbacks registered for its type."""

    def __init__(self) -> None:
        self._callbacks: defaultdict[EventType, list[Callback]] = defaultdict(list)

    def subscribe(
        self,
        event_type: EventType,
        callback: Callback,
    ) -> None:
        """Register a callback for an event type."""
        self._callbacks[event_type].append(callback)

    def notify(self, event: object) -> None:
        """Notify callbacks registered for this event's exact type."""
        for callback in self._callbacks[type(event)]:
            callback(event)
