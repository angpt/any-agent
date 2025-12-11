<!-- markdownlint-disable -->

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/web_browsing.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `tools.web_browsing`





---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/web_browsing.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_web`

```python
search_web(query: str) → str
```

Perform a duckduckgo web search based on your query (think a Google search) then returns the top search results. 



**Args:**
 
 - <b>`query`</b> (str):  The search query to perform. 



**Returns:**
 The top search results. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/web_browsing.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `visit_webpage`

```python
visit_webpage(url: str, timeout: int = 30, max_length: int = 10000) → str
```

Visits a webpage at the given url and reads its content as a markdown string. Use this to browse webpages. 



**Args:**
 
 - <b>`url`</b>:  The url of the webpage to visit. 
 - <b>`timeout`</b>:  The timeout in seconds for the request. 
 - <b>`max_length`</b>:  The maximum number of characters of text that can be returned (default=10000).  If max_length==-1, text is not truncated and the full webpage is returned. 


---

<a href="https://github.com/angpt/any-agent/blob/3969d3db064c902c71a9553e859cf20c951a8658/src/any_agent/tools/web_browsing.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `search_tavily`

```python
search_tavily(query: str, include_images: bool = False) → str
```

Perform a Tavily web search based on your query and return the top search results. 

See https://blog.tavily.com/getting-started-with-the-tavily-search-api for more information. 



**Args:**
 
 - <b>`query`</b> (str):  The search query to perform. 
 - <b>`include_images`</b> (bool):  Whether to include images in the results. 



**Returns:**
 The top search results as a formatted string. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
