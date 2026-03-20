# UpdateInstanceRequest

A request to update an existing integration instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Instance identifier | 
**integration_type** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**enabled** | **bool** |  | 
**triggers** | [**List[Trigger]**](Trigger.md) |  | 
**details** | **object** | Base DTO type of an integration configuration specific to the integration type.              N.B. ASP.NET Core model validation is normally applied automatically when [ApiController] is added to a controller, however it doesn&#39;t work here with the polymorphic integration subtypes of this class (see https://github.com/dotnet/aspnetcore/issues/27882). The workaround here is to implement the IValidatableObject interface and each subtype must call Validate() or ValidateContents() on its properties (the validation is not recursive).  Located in Horizon.Integrations.Web so both specific integration projects and Horizon.WebApi can reference it. | 
**post_process_tasks** | [**List[PostProcessTask]**](PostProcessTask.md) |  | 
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
details: Dict[str, Any] = # Replace with your value
post_process_tasks: List[PostProcessTask] = # Replace with your value
update_instance_request_instance = UpdateInstanceRequest(id=id, integration_type=integration_type, name=name, description=description, enabled=enabled, triggers=triggers, details=details, post_process_tasks=post_process_tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

