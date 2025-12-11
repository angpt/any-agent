<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `callbacks`




**Global Variables**
---------------
- **base**: # mypy: disable-error-code="no-untyped-def"

- **context**
- **span_print**: # mypy: disable-error-code="arg-type,attr-defined,no-untyped-def,union-attr"


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/callbacks/__init__.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_default_callbacks`

```python
get_default_callbacks() → list[Callback]
```

Return instances of the default callbacks used in any-agent. 

This function is called internally when the user doesn't provide a value for [`AgentConfig.callbacks`][any_agent.config.AgentConfig.callbacks]. 



**Returns:**
  A list of instances containing: 


        - [`ConsolePrintSpan`][any_agent.callbacks.span_print.ConsolePrintSpan] 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
