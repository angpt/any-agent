<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/testing/helpers.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `testing.helpers`




**Global Variables**
---------------
- **DEFAULT_SMALL_MODEL_ID**
- **LLM_IMPORT_PATHS**
- **DEFAULT_HTTP_KWARGS**

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/testing/helpers.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_default_agent_model_args`

```python
get_default_agent_model_args(
    agent_framework: AgentFramework,
    model_id: str | None = None
) → dict[str, Any]
```

Get the default model arguments for an agent framework. 



**Args:**
 
 - <b>`agent_framework`</b> (AgentFramework):  The agent framework to get the default model arguments for. 
 - <b>`model_id`</b> (str, optional):  The model ID to get specific model arguments for. Defaults to None. 



**Returns:**
 
 - <b>`dict[str, Any]`</b>:  The default model arguments for the agent framework. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/testing/helpers.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `wait_for_server`

```python
wait_for_server(
    server_url: str,
    max_attempts: int = 20,
    poll_interval: float = 0.5
) → None
```

Wait for a server to be ready. 



**Args:**
 
 - <b>`server_url`</b> (str):  The URL of the server to wait for. 
 - <b>`max_attempts`</b> (int):  The maximum number of attempts to make. 
 - <b>`poll_interval`</b> (float):  The interval between attempts. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/testing/helpers.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `wait_for_server_async`

```python
wait_for_server_async(
    server_url: str,
    max_attempts: int = 20,
    poll_interval: float = 0.5
) → None
```

Wait for a server to be ready. 



**Args:**
 
 - <b>`server_url`</b> (str):  The URL of the server to wait for. 
 - <b>`max_attempts`</b> (int):  The maximum number of attempts to make. 
 - <b>`poll_interval`</b> (float):  The interval between attempts. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/testing/helpers.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `group_spans`

```python
group_spans(
    spans: Sequence[AgentSpan]
) → tuple[Sequence[AgentSpan], Sequence[AgentSpan], Sequence[AgentSpan]]
```

Group spans into agent invocations, llm calls and tool executions. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
