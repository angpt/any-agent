<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/user_interaction.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tools.user_interaction`





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/user_interaction.py#L6"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `show_plan`

```python
show_plan(plan: str) → str
```

Show the current plan to the user. 



**Args:**
 
 - <b>`plan`</b>:  The current plan. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/user_interaction.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `show_final_output`

```python
show_final_output(answer: str) → str
```

Show the final answer to the user. 



**Args:**
 
 - <b>`answer`</b>:  The final answer. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/user_interaction.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ask_user_verification`

```python
ask_user_verification(query: str) → str
```

Asks user to verify the given `query`. 



**Args:**
 
 - <b>`query`</b>:  The question that requires verification. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/user_interaction.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `send_console_message`

```python
send_console_message(user: str, query: str) → str
```

Send the specified user a message via console and returns their response. 



**Args:**
 
 - <b>`query`</b>:  The question to ask the user. 
 - <b>`user`</b>:  The user to ask the question to. 



**Returns:**
 
 - <b>`str`</b>:  The user's response. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
