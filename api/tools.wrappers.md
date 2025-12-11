<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/wrappers.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tools.wrappers`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **WRAPPERS**

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/wrappers.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `verify_callable`

```python
verify_callable(tool: Callable[, Any]) → None
```

Verify that `tool` is a valid callable. 


- It needs to have some sort of docstring that describes what it does 
- It needs to have typed argument 
- It needs to have a typed return. 

We need these things because this info gets provided to the agent so that they know how and when to call the tool. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
