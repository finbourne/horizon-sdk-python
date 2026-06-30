# TpfRetryFailedDeliveryRequest

Request to retry failed deliveries for multiple batch elements. The integration instance identifier is supplied via the route, not the body.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_element_reference_ids** | **List[str]** | Batch element reference identifiers to retry. No regex pattern is required as batch element IDs are vendor-defined strings with varying formats. | 
## Example

```python
from finbourne_horizon.models.tpf_retry_failed_delivery_request import TpfRetryFailedDeliveryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

batch_element_reference_ids: List[StrictStr] = # Replace with your value
tpf_retry_failed_delivery_request_instance = TpfRetryFailedDeliveryRequest(batch_element_reference_ids=batch_element_reference_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

