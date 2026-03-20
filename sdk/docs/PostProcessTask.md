# PostProcessTask

Request defining a post-processing task for an instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The type of action to perform (Allowed: RunIntegration, RunWorkflow, TriggerEmail) | 
**target_instance** | **str** | The instance identifier to trigger (for TriggerIntegration action). | [optional] 
**trigger_on** | **str** | When the task should be triggered (Allowed: OnSuccess, OnFailure, Always) | 
**parameters** | **object** | JSON parameters specific to the action type. | [optional] 
## Example

```python
from finbourne_horizon.models.post_process_task import PostProcessTask
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

action: StrictStr = "example_action"
target_instance: Optional[StrictStr] = "example_target_instance"
trigger_on: StrictStr = "example_trigger_on"
parameters: Optional[Any] = # Replace with your value
post_process_task_instance = PostProcessTask(action=action, target_instance=target_instance, trigger_on=trigger_on, parameters=parameters)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

