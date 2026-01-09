# QueryRequest

Used to control queries, including getting \"pages\" of data
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**QuerySpecification**](QuerySpecification.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.query_request import QueryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

specification: Optional[QuerySpecification] = None
query_request_instance = QueryRequest(specification=specification)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

