# InstanceIdentifier

Identifies a single instance of an integration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Instance identifier. | 
## Example

```python
from finbourne_horizon.models.instance_identifier import InstanceIdentifier
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

id: StrictStr = "example_id"
instance_identifier_instance = InstanceIdentifier(id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

