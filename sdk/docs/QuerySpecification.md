# QuerySpecification

Defines the information that can be used to query a set of data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of results to be returned in a \&quot;page\&quot; | [optional] 
## Example

```python
from finbourne_horizon.models.query_specification import QuerySpecification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
query_specification_instance = QuerySpecification(limit=limit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

