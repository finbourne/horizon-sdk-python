# ResourceId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
## Example

```python
from finbourne_horizon.models.resource_id import ResourceId
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
resource_id_instance = ResourceId(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

