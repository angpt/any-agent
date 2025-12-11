<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/final_output.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tools.final_output`





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/final_output.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `prepare_final_output`

```python
prepare_final_output(
    output_type: type[BaseModel],
    instructions: str | None = None
) → tuple[str, Callable[[str], dict[str, str | bool | dict[str, Any] | list[Any]]]]
```

Prepare instructions and tools for structured output, returning the function directly. 



**Args:**
 
 - <b>`output_type`</b>:  The Pydantic model type for structured output 
 - <b>`instructions`</b>:  Original instructions to modify 



**Returns:**
 Tuple of (modified_instructions, final_output_function) 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
