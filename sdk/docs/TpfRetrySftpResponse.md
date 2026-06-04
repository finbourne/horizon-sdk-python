# TpfRetrySftpResponse

Response from retrying SFTP file delivery
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the retry was successful | 
**message** | **str** | Status message describing the result | 
**new_file_delivery_id** | **int** | ID of the new file delivery record created for this retry (if successful) | [optional] 
**retried_at** | **datetime** | Timestamp when the retry was executed | [optional] 
**original_file** | [**TpfFileDeliveryInfo**](TpfFileDeliveryInfo.md) |  | [optional] 
**duplicate_file** | [**TpfFileDeliveryInfo**](TpfFileDeliveryInfo.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.tpf_retry_sftp_response import TpfRetrySftpResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

success: StrictBool = # Replace with your value
success:StrictBool = True
message: StrictStr = "example_message"
new_file_delivery_id: Optional[StrictInt] = # Replace with your value
retried_at: Optional[datetime] = # Replace with your value
original_file: Optional[TpfFileDeliveryInfo] = # Replace with your value
duplicate_file: Optional[TpfFileDeliveryInfo] = # Replace with your value
tpf_retry_sftp_response_instance = TpfRetrySftpResponse(success=success, message=message, new_file_delivery_id=new_file_delivery_id, retried_at=retried_at, original_file=original_file, duplicate_file=duplicate_file)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

