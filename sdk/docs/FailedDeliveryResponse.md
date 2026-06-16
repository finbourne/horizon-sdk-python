# FailedDeliveryResponse

A batch's failed deliveries returned by the list endpoint, aggregated to one row per batch. Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.FailedDeliveryResponse.FailedCount is the number of failed deliveries in the batch and Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.FailedDeliveryResponse.FailureReason is the comma-separated set of their failure reasons.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_reference_id** | **str** |  | 
**run_id** | **str** |  | 
**run_start_time** | **datetime** |  | 
**failed_count** | **int** |  | 
**failure_reason** | **str** |  | 
**last_attempt_at** | **datetime** |  | 
**attempt_count** | **int** |  | 
**resolved** | **bool** |  | 
**resolved_at** | **datetime** |  | [optional] 
**resolution_reason** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.failed_delivery_response import FailedDeliveryResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

batch_reference_id: StrictStr = "example_batch_reference_id"
run_id: StrictStr = "example_run_id"
run_start_time: datetime = # Replace with your value
failed_count: StrictInt = # Replace with your value
failed_count: StrictInt = 42
failure_reason: StrictStr = "example_failure_reason"
last_attempt_at: datetime = # Replace with your value
attempt_count: StrictInt = # Replace with your value
attempt_count: StrictInt = 42
resolved: StrictBool
resolved:StrictBool = True
resolved_at: Optional[datetime] = # Replace with your value
resolution_reason: Optional[StrictStr] = "example_resolution_reason"
failed_delivery_response_instance = FailedDeliveryResponse(batch_reference_id=batch_reference_id, run_id=run_id, run_start_time=run_start_time, failed_count=failed_count, failure_reason=failure_reason, last_attempt_at=last_attempt_at, attempt_count=attempt_count, resolved=resolved, resolved_at=resolved_at, resolution_reason=resolution_reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

