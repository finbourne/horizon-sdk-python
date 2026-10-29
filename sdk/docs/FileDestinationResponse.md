# FileDestinationResponse

The destination a file delivery row describes. A Failed row carries the per-transaction FailureReason when one was recorded, falling back to the raw Error text.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**path** | **str** |  | 
**status** | **str** |  | 
**error** | **str** |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**name** | **str** | The configured destination name, such as the SFTP host, when one was recorded. | [optional] 
**delivered_at** | **datetime** | When the file reached the destination; null for a Failed or Pending row. | [optional] 
## Example

```python
from finbourne_horizon.models.file_destination_response import FileDestinationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
path: StrictStr = "example_path"
status: StrictStr = "example_status"
error: Optional[StrictStr] = "example_error"
failure_reason: Optional[StrictStr] = "example_failure_reason"
name: Optional[StrictStr] = "example_name"
delivered_at: Optional[datetime] = # Replace with your value
file_destination_response_instance = FileDestinationResponse(type=type, path=path, status=status, error=error, failure_reason=failure_reason, name=name, delivered_at=delivered_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

