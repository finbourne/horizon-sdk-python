# InstanceRunResponse

Response containing details of a single run for an instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**batch_reference_id** | **str** |  | [optional] 
**attempt** | **int** |  | [optional] 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | [optional] 
**duration** | **str** |  | [optional] 
**status** | **str** |  | 
**triggered_by** | **str** |  | [optional] 
**total** | **int** |  | 
**sent_count** | **int** |  | 
**skipped_count** | **int** |  | 
**failed_count** | **int** |  | 
**failed_files** | **int** |  | 
## Example

```python
from finbourne_horizon.models.instance_run_response import InstanceRunResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
batch_reference_id: Optional[StrictStr] = "example_batch_reference_id"
attempt: Optional[StrictInt] = None
attempt: Optional[StrictInt] = None
start_time: datetime = # Replace with your value
end_time: Optional[datetime] = # Replace with your value
duration: Optional[StrictStr] = "example_duration"
status: StrictStr = "example_status"
triggered_by: Optional[StrictStr] = "example_triggered_by"
total: StrictInt
total: StrictInt = 42
sent_count: StrictInt = # Replace with your value
skipped_count: StrictInt = # Replace with your value
failed_count: StrictInt = # Replace with your value
failed_files: StrictInt = # Replace with your value
failed_files: StrictInt = 42
instance_run_response_instance = InstanceRunResponse(run_id=run_id, batch_reference_id=batch_reference_id, attempt=attempt, start_time=start_time, end_time=end_time, duration=duration, status=status, triggered_by=triggered_by, total=total, sent_count=sent_count, skipped_count=skipped_count, failed_count=failed_count, failed_files=failed_files)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

