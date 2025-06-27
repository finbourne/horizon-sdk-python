# CreateInstanceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_optional_props** | [**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md) |  | [optional] 
**integration_type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**enabled** | **bool** |  | 
**triggers** | [**List[Trigger]**](Trigger.md) |  | 
**details** | **object** |  | 
## Example

```python
from finbourne_horizon.models.create_instance_request import CreateInstanceRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr, validator

instance_optional_props: Optional[Dict[str, LusidPropertyDefinitionOverridesByType]] = # Replace with your value
integration_type: StrictStr = "example_integration_type"
name: StrictStr = "example_name"
description: StrictStr = "example_description"
enabled: StrictBool = # Replace with your value
enabled:StrictBool = True
triggers: conlist(Trigger) = # Replace with your value
details: Dict[str, Any] = # Replace with your value
create_instance_request_instance = CreateInstanceRequest(instance_optional_props=instance_optional_props, integration_type=integration_type, name=name, description=description, enabled=enabled, triggers=triggers, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

