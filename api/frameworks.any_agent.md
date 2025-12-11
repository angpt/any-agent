<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `frameworks.any_agent`




**Global Variables**
---------------
- **TYPE_CHECKING**
- **INSIDE_NOTEBOOK**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AgentRunError`
Error that wraps underlying framework specific errors and carries spans. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(trace: 'AgentTrace', original_exception: 'Exception')
```






---

#### <kbd>property</kbd> original_exception





---

#### <kbd>property</kbd> trace








---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AnyAgent`
Base abstract class for all agent implementations. 

This provides a unified interface for different agent frameworks. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(config: 'AgentConfig')
```






---

#### <kbd>property</kbd> agent

The underlying agent implementation from the framework. 

This property is intentionally restricted to maintain framework abstraction and prevent direct dependency on specific agent implementations. 

If you need functionality that relies on accessing the underlying agent: 1. Consider if the functionality can be added to the AnyAgent interface 2. Submit a GitHub issue describing your use case 3. Contribute a PR implementing the needed functionality 



**Raises:**
 
 - <b>`NotImplementedError`</b>:  Always raised when this property is accessed 

---

#### <kbd>property</kbd> framework

The Agent Framework used. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `cleanup_async`

```python
cleanup_async() → None
```

Clean up resources including MCP client connections. 

This should be called when you're done using the agent to ensure all resources are properly released. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create`

```python
create(
    agent_framework: 'AgentFramework | str',
    agent_config: 'AgentConfig'
) → AnyAgent
```

Create an agent using the given framework and config. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `create_async`

```python
create_async(
    agent_framework: 'AgentFramework | str',
    agent_config: 'AgentConfig'
) → AnyAgent
```

Create an agent using the given framework and config. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run`

```python
run(prompt: 'str', **kwargs: 'Any') → AgentTrace
```

Run the agent with the given prompt. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L191"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `run_async`

```python
run_async(prompt: 'str', **kwargs: 'Any') → AgentTrace
```

Run the agent asynchronously with the given prompt. 



**Args:**
 
 - <b>`prompt`</b>:  The user prompt to be passed to the agent. 


 - <b>`kwargs`</b>:  Will be passed to the underlying runner used  by the framework. 



**Returns:**
 The `AgentTrace` containing information about the  steps taken by the agent. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L322"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `serve_async`

```python
serve_async(
    serving_config: 'MCPServingConfig | A2AServingConfig | None' = None
) → ServerHandle
```

Serve this agent asynchronously using the protocol defined in the serving_config. 



**Args:**
 
 - <b>`serving_config`</b>:  Configuration for serving the agent. If None, uses default A2AServingConfig.  Must be an instance of A2AServingConfig or MCPServingConfig. 



**Returns:**
 A ServerHandle instance that provides methods for managing the server lifecycle. 



**Raises:**
 
 - <b>`ImportError`</b>:  If the `a2a` dependencies are not installed and an `A2AServingConfig` is used. 



**Example:**
 ```
    agent = await AnyAgent.create_async("tinyagent", AgentConfig(...))
    config = MCPServingConfig(port=8080)
    server_handle = await agent.serve_async(config)
    try:
         # Server is running
         await asyncio.sleep(10)
    finally:
         await server_handle.shutdown()
    ``` 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/frameworks/any_agent.py#L381"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_output_type_async`

```python
update_output_type_async(output_type: 'type[BaseModel] | None') → None
```

Update the output type of the agent in-place. 

This method allows updating the agent's output type without recreating the entire agent instance, which is more efficient than the current approach of recreating the agent. 



**Args:**
 
 - <b>`output_type`</b>:  The new output type to use, or None to remove output type constraint 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
