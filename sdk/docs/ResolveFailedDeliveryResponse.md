# ResolveFailedDeliveryResponse

Response from resolving the failed deliveries for a batch without retry. Resolution is batch-level, so Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.ResolveFailedDeliveryResponse.ResolvedCount is the number of failed deliveries marked resolved.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_reference_id** | **str** |  | 
**resolved_count** | **int** |  | 
**resolved** | **bool** |  | 
**resolved_at** | **datetime** |  | 
**resolution_reason** | **str** |  | 
**message** | **str** |  | 
## Example

```python
from finbourne_horizon.models.resolve_failed_delivery_response import ResolveFailedDeliveryResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

batch_reference_id: StrictStr = "example_batch_reference_id"
resolved_count: StrictInt = # Replace with your value
resolved_count: StrictInt = 42
resolved: StrictBool
resolved:StrictBool = True
resolved_at: datetime = # Replace with your value
resolution_reason: StrictStr = "example_resolution_reason"
message: StrictStr = "example_message"
resolve_failed_delivery_response_instance = ResolveFailedDeliveryResponse(batch_reference_id=batch_reference_id, resolved_count=resolved_count, resolved=resolved, resolved_at=resolved_at, resolution_reason=resolution_reason, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

