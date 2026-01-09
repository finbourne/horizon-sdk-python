# AuditUpdateRequest

An incoming request for a Horizon Update Event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID identifiying the source of the event | 
**user_id** | **str** | A unique ID identifiying who owns the schedule | 
**scheduler_run_id** | **str** | The GUID of the schedule run | 
**start_time** | **datetime** | When the run was started in UTC | 
**message** | **str** | A descriptive message to accompany the status | 
**process_name_override** | **str** | Optional Name for how the process appears in Data Feed Monitoring | [optional] 
## Example

```python
from finbourne_horizon.models.audit_update_request import AuditUpdateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
user_id: StrictStr = "example_user_id"
scheduler_run_id: StrictStr = "example_scheduler_run_id"
start_time: datetime = # Replace with your value
message: StrictStr = "example_message"
process_name_override: Optional[StrictStr] = "example_process_name_override"
audit_update_request_instance = AuditUpdateRequest(id=id, user_id=user_id, scheduler_run_id=scheduler_run_id, start_time=start_time, message=message, process_name_override=process_name_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

