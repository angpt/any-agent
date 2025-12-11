<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/attributes.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tracing.attributes`




**Global Variables**
---------------
- **GEN_AI_AGENT_DESCRIPTION**
- **GEN_AI_AGENT_NAME**
- **GEN_AI_OPERATION_NAME**
- **GEN_AI_OUTPUT_TYPE**
- **GEN_AI_REQUEST_MODEL**
- **GEN_AI_TOOL_DESCRIPTION**
- **GEN_AI_TOOL_NAME**
- **GEN_AI_USAGE_INPUT_TOKENS**
- **GEN_AI_USAGE_OUTPUT_TOKENS**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/attributes.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GenAI`
Constants exported for convenience to access span attributes. 

Trying to follow OpenTelemetry's [Semantic Conventions for Generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/). 

We import the constants from `opentelemetry.semconv._incubating.attributes.gen_ai_attributes` whenever is possible. 

We only expose the keys that we currently use in `any-agent`. 





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/attributes.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AnyAgentAttributes`
Span-attribute keys specific to AnyAgent library. 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
