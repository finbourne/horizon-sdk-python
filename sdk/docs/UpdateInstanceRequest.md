# UpdateInstanceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**integration_type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**enabled** | **bool** |  | 
**triggers** | [**List[Trigger]**](Trigger.md) |  | 
**details** | **object** |  | 
## Example

```python
from finbourne_horizon.models.update_instance_request import UpdateInstanceRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr, validator

id: StrictStr = "example_id"
integration_type: StrictStr = "example_integration_type"
name: StrictStr = "example_name"
description: StrictStr = "example_description"
enabled: StrictBool = # Replace with your value
enabled:StrictBool = True
triggers: conlist(Trigger) = # Replace with your value
details: Dict[str, Any] = # Replace with your value
update_instance_request_instance = UpdateInstanceRequest(id=id, integration_type=integration_type, name=name, description=description, enabled=enabled, triggers=triggers, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

