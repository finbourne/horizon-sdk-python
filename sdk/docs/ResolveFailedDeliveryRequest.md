# ResolveFailedDeliveryRequest

Request to resolve a failed delivery without retry.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for resolving the failed delivery without retrying. | 
## Example

```python
from finbourne_horizon.models.resolve_failed_delivery_request import ResolveFailedDeliveryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

reason: StrictStr = "example_reason"
resolve_failed_delivery_request_instance = ResolveFailedDeliveryRequest(reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

