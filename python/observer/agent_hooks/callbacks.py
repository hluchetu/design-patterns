from __future__ import annotations

from observer.agent_hooks.events import (
    AfterModelCall,
    AfterToolCall,
    BeforeModelCall,
    BeforeToolCall,
)


def trace_model_start(event: object) -> None:
    if not isinstance(event, BeforeModelCall):
        return

    print(f"[trace] model call started at step {event.step}")
    print(f"[trace] messages: {len(event.messages)}")


def trace_model_end(event: object) -> None:
    if not isinstance(event, AfterModelCall):
        return

    print(f"[trace] model call finished at step {event.step} ({event.duration_ms:.2f} ms)")


def trace_tool_start(event: object) -> None:
    if not isinstance(event, BeforeToolCall):
        return

    print(f"[trace] tool started: {event.tool_name} with arguments {event.arguments}")


def trace_tool_end(event: object) -> None:
    if not isinstance(event, AfterToolCall):
        return

    print(f"[trace] tool finished: {event.tool_name}")
    print(f"[trace] result: {event.result}")
