<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.tools`






---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TraceTools`




<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(trace: AgentTrace)
```








---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all_tools`

```python
get_all_tools() → list[Callable[, Any]]
```

Get all tool functions from this class. 



**Returns:**
 
 - <b>`list[callable]`</b>:  List of all tool functions 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_duration`

```python
get_duration() → float
```

Get the duration of the agent trace. 



**Returns:**
 
 - <b>`float`</b>:  The duration in seconds of the agent trace 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_final_output`

```python
get_final_output() → str | BaseModel | dict[str, Any] | None
```

Get the final output from the agent trace. 



**Returns:**
 
 - <b>`str | BaseModel | None`</b>:  The final output of the agent 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_messages_from_trace`

```python
get_messages_from_trace() → str
```

Get a summary of what happened in each step/span of the agent trace. 

This includes information about the input, output, and tool calls for each step. 



**Returns:**
 
 - <b>`str`</b>:  The evidence of all the spans in the trace 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_steps_taken`

```python
get_steps_taken() → int
```

Get the number of steps taken by the agent as reported by the trace. 



**Returns:**
 
 - <b>`int`</b>:  The number of steps taken by the agent 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/tools.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_tokens_used`

```python
get_tokens_used() → int
```

Get the number of tokens used by the agent as reported by the trace. 



**Returns:**
 
 - <b>`int`</b>:  The number of tokens used by the agent 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
