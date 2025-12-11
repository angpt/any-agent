<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/llm_judge.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.llm_judge`




**Global Variables**
---------------
- **INSIDE_NOTEBOOK**
- **DEFAULT_PROMPT_TEMPLATE**
- **LLM_JUDGE_SYSTEM_PROMPT**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/llm_judge.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `LlmJudge`




<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/llm_judge.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    model_id: str,
    framework: AgentFramework = <AgentFramework.TINYAGENT: 'tinyagent'>,
    output_type: type[BaseModel] = <class 'any_agent.evaluation.schemas.EvaluationOutput'>,
    model_args: dict[str, Any] | None = None,
    system_prompt: str = "You are an expert evaluator that analyzes contextual information to answer specific questions about agent performance and behavior.\n\nYou will be provided with:\n1. Contextual information of an agent's execution that may be relevant to the evaluation question\n2. A specific evaluation question to answer\n\nYour task is to carefully analyze the context and provide a judgment on whether the agent's performance meets the criteria specified in the question.\n\nEVALUATION GUIDELINES:\n- Be objective and thorough in your analysis\n- If the question asks about specific actions, look for evidence of those actions in the context\n- If unsure, err on the side of being more critical rather than lenient\n\nYour output must match the following JSON schema:\n{response_schema}"
)
```








---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/llm_judge.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(
    context: str,
    question: str,
    prompt_template: str = 'Please answer the evaluation question given the following contextual information:\n\nCONTEXT:\n{context}\n\nEVALUATION QUESTION:\n{question}'
) → BaseModel
```

Run the judge synchronously. 



**Args:**
 
 - <b>`context`</b>:  Any relevant information that may be needed to answer the question 
 - <b>`question`</b>:  The question to ask the agent 
 - <b>`prompt_template`</b>:  The prompt to use for the LLM 



**Returns:**
 The evaluation result 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/evaluation/llm_judge.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run_async`

```python
run_async(
    context: str,
    question: str,
    prompt_template: str = 'Please answer the evaluation question given the following contextual information:\n\nCONTEXT:\n{context}\n\nEVALUATION QUESTION:\n{question}'
) → BaseModel
```

Run the LLM asynchronously. 



**Args:**
 
 - <b>`context`</b>:  Any relevant information that may be needed to answer the question 
 - <b>`question`</b>:  The question to ask the agent 
 - <b>`prompt_template`</b>:  The prompt to use for the LLM 



**Returns:**
 The evaluation result 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
