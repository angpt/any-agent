<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `serving.a2a.context_manager`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ContextData`
Data stored for each task. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(task_id: str)
```

Initialize task data. 



**Args:**
 
 - <b>`task_id`</b>:  Unique identifier for the task 




---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_expired`

```python
is_expired(timeout_minutes: int) → bool
```

Check if the task has expired. 



**Args:**
 
 - <b>`timeout_minutes`</b>:  Timeout in minutes 



**Returns:**
 True if task is expired, False otherwise 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_activity`

```python
update_activity() → None
```

Update the last activity timestamp. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ContextManager`
Manages agent conversation context for multi-turn interactions. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(config: 'A2AServingConfig')
```

Initialize the context manager. 



**Args:**
 
 - <b>`config`</b>:  Serving configuration containing context settings 




---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_context`

```python
add_context(context_id: str) → None
```

Store a new context. 

This method will also trigger cleanup of expired context 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `format_query_with_history`

```python
format_query_with_history(context_id: str, current_query: str) → str
```

Format a query with conversation history. 



**Args:**
 
 - <b>`context_id`</b>:  context ID to get history for 
 - <b>`current_query`</b>:  Current user query 



**Returns:**
 Formatted query string with history context 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L71"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_context`

```python
get_context(context_id: str) → ContextData | None
```

Get context data by ID. 



**Args:**
 
 - <b>`context_id`</b>:  context ID to retrieve 



**Returns:**
 ContextData if found and not expired, None otherwise 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `remove_context`

```python
remove_context(context_id: str) → None
```

Remove a context. 



**Args:**
 
 - <b>`context_id`</b>:  context ID to remove 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/a2a/context_manager.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_context_trace`

```python
update_context_trace(
    context_id: str,
    agent_trace: AgentTrace,
    original_query: str
) → None
```

Update the agent trace for a context. 



**Args:**
 
 - <b>`context_id`</b>:  context ID to update 
 - <b>`agent_trace`</b>:  New agent trace to merge/store 
 - <b>`original_query`</b>:  The original user query (without history formatting) 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
