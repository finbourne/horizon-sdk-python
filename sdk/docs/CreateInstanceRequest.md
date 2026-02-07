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
**post_process_tasks** | [**List[PostProcessTask]**](PostProcessTask.md) |  | 
## Example

```python
from finbourne_horizon.models.create_instance_request import CreateInstanceRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instance_optional_props: Optional[Dict[str, LusidPropertyDefinitionOverridesByType]] = # Replace with your value
integration_type: StrictStr = "example_integration_type"
name: StrictStr = "example_name"
description: StrictStr = "example_description"
enabled: StrictBool
enabled:StrictBool = True
triggers: List[Trigger]
details: Dict[str, Any]
post_process_tasks: List[PostProcessTask] = # Replace with your value
create_instance_request_instance = CreateInstanceRequest(instance_optional_props=instance_optional_props, integration_type=integration_type, name=name, description=description, enabled=enabled, triggers=triggers, details=details, post_process_tasks=post_process_tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

