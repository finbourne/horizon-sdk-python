# TpfFailedDeliveryResponse

Response for bulk retry operation of failed deliveries
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted** | **int** | Number of batch elements submitted for retry | 
**results** | [**List[TpfRetryElementResult]**](TpfRetryElementResult.md) | Per-element retry results | 
## Example

```python
from finbourne_horizon.models.tpf_failed_delivery_response import TpfFailedDeliveryResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

submitted: StrictInt = # Replace with your value
submitted: StrictInt = 42
results: List[TpfRetryElementResult] = # Replace with your value
tpf_failed_delivery_response_instance = TpfFailedDeliveryResponse(submitted=submitted, results=results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

