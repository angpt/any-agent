<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tracing.otel_types`






---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SpanKind`
String-based enum for span kind to make it serializable. 





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TraceFlags`
Serializable trace flags. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(flags: Any | None) → TraceFlags
```

Convert from OpenTelemetry TraceFlags. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TraceState`
Serializable trace state. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(state: Any | None) → TraceState
```

Convert from OpenTelemetry TraceState. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SpanContext`
Serializable span context. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(context: Any | None) → SpanContext
```

Convert from OpenTelemetry SpanContext. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `StatusCode`
String-based enum for status code to make it serializable. 





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Status`
Serializable status. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(status: Any | None) → Status
```

Convert from OpenTelemetry Status. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AttributeValue`
A wrapper for attribute values that can be serialized. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 




---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Link`
Serializable link. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L132"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(link: Any | None) → Link
```

Convert from OpenTelemetry Link. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Event`
Serializable event. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(event: Any | None) → Event
```

Convert from OpenTelemetry Event. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Resource`
Serializable resource. 


---

#### <kbd>property</kbd> model_extra

Get extra fields set during validation. 



**Returns:**
  A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. 

---

#### <kbd>property</kbd> model_fields_set

Returns the set of fields that have been explicitly set on this model instance. 



**Returns:**
  A set of strings representing the fields that have been set,  i.e. that were not filled from defaults. 



---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tracing/otel_types.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_otel`

```python
from_otel(resource: Any | None) → Resource
```

Convert from OpenTelemetry Resource. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
