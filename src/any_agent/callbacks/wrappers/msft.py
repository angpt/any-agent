# mypy: disable-error-code="method-assign,misc,no-untyped-call,no-untyped-def,union-attr,unused-ignore"
from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any

from opentelemetry.trace import get_current_span

try:
    from agent_framework import ChatMiddleware as _MsftChatMiddleware
    from agent_framework import FunctionMiddleware as _MsftFunctionMiddleware
except ImportError:
    _MsftChatMiddleware = object  # type: ignore[assignment,misc]
    _MsftFunctionMiddleware = object  # type: ignore[assignment,misc]

if TYPE_CHECKING:
    from collections.abc import Callable

    from any_agent.callbacks.context import Context
    from any_agent.frameworks.msft import MsftAgent


class _AnyAgentChatMiddleware(_MsftChatMiddleware):  # type: ignore[valid-type,misc]
    """ChatMiddleware that fires any-agent callbacks around each LLM call."""

    def __init__(
        self,
        callback_context: dict[int, Context],
        agent_ref: MsftAgent,
    ) -> None:
        self.callback_context = callback_context
        self._agent_ref = agent_ref

    async def process(self, msft_ctx: Any, next_: Callable[..., Any]) -> None:
        trace_id = get_current_span().get_span_context().trace_id
        context = self.callback_context[trace_id]

        chat_options = getattr(msft_ctx, "chat_options", None)
        model_id = getattr(chat_options, "model_id", None) or "No model"
        messages = getattr(msft_ctx, "messages", [])

        for callback in self._agent_ref.config.callbacks:
            result = callback.before_llm_call(
                context, model_id=model_id, messages=messages
            )
            if asyncio.iscoroutinefunction(callback.before_llm_call):
                context = await result
            else:
                context = result

        await next_(msft_ctx)

        for callback in self._agent_ref.config.callbacks:
            result = callback.after_llm_call(context, msft_ctx.result)
            if asyncio.iscoroutinefunction(callback.after_llm_call):
                context = await result
            else:
                context = result


class _AnyAgentFunctionMiddleware(_MsftFunctionMiddleware):  # type: ignore[valid-type,misc]
    """FunctionMiddleware that fires any-agent callbacks around each tool call."""

    def __init__(
        self,
        callback_context: dict[int, Context],
        agent_ref: MsftAgent,
    ) -> None:
        self.callback_context = callback_context
        self._agent_ref = agent_ref

    async def process(self, msft_ctx: Any, next_: Callable[..., Any]) -> None:
        trace_id = get_current_span().get_span_context().trace_id
        context = self.callback_context[trace_id]

        func = getattr(msft_ctx, "function", None)
        args = getattr(msft_ctx, "arguments", None)
        tool_request = {
            "name": getattr(func, "name", "No name"),
            "arguments": args.model_dump() if args is not None else {},
        }

        for callback in self._agent_ref.config.callbacks:
            result = callback.before_tool_execution(context, tool_request)
            if asyncio.iscoroutinefunction(callback.before_tool_execution):
                context = await result
            else:
                context = result

        await next_(msft_ctx)

        # Extract the result string from FunctionExecutionResult
        raw = msft_ctx.result
        if hasattr(raw, "content") and hasattr(raw.content, "result"):
            tool_output = raw.content.result
        elif hasattr(raw, "result"):
            tool_output = raw.result
        else:
            tool_output = str(raw) if raw is not None else ""

        for callback in self._agent_ref.config.callbacks:
            result = callback.after_tool_execution(context, tool_output)
            if asyncio.iscoroutinefunction(callback.after_tool_execution):
                context = await result
            else:
                context = result


class _MsftWrapper:
    def __init__(self) -> None:
        self.callback_context: dict[int, Context] = {}
        self._chat_middleware: _AnyAgentChatMiddleware | None = None
        self._function_middleware: _AnyAgentFunctionMiddleware | None = None

    async def wrap(self, agent: MsftAgent) -> None:
        self._chat_middleware = _AnyAgentChatMiddleware(self.callback_context, agent)
        self._function_middleware = _AnyAgentFunctionMiddleware(
            self.callback_context, agent
        )

        if agent._agent.middleware is None:
            agent._agent.middleware = []
        agent._agent.middleware.append(self._chat_middleware)
        agent._agent.middleware.append(self._function_middleware)

    async def unwrap(self, agent: MsftAgent) -> None:
        if agent._agent.middleware:
            if self._chat_middleware in agent._agent.middleware:
                agent._agent.middleware.remove(self._chat_middleware)
            if self._function_middleware in agent._agent.middleware:
                agent._agent.middleware.remove(self._function_middleware)
