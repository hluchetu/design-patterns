from __future__ import annotations

from observer.agent_hooks.callbacks import (
    trace_model_end,
    trace_model_start,
    trace_tool_end,
    trace_tool_start,
)
from observer.agent_hooks.events import (
    AfterModelCall,
    AfterToolCall,
    BeforeModelCall,
    BeforeToolCall,
)
from observer.agent_hooks.registry import HookRegistry


def main() -> None:
    hooks = HookRegistry()

    hooks.subscribe(BeforeModelCall, trace_model_start)
    hooks.subscribe(AfterModelCall, trace_model_end)
    hooks.subscribe(BeforeToolCall, trace_tool_start)
    hooks.subscribe(AfterToolCall, trace_tool_end)

    messages = ["Find the latest Python release"]

    hooks.notify(
        BeforeModelCall(
            messages=messages,
            step=1,
        )
    )

    hooks.notify(
        AfterModelCall(
            response="Python 3.14 is the latest release.",
            step=1,
            duration_ms=245.5,
        )
    )

    hooks.notify(
        BeforeToolCall(
            tool_name="web_search",
            arguments={"query": "latest Python release"},
            step=1,
        )
    )

    hooks.notify(
        AfterToolCall(
            tool_name="web_search",
            result="Search completed",
            step=1,
            duration_ms=812.2,
        )
    )


if __name__ == "__main__":
    main()
