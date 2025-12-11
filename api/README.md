<!-- markdownlint-disable -->

# API Overview

## Modules

- [`callbacks`](./callbacks.md#module-callbacks)
- [`callbacks.base`](./callbacks.base.md#module-callbacksbase)
- [`callbacks.context`](./callbacks.context.md#module-callbackscontext)
- [`callbacks.span_end`](./callbacks.span_end.md#module-callbacksspan_end)
- [`callbacks.span_generation`](./callbacks.span_generation.md#module-callbacksspan_generation)
- [`callbacks.span_generation.agno`](./callbacks.span_generation.agno.md#module-callbacksspan_generationagno)
- [`callbacks.span_generation.base`](./callbacks.span_generation.base.md#module-callbacksspan_generationbase)
- [`callbacks.span_generation.google`](./callbacks.span_generation.google.md#module-callbacksspan_generationgoogle)
- [`callbacks.span_generation.langchain`](./callbacks.span_generation.langchain.md#module-callbacksspan_generationlangchain)
- [`callbacks.span_generation.llama_index`](./callbacks.span_generation.llama_index.md#module-callbacksspan_generationllama_index)
- [`callbacks.span_generation.openai`](./callbacks.span_generation.openai.md#module-callbacksspan_generationopenai)
- [`callbacks.span_generation.smolagents`](./callbacks.span_generation.smolagents.md#module-callbacksspan_generationsmolagents)
- [`callbacks.span_generation.tinyagent`](./callbacks.span_generation.tinyagent.md#module-callbacksspan_generationtinyagent)
- [`callbacks.span_print`](./callbacks.span_print.md#module-callbacksspan_print)
- [`callbacks.wrappers`](./callbacks.wrappers.md#module-callbackswrappers)
- [`callbacks.wrappers.agno`](./callbacks.wrappers.agno.md#module-callbackswrappersagno)
- [`callbacks.wrappers.google`](./callbacks.wrappers.google.md#module-callbackswrappersgoogle)
- [`callbacks.wrappers.langchain`](./callbacks.wrappers.langchain.md#module-callbackswrapperslangchain)
- [`callbacks.wrappers.llama_index`](./callbacks.wrappers.llama_index.md#module-callbackswrappersllama_index)
- [`callbacks.wrappers.openai`](./callbacks.wrappers.openai.md#module-callbackswrappersopenai)
- [`callbacks.wrappers.smolagents`](./callbacks.wrappers.smolagents.md#module-callbackswrapperssmolagents)
- [`callbacks.wrappers.tinyagent`](./callbacks.wrappers.tinyagent.md#module-callbackswrapperstinyagent)
- [`config`](./config.md#module-config)
- [`evaluation`](./evaluation.md#module-evaluation)
- [`evaluation.agent_judge`](./evaluation.agent_judge.md#module-evaluationagent_judge)
- [`evaluation.llm_judge`](./evaluation.llm_judge.md#module-evaluationllm_judge)
- [`evaluation.schemas`](./evaluation.schemas.md#module-evaluationschemas)
- [`evaluation.tools`](./evaluation.tools.md#module-evaluationtools)
- [`frameworks`](./frameworks.md#module-frameworks)
- [`frameworks.any_agent`](./frameworks.any_agent.md#module-frameworksany_agent)
- [`frameworks.tinyagent`](./frameworks.tinyagent.md#module-frameworkstinyagent)
- [`logging`](./logging.md#module-logging): Logging package for Python. Based on PEP 282 and comments thereto in
- [`serving`](./serving.md#module-serving)
- [`serving.a2a`](./serving.a2a.md#module-servinga2a)
- [`serving.a2a.context_manager`](./serving.a2a.context_manager.md#module-servinga2acontext_manager)
- [`serving.mcp`](./serving.mcp.md#module-servingmcp)
- [`serving.mcp.config_mcp`](./serving.mcp.config_mcp.md#module-servingmcpconfig_mcp)
- [`serving.mcp.server_mcp`](./serving.mcp.server_mcp.md#module-servingmcpserver_mcp)
- [`serving.server_handle`](./serving.server_handle.md#module-servingserver_handle)
- [`testing`](./testing.md#module-testing)
- [`testing.helpers`](./testing.helpers.md#module-testinghelpers)
- [`tools`](./tools.md#module-tools)
- [`tools.a2a`](./tools.a2a.md#module-toolsa2a)
- [`tools.final_output`](./tools.final_output.md#module-toolsfinal_output)
- [`tools.mcp`](./tools.mcp.md#module-toolsmcp)
- [`tools.mcp.mcp_client`](./tools.mcp.mcp_client.md#module-toolsmcpmcp_client): Simplified MCP client that handles all transport types and frameworks.
- [`tools.mcp.smolagents_client`](./tools.mcp.smolagents_client.md#module-toolsmcpsmolagents_client)
- [`tools.user_interaction`](./tools.user_interaction.md#module-toolsuser_interaction)
- [`tools.web_browsing`](./tools.web_browsing.md#module-toolsweb_browsing)
- [`tools.wrappers`](./tools.wrappers.md#module-toolswrappers)
- [`tracing`](./tracing.md#module-tracing)
- [`tracing.agent_trace`](./tracing.agent_trace.md#module-tracingagent_trace)
- [`tracing.attributes`](./tracing.attributes.md#module-tracingattributes)
- [`tracing.otel_types`](./tracing.otel_types.md#module-tracingotel_types)
- [`utils`](./utils.md#module-utils): Utility functions for any-agent.
- [`utils.cast`](./utils.cast.md#module-utilscast)

## Classes

- [`base.Callback`](./callbacks.base.md#class-callback): Base class for AnyAgent callbacks.
- [`context.Context`](./callbacks.context.md#class-context): Object that will be shared across callbacks.
- [`span_end.SpanEndCallback`](./callbacks.span_end.md#class-spanendcallback): End the current span and add it to the corresponding `AgentTrace`.
- [`span_print.ConsolePrintSpan`](./callbacks.span_print.md#class-consoleprintspan): Use rich's console to print the `Context.current_span`.
- [`config.AgentConfig`](./config.md#class-agentconfig)
- [`config.AgentFramework`](./config.md#class-agentframework)
- [`config.MCPSse`](./config.md#class-mcpsse)
- [`config.MCPStdio`](./config.md#class-mcpstdio)
- [`config.MCPStreamableHttp`](./config.md#class-mcpstreamablehttp)
- [`config.ServingConfig`](./config.md#class-servingconfig): Configuration for serving an agent using the Agent2Agent Protocol (A2A).
- [`agent_judge.AgentJudge`](./evaluation.agent_judge.md#class-agentjudge): An agent that evaluates the correctness of another agent's trace.
- [`llm_judge.LlmJudge`](./evaluation.llm_judge.md#class-llmjudge)
- [`schemas.EvaluationOutput`](./evaluation.schemas.md#class-evaluationoutput)
- [`tools.TraceTools`](./evaluation.tools.md#class-tracetools)
- [`any_agent.AgentRunError`](./frameworks.any_agent.md#class-agentrunerror): Error that wraps underlying framework specific errors and carries spans.
- [`any_agent.AnyAgent`](./frameworks.any_agent.md#class-anyagent): Base abstract class for all agent implementations.
- [`tinyagent.TinyAgent`](./frameworks.tinyagent.md#class-tinyagent): A lightweight agent implementation using any-llm.
- [`tinyagent.ToolExecutor`](./frameworks.tinyagent.md#class-toolexecutor): Executor for tools that wraps tool functions to work with the MCP client.
- [`logging.BufferingFormatter`](./logging.md#class-bufferingformatter): A formatter suitable for formatting a number of records.
- [`logging.FileHandler`](./logging.md#class-filehandler): A handler class which writes formatted logging records to disk files.
- [`logging.Filter`](./logging.md#class-filter): Filter instances are used to perform arbitrary filtering of LogRecords.
- [`logging.Filterer`](./logging.md#class-filterer): A base class for loggers and handlers which allows them to share
- [`logging.Formatter`](./logging.md#class-formatter): Formatter instances are used to convert a LogRecord to text.
- [`logging.Handler`](./logging.md#class-handler): Handler instances dispatch logging events to specific destinations.
- [`logging.LogRecord`](./logging.md#class-logrecord): A LogRecord instance represents an event being logged.
- [`logging.Logger`](./logging.md#class-logger): Instances of the Logger class represent a single logging channel. A
- [`logging.LoggerAdapter`](./logging.md#class-loggeradapter): An adapter for loggers which makes it easier to specify contextual
- [`logging.Manager`](./logging.md#class-manager): There is [under normal circumstances] just one Manager instance, which
- [`logging.NullHandler`](./logging.md#class-nullhandler): This handler does nothing. It's intended to be used to avoid the
- [`logging.PercentStyle`](./logging.md#class-percentstyle)
- [`logging.PlaceHolder`](./logging.md#class-placeholder): PlaceHolder instances are used in the Manager logger hierarchy to take
- [`logging.RootLogger`](./logging.md#class-rootlogger): A root logger is not that different to any other logger, except that
- [`logging.StrFormatStyle`](./logging.md#class-strformatstyle)
- [`logging.StreamHandler`](./logging.md#class-streamhandler): A handler class which writes logging records, appropriately formatted,
- [`logging.StringTemplateStyle`](./logging.md#class-stringtemplatestyle)
- [`context_manager.ContextData`](./serving.a2a.context_manager.md#class-contextdata): Data stored for each task.
- [`context_manager.ContextManager`](./serving.a2a.context_manager.md#class-contextmanager): Manages agent conversation context for multi-turn interactions.
- [`config_mcp.MCPServingConfig`](./serving.mcp.config_mcp.md#class-mcpservingconfig): Configuration for serving an agent using the Model Context Protocol (MCP).
- [`server_handle.ServerHandle`](./serving.server_handle.md#class-serverhandle): A handle for managing an async server instance.
- [`mcp_client.MCPClient`](./tools.mcp.mcp_client.md#class-mcpclient): Unified MCP client that handles all transport types and frameworks.
- [`smolagents_client.SmolagentsMCPClient`](./tools.mcp.smolagents_client.md#class-smolagentsmcpclient): Smolagents-specific MCP client that uses smolagents.mcp_client.MCPClient.
- [`agent_trace.AgentMessage`](./tracing.agent_trace.md#class-agentmessage): A message that can be exported to JSON or printed to the console.
- [`agent_trace.AgentSpan`](./tracing.agent_trace.md#class-agentspan): A span that can be exported to JSON or printed to the console.
- [`agent_trace.AgentTrace`](./tracing.agent_trace.md#class-agenttrace): A trace that can be exported to JSON or printed to the console.
- [`agent_trace.CostInfo`](./tracing.agent_trace.md#class-costinfo): Cost information.
- [`agent_trace.TokenInfo`](./tracing.agent_trace.md#class-tokeninfo): Token Count information.
- [`attributes.AnyAgentAttributes`](./tracing.attributes.md#class-anyagentattributes): Span-attribute keys specific to AnyAgent library.
- [`attributes.GenAI`](./tracing.attributes.md#class-genai): Constants exported for convenience to access span attributes.
- [`otel_types.AttributeValue`](./tracing.otel_types.md#class-attributevalue): A wrapper for attribute values that can be serialized.
- [`otel_types.Event`](./tracing.otel_types.md#class-event): Serializable event.
- [`otel_types.Link`](./tracing.otel_types.md#class-link): Serializable link.
- [`otel_types.Resource`](./tracing.otel_types.md#class-resource): Serializable resource.
- [`otel_types.SpanContext`](./tracing.otel_types.md#class-spancontext): Serializable span context.
- [`otel_types.SpanKind`](./tracing.otel_types.md#class-spankind): String-based enum for span kind to make it serializable.
- [`otel_types.Status`](./tracing.otel_types.md#class-status): Serializable status.
- [`otel_types.StatusCode`](./tracing.otel_types.md#class-statuscode): String-based enum for status code to make it serializable.
- [`otel_types.TraceFlags`](./tracing.otel_types.md#class-traceflags): Serializable trace flags.
- [`otel_types.TraceState`](./tracing.otel_types.md#class-tracestate): Serializable trace state.

## Functions

- [`callbacks.get_default_callbacks`](./callbacks.md#function-get_default_callbacks): Return instances of the default callbacks used in any-agent.
- [`tinyagent.final_answer`](./frameworks.tinyagent.md#function-final_answer): Return the final answer to the user.
- [`logging.addLevelName`](./logging.md#function-addlevelname): Associate 'levelName' with 'level'.
- [`logging.basicConfig`](./logging.md#function-basicconfig): Do basic configuration for the logging system.
- [`logging.captureWarnings`](./logging.md#function-capturewarnings): If capture is true, redirect all warnings to the logging package.
- [`logging.critical`](./logging.md#function-critical): Log a message with severity 'CRITICAL' on the root logger. If the logger
- [`serving._raise`](./serving.md#function-_raise)
- [`serving._raise`](./serving.md#function-_raise)
- [`server_mcp.serve_mcp_async`](./serving.mcp.server_mcp.md#function-serve_mcp_async): Provide an MCP server to be used in an event loop.
- [`helpers.get_default_agent_model_args`](./testing.helpers.md#function-get_default_agent_model_args): Get the default model arguments for an agent framework.
- [`helpers.group_spans`](./testing.helpers.md#function-group_spans): Group spans into agent invocations, llm calls and tool executions.
- [`helpers.wait_for_server`](./testing.helpers.md#function-wait_for_server): Wait for a server to be ready.
- [`helpers.wait_for_server_async`](./testing.helpers.md#function-wait_for_server_async): Wait for a server to be ready.
- [`a2a.a2a_tool`](./tools.a2a.md#function-a2a_tool): Perform a query using A2A to another agent (synchronous version).
- [`a2a.a2a_tool_async`](./tools.a2a.md#function-a2a_tool_async): Perform a query using A2A to another agent.
- [`final_output.prepare_final_output`](./tools.final_output.md#function-prepare_final_output): Prepare instructions and tools for structured output, returning the function directly.
- [`user_interaction.ask_user_verification`](./tools.user_interaction.md#function-ask_user_verification): Asks user to verify the given `query`.
- [`user_interaction.send_console_message`](./tools.user_interaction.md#function-send_console_message): Send the specified user a message via console and returns their response.
- [`user_interaction.show_final_output`](./tools.user_interaction.md#function-show_final_output): Show the final answer to the user.
- [`user_interaction.show_plan`](./tools.user_interaction.md#function-show_plan): Show the current plan to the user.
- [`web_browsing.search_tavily`](./tools.web_browsing.md#function-search_tavily): Perform a Tavily web search based on your query and return the top search results.
- [`web_browsing.search_web`](./tools.web_browsing.md#function-search_web): Perform a duckduckgo web search based on your query (think a Google search) then returns the top search results.
- [`web_browsing.visit_webpage`](./tools.web_browsing.md#function-visit_webpage): Visits a webpage at the given url and reads its content as a markdown string. Use this to browse webpages.
- [`wrappers.verify_callable`](./tools.wrappers.md#function-verify_callable): Verify that `tool` is a valid callable.
- [`cast.safe_cast_argument`](./utils.cast.md#function-safe_cast_argument): Safely cast an argument to the specified type, handling union types.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
