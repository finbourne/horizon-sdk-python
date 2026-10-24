# InstanceRunResponse

Response containing details of a single run for an instance. The transaction and file figures describe the batch as it stands now, so they are reported on the latest attempt only and are null on earlier attempts of a retried run. Message explains a failed attempt and what will happen or must be done next; it is null for completed, running and queued attempts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**reference_id** | **str** |  | 
**attempt** | **int** |  | [optional] 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | [optional] 
**duration** | **str** |  | [optional] 
**status** | **str** |  | 
**triggered_by** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**sent_count** | **int** |  | [optional] 
**skipped_count** | **int** |  | [optional] 
**failed_count** | **int** |  | [optional] 
**failed_files** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.instance_run_response import InstanceRunResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
reference_id: StrictStr = "example_reference_id"
attempt: Optional[StrictInt] = None
attempt: Optional[StrictInt] = None
start_time: datetime = # Replace with your value
end_time: Optional[datetime] = # Replace with your value
duration: Optional[StrictStr] = "example_duration"
status: StrictStr = "example_status"
triggered_by: Optional[StrictStr] = "example_triggered_by"
total: Optional[StrictInt] = None
total: Optional[StrictInt] = None
sent_count: Optional[StrictInt] = # Replace with your value
skipped_count: Optional[StrictInt] = # Replace with your value
failed_count: Optional[StrictInt] = # Replace with your value
failed_files: Optional[StrictInt] = # Replace with your value
failed_files: Optional[StrictInt] = None
message: Optional[StrictStr] = "example_message"
instance_run_response_instance = InstanceRunResponse(run_id=run_id, reference_id=reference_id, attempt=attempt, start_time=start_time, end_time=end_time, duration=duration, status=status, triggered_by=triggered_by, total=total, sent_count=sent_count, skipped_count=skipped_count, failed_count=failed_count, failed_files=failed_files, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

