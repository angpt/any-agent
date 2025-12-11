<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/a2a.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tools.a2a`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **a2a_tool_available**
- **INSIDE_NOTEBOOK**

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/a2a.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `a2a_tool_async`

```python
a2a_tool_async(
    url: str,
    toolname: Optional[str] = None,
    http_kwargs: dict[str, Any] | None = None
) → Callable[[str, Optional[str], Optional[str]], Coroutine[Any, Any, dict[str, Any]]]
```

Perform a query using A2A to another agent. 



**Args:**
 
 - <b>`url`</b> (str):  The url in which the A2A agent is located. 
 - <b>`toolname`</b> (str):  The name for the created tool. Defaults to `call_{agent name in card}`.  Leading and trailing whitespace are removed. Whitespace in the middle is replaced by `_`. 
 - <b>`http_kwargs`</b> (dict):  Additional kwargs to pass to the httpx client. 



**Returns:**
 An async `Callable` that takes a query and returns the agent response. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/a2a.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `a2a_tool`

```python
a2a_tool(
    url: str,
    toolname: Optional[str] = None,
    http_kwargs: dict[str, Any] | None = None
) → Callable[[str, Optional[str], Optional[str]], str]
```

Perform a query using A2A to another agent (synchronous version). 



**Args:**
 
 - <b>`url`</b> (str):  The url in which the A2A agent is located. 
 - <b>`toolname`</b> (str):  The name for the created tool. Defaults to `call_{agent name in card}`.  Leading and trailing whitespace are removed. Whitespace in the middle is replaced by `_`. 
 - <b>`http_kwargs`</b> (dict):  Additional kwargs to pass to the httpx client. 



**Returns:**
 A sync `Callable` that takes a query and returns the agent response. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
