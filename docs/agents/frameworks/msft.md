# Microsoft Agent Framework

[https://github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)

## Default Agent Type

We use [`agent_framework.ChatAgent`](https://learn.microsoft.com/en-us/python/api/agent-framework-core/agent_framework.chatagent?view=agent-framework-python-latest) as default.
Check the reference to find additional supported `agent_args`.

## Default Model Type

We use [`agent_framework.openai.OpenAIChatClient`](https://learn.microsoft.com/en-us/agent-framework/agents/providers/openai?pivots=programming-language-python) as the default chat client.
You can pass a different client (e.g., `AzureOpenAIChatClient`) via `model_type`.

## Run args

Check [`ChatAgent.run`](https://learn.microsoft.com/en-us/python/api/agent-framework-core/agent_framework.chatagent?view=agent-framework-python-latest#agent_framework.ChatAgent.run) to find additional supported `AnyAgent.run` args.
