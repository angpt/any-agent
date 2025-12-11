<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/span_print.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `callbacks.span_print`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/span_print.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ConsolePrintSpan`
Use rich's console to print the `Context.current_span`. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/span_print.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(console: 'Console | None' = None) → None
```

Init the ConsolePrintSpan. 



**Args:**
 
 - <b>`console`</b>:  An optional instance of `rich.console.Console`.  If `None`, a new instance will be used. 




---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/span_print.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `after_llm_call`

```python
after_llm_call(context: 'Context', *args, **kwargs) → Context
```





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/span_print.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `after_tool_execution`

```python
after_tool_execution(context: 'Context', *args, **kwargs) → Context
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
