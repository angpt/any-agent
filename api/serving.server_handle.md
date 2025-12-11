<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/server_handle.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `serving.server_handle`




**Global Variables**
---------------
- **TYPE_CHECKING**


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/server_handle.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ServerHandle`
A handle for managing an async server instance. 

This class provides a clean interface for managing the lifecycle of a server without requiring manual management of the underlying task and server objects. 

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(task: 'Task[Any]', server: 'UvicornServer') → None
```






---

#### <kbd>property</kbd> port

Get the port the server is running on. 

If the server port was specified as 0, the port will be the one assigned by the OS. This helper method is useful to get the actual port that the server is running on. 



**Returns:**
  The port number the server is running on. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/server_handle.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_running`

```python
is_running() → bool
```

Check if the server is still running. 



**Returns:**
  True if the server task is still running, False otherwise. 

---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/serving/server_handle.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `shutdown`

```python
shutdown(timeout_seconds: 'float' = 10.0) → None
```

Gracefully shutdown the server with a timeout. 



**Args:**
 
 - <b>`timeout_seconds`</b>:  Maximum time to wait for graceful shutdown before forcing cancellation. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
