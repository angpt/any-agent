# mypy: disable-error-code="method-assign,no-untyped-def"
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from any_agent.callbacks.span_generation.base import _SpanGeneration

if TYPE_CHECKING:
    from any_agent.callbacks.context import Context


class _MsftSpanGeneration(_SpanGeneration):
    def before_llm_call(self, context: Context, *args, **kwargs) -> Context:
        return self._set_llm_input(
            context,
            model_id=kwargs.get("model_id", "No model"),
            input_messages=kwargs.get("messages", []),
        )

    def after_llm_call(self, context: Context, *args, **kwargs) -> Context:
        response = args[0]

        output = getattr(response, "text", "") or ""

        input_tokens = 0
        output_tokens = 0
        if usage := getattr(response, "usage_details", None):
            input_tokens = getattr(usage, "input_token_count", 0) or 0
            output_tokens = getattr(usage, "output_token_count", 0) or 0

        return self._set_llm_output(context, output, input_tokens, output_tokens)

    def before_tool_execution(self, context: Context, *args, **kwargs) -> Context:
        request: dict[str, Any] = args[0] if args else {}

        return self._set_tool_input(
            context,
            name=request.get("name", "No name"),
            args=request.get("arguments", {}),
        )

    def after_tool_execution(self, context: Context, *args, **kwargs) -> Context:
        return self._set_tool_output(context, args[0] if args else None)
