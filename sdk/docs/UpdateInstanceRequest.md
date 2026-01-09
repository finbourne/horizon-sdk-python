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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
integration_type: StrictStr = "example_integration_type"
name: StrictStr = "example_name"
description: StrictStr = "example_description"
enabled: StrictBool
enabled:StrictBool = True
triggers: List[Trigger]
details: Dict[str, Any]
update_instance_request_instance = UpdateInstanceRequest(id=id, integration_type=integration_type, name=name, description=description, enabled=enabled, triggers=triggers, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

