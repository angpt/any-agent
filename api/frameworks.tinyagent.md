<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `frameworks.tinyagent`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **DEFAULT_SYSTEM_PROMPT**

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `final_answer`

```python
final_answer(answer: 'str') → str
```

Return the final answer to the user. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ToolExecutor`
Executor for tools that wraps tool functions to work with the MCP client. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(tool_function: 'Callable[, Any]') → None
```

Initialize the tool executor. 



**Args:**
 
 - <b>`tool_function`</b>:  The tool function to execute 




---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `call_tool`

```python
call_tool(request: 'dict[str, Any]') → str
```

Call the tool function. 



**Args:**
 
 - <b>`request`</b>:  The tool request with name and arguments 



**Returns:**
 Tool execution result 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TinyAgent`
A lightweight agent implementation using any-llm. 

Modeled after JS implementation https://huggingface.co/blog/tiny-agents. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(config: 'AgentConfig') → None
```

Initialize the TinyAgent. 



**Args:**
 
 - <b>`config`</b>:  Agent configuration 
 - <b>`tracing`</b>:  Optional tracing configuration 


---

#### <kbd>property</kbd> agent

The underlying agent implementation from the framework. 

This property is intentionally restricted to maintain framework abstraction and prevent direct dependency on specific agent implementations. 

If you need functionality that relies on accessing the underlying agent: 1. Consider if the functionality can be added to the AnyAgent interface 2. Submit a GitHub issue describing your use case 3. Contribute a PR implementing the needed functionality 



**Raises:**
 
 - <b>`NotImplementedError`</b>:  Always raised when this property is accessed 

---

#### <kbd>property</kbd> framework







---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L289"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `call_model`

```python
call_model(**completion_params: 'dict[str, Any]') → ChatCompletion
```





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/tinyagent.py#L292"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_output_type_async`

```python
update_output_type_async(output_type: 'type[BaseModel] | None') → None
```

Update the output type of the agent in-place. 



**Args:**
 
 - <b>`output_type`</b>:  The new output type to use, or None to remove output type constraint 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
