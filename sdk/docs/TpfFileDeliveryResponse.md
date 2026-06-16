# TpfFileDeliveryResponse

Response model for TPF file delivery search results
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | [optional] 
**run_start_time** | **datetime** |  | [optional] 
**file_name** | **str** |  | 
**generated_at** | **datetime** |  | 
**row_count** | **int** |  | 
**file_hash** | **str** |  | [optional] 
**destination_type** | **str** |  | 
**destination_path** | **str** |  | [optional] 
**destination_status** | **str** |  | 
**destination_error** | **str** |  | [optional] 
**destination_name** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.tpf_file_delivery_response import TpfFileDeliveryResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: Optional[StrictStr] = "example_run_id"
run_start_time: Optional[datetime] = # Replace with your value
file_name: StrictStr = "example_file_name"
generated_at: datetime = # Replace with your value
row_count: StrictInt = # Replace with your value
row_count: StrictInt = 42
file_hash: Optional[StrictStr] = "example_file_hash"
destination_type: StrictStr = "example_destination_type"
destination_path: Optional[StrictStr] = "example_destination_path"
destination_status: StrictStr = "example_destination_status"
destination_error: Optional[StrictStr] = "example_destination_error"
destination_name: Optional[StrictStr] = "example_destination_name"
tpf_file_delivery_response_instance = TpfFileDeliveryResponse(run_id=run_id, run_start_time=run_start_time, file_name=file_name, generated_at=generated_at, row_count=row_count, file_hash=file_hash, destination_type=destination_type, destination_path=destination_path, destination_status=destination_status, destination_error=destination_error, destination_name=destination_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

