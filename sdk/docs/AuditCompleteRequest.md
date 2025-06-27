# AuditCompleteRequest

An incoming request for a Horizon Complete Event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID identifiying the source of the event | 
**user_id** | **str** | A unique ID identifiying who owns the schedule | 
**scheduler_run_id** | **str** | The GUID of the schedule run | 
**start_time** | **datetime** | When the run was started in UTC | 
**end_time** | **datetime** | When the run finished in UTC | 
**message** | **str** | A descriptive message to accompany the status | 
**status** | [**AuditCompleteStatus**](AuditCompleteStatus.md) |  | 
**rows_total** | **int** | The number of data rows operated on | 
**rows_succeeded** | **int** | The number of data rows successfully operated on | 
**rows_failed** | **int** | The number of data rows that failed to be operated on | 
**rows_ignored** | **int** | The number of data rows that had no actions taken | 
**audit_files** | [**List[AuditFileDetails]**](AuditFileDetails.md) | A list of file details for attaching to the event | 
**process_name_override** | **str** | Optional Name for how the process appears in Data Feed Monitoring | [optional] 
## Example

```python
from finbourne_horizon.models.audit_complete_request import AuditCompleteRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, conlist, constr
from datetime import datetime
id: StrictStr = "example_id"
user_id: StrictStr = "example_user_id"
scheduler_run_id: StrictStr = "example_scheduler_run_id"
start_time: datetime = # Replace with your value
end_time: datetime = # Replace with your value
message: StrictStr = "example_message"
status: AuditCompleteStatus = # Replace with your value
rows_total: StrictInt = # Replace with your value
rows_total: StrictInt = 42
rows_succeeded: StrictInt = # Replace with your value
rows_succeeded: StrictInt = 42
rows_failed: StrictInt = # Replace with your value
rows_failed: StrictInt = 42
rows_ignored: StrictInt = # Replace with your value
rows_ignored: StrictInt = 42
audit_files: conlist(AuditFileDetails) = # Replace with your value
process_name_override: Optional[StrictStr] = "example_process_name_override"
audit_complete_request_instance = AuditCompleteRequest(id=id, user_id=user_id, scheduler_run_id=scheduler_run_id, start_time=start_time, end_time=end_time, message=message, status=status, rows_total=rows_total, rows_succeeded=rows_succeeded, rows_failed=rows_failed, rows_ignored=rows_ignored, audit_files=audit_files, process_name_override=process_name_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

