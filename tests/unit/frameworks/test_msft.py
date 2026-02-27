from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from any_agent import AgentConfig, AgentFramework, AnyAgent


def test_load_msft_default() -> None:
    mock_chat_agent = MagicMock()
    mock_chat_client = MagicMock()

    with (
        patch("any_agent.frameworks.msft.MsftChatAgent", mock_chat_agent),
        patch("any_agent.frameworks.msft.OpenAIChatClient", mock_chat_client),
    ):
        AnyAgent.create(
            AgentFramework.MSFT,
            AgentConfig(model_id="gpt-4o"),
        )

        mock_chat_client.assert_called_once_with(
            model_id="gpt-4o",
        )
        mock_chat_agent.assert_called_once_with(
            chat_client=mock_chat_client.return_value,
            name="any_agent",
            instructions="",
            tools=[],
        )


def test_load_msft_with_api_key() -> None:
    mock_chat_agent = MagicMock()
    mock_chat_client = MagicMock()

    with (
        patch("any_agent.frameworks.msft.MsftChatAgent", mock_chat_agent),
        patch("any_agent.frameworks.msft.OpenAIChatClient", mock_chat_client),
    ):
        AnyAgent.create(
            AgentFramework.MSFT,
            AgentConfig(model_id="gpt-4o", api_key="test-key"),
        )

        mock_chat_client.assert_called_once_with(
            model_id="gpt-4o",
            api_key="test-key",
        )


def test_load_msft_with_api_base() -> None:
    mock_chat_agent = MagicMock()
    mock_chat_client = MagicMock()

    with (
        patch("any_agent.frameworks.msft.MsftChatAgent", mock_chat_agent),
        patch("any_agent.frameworks.msft.OpenAIChatClient", mock_chat_client),
    ):
        AnyAgent.create(
            AgentFramework.MSFT,
            AgentConfig(model_id="gpt-4o", api_base="https://custom.endpoint.com"),
        )

        mock_chat_client.assert_called_once_with(
            model_id="gpt-4o",
            base_url="https://custom.endpoint.com",
        )


def test_load_msft_agent_missing() -> None:
    with patch("any_agent.frameworks.msft.msft_available", False):
        with pytest.raises(ImportError):
            AnyAgent.create(
                AgentFramework.MSFT,
                AgentConfig(model_id="gpt-4o"),
            )


def test_load_msft_with_instructions() -> None:
    mock_chat_agent = MagicMock()
    mock_chat_client = MagicMock()

    with (
        patch("any_agent.frameworks.msft.MsftChatAgent", mock_chat_agent),
        patch("any_agent.frameworks.msft.OpenAIChatClient", mock_chat_client),
    ):
        AnyAgent.create(
            AgentFramework.MSFT,
            AgentConfig(
                model_id="gpt-4o",
                instructions="You are a helpful assistant.",
            ),
        )

        mock_chat_agent.assert_called_once_with(
            chat_client=mock_chat_client.return_value,
            name="any_agent",
            instructions="You are a helpful assistant.",
            tools=[],
        )


def test_run_msft_agent() -> None:
    mock_chat_agent_cls = MagicMock()
    mock_chat_client = MagicMock()
    mock_agent_instance = MagicMock()
    mock_agent_instance.middleware = []
    mock_result = MagicMock()
    mock_result.text = "Hello, world!"
    mock_agent_instance.run = AsyncMock(return_value=mock_result)
    mock_chat_agent_cls.return_value = mock_agent_instance

    with (
        patch("any_agent.frameworks.msft.MsftChatAgent", mock_chat_agent_cls),
        patch("any_agent.frameworks.msft.OpenAIChatClient", mock_chat_client),
    ):
        agent = AnyAgent.create(
            AgentFramework.MSFT,
            AgentConfig(model_id="gpt-4o", callbacks=[]),
        )
        result = agent.run("Tell me a joke")
        assert result.final_output == "Hello, world!"


def test_load_msft_with_custom_model_type() -> None:
    mock_chat_agent = MagicMock()
    mock_custom_client = MagicMock()

    with patch("any_agent.frameworks.msft.MsftChatAgent", mock_chat_agent):
        AnyAgent.create(
            AgentFramework.MSFT,
            AgentConfig(
                model_id="gpt-4o",
                model_type=mock_custom_client,
            ),
        )

        mock_custom_client.assert_called_once_with(
            model_id="gpt-4o",
        )
