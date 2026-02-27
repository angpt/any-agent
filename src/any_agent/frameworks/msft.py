from __future__ import annotations

from typing import TYPE_CHECKING, Any

from any_agent.config import AgentConfig, AgentFramework

from .any_agent import AnyAgent

try:
    from agent_framework import ChatAgent as MsftChatAgent
    from agent_framework.openai import OpenAIChatClient

    msft_available = True
except ImportError:
    msft_available = False

if TYPE_CHECKING:
    from pydantic import BaseModel

DEFAULT_AGENT_TYPE = None
DEFAULT_MODEL_TYPE = None


class MsftAgent(AnyAgent):
    """Microsoft Agent Framework implementation."""

    def __init__(self, config: AgentConfig):
        super().__init__(config)
        self._agent: MsftChatAgent | None = None

    @property
    def framework(self) -> AgentFramework:
        return AgentFramework.MSFT

    def _get_chat_client(self, agent_config: AgentConfig) -> Any:
        """Get the chat client for the Microsoft agent."""
        model_type = agent_config.model_type or OpenAIChatClient
        model_args = agent_config.model_args or {}

        kwargs: dict[str, Any] = {}
        if agent_config.api_key:
            kwargs["api_key"] = agent_config.api_key
        if agent_config.api_base:
            kwargs["base_url"] = agent_config.api_base

        return model_type(
            model_id=agent_config.model_id,
            **kwargs,
            **model_args,
        )

    async def _load_agent(self) -> None:
        if not msft_available:
            msg = "You need to `pip install 'any-agent[msft]'` to use this agent"
            raise ImportError(msg)

        tools = await self._load_tools(self.config.tools)
        self._tools = tools

        chat_client = self._get_chat_client(self.config)

        agent_args = self.config.agent_args or {}

        self._agent = MsftChatAgent(
            chat_client=chat_client,
            name=self.config.name,
            instructions=self.config.instructions or "",
            tools=tools or [],
            **agent_args,
        )

    async def _run_async(
        self, prompt: str | list[dict[str, Any]], **kwargs: Any
    ) -> str | BaseModel:
        if not self._agent:
            error_message = "Agent not loaded. Call load_agent() first."
            raise ValueError(error_message)
        if not isinstance(prompt, str):
            msg = "Microsoft Agent Framework does not support list of messages as input. Use a plain string prompt."
            raise NotImplementedError(msg)

        result = await self._agent.run(prompt, **kwargs)

        output = result.text

        if self.config.output_type and output:
            return self.config.output_type.model_validate_json(output)

        return output or ""

    async def update_output_type_async(
        self, output_type: type[BaseModel] | None
    ) -> None:
        self.config.output_type = output_type
