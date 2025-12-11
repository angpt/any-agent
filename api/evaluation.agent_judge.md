<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/agent_judge.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.agent_judge`




**Global Variables**
---------------
- **INSIDE_NOTEBOOK**
- **AGENT_INSTRUCTIONS**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/agent_judge.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AgentJudge`
An agent that evaluates the correctness of another agent's trace. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/agent_judge.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    model_id: str,
    framework: AgentFramework = <AgentFramework.TINYAGENT: 'tinyagent'>,
    output_type: type[BaseModel] = <class 'any_agent.evaluation.schemas.EvaluationOutput'>,
    model_args: dict[str, Any] | None = None
)
```








---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/agent_judge.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    trace: AgentTrace,
    question: str,
    additional_tools: list[Callable[[], Any]] | None = None
) → AgentTrace
```

Run the agent judge. 



**Args:**
 
 - <b>`trace`</b>:  The agent trace to evaluate 
 - <b>`question`</b>:  The question to ask the agent 
 - <b>`additional_tools`</b>:  Additional tools to use for the agent 



**Returns:**
 The trace of the evaluation run. You can access the evaluation result in the `final_output` property. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/agent_judge.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run_async`

```python
run_async(
    trace: AgentTrace,
    question: str,
    additional_tools: list[Callable[[], Any]] | None = None
) → AgentTrace
```

Run the agent judge asynchronously. 



**Args:**
 
 - <b>`trace`</b>:  The agent trace to evaluate 
 - <b>`question`</b>:  The question to ask the agent 
 - <b>`additional_tools`</b>:  Additional tools to use for the agent 

**Returns:**
 The trace of the evaluation run. You can access the evaluation result in the `final_output` property. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
