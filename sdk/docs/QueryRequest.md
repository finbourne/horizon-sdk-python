# QueryRequest

Used to control queries, including getting \"pages\" of data
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**QuerySpecification**](QuerySpecification.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.query_request import QueryRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel

specification: Optional[QuerySpecification] = None
query_request_instance = QueryRequest(specification=specification)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

