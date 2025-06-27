# IIntegrationLogResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **int** |  | [readonly] 
**run_id** | **str** |  | [optional] [readonly] 
**parent_log_id** | **int** |  | [optional] [readonly] 
**log_type** | **str** |  | [readonly] 
**first_activity** | **datetime** |  | [optional] [readonly] 
**last_activity** | **datetime** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**source_record** | [**IntegrationLogRecord**](IntegrationLogRecord.md) |  | [optional] 
**target_record** | [**IntegrationLogTargetRecord**](IntegrationLogTargetRecord.md) |  | [optional] 
**activities** | [**List[IntegrationLogActivity]**](IntegrationLogActivity.md) |  | [readonly] 
## Example

```python
from finbourne_horizon.models.i_integration_log_response import IIntegrationLogResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
log_id: StrictInt = # Replace with your value
run_id: Optional[StrictStr] = "example_run_id"
parent_log_id: Optional[StrictInt] = # Replace with your value
log_type: StrictStr = "example_log_type"
first_activity: Optional[datetime] = # Replace with your value
last_activity: Optional[datetime] = # Replace with your value
status: Optional[StrictStr] = "example_status"
source_record: Optional[IntegrationLogRecord] = # Replace with your value
target_record: Optional[IntegrationLogTargetRecord] = # Replace with your value
activities: conlist(IntegrationLogActivity) = # Replace with your value
i_integration_log_response_instance = IIntegrationLogResponse(log_id=log_id, run_id=run_id, parent_log_id=parent_log_id, log_type=log_type, first_activity=first_activity, last_activity=last_activity, status=status, source_record=source_record, target_record=target_record, activities=activities)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

