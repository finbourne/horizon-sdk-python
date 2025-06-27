# QuerySpecification

Defines the information that can be used to query a set of data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of results to be returned in a \&quot;page\&quot; | [optional] 
## Example

```python
from finbourne_horizon.models.query_specification import QuerySpecification
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt

limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
query_specification_instance = QuerySpecification(limit=limit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

