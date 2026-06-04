# TpfFileDeliveryInfo

Information about a file delivery
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File delivery ID | 
**file_name** | **str** | File name | 
**file_hash** | **str** | SHA-256 hash of the file content | 
**destination_path** | **str** | SFTP destination path | 
**status** | **str** | Delivery status | 
**generated_at** | **datetime** | Timestamp when the file was originally generated | 
## Example

```python
from finbourne_horizon.models.tpf_file_delivery_info import TpfFileDeliveryInfo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictInt = # Replace with your value
file_name: StrictStr = "example_file_name"
file_hash: StrictStr = "example_file_hash"
destination_path: StrictStr = "example_destination_path"
status: StrictStr = "example_status"
generated_at: datetime = # Replace with your value
tpf_file_delivery_info_instance = TpfFileDeliveryInfo(id=id, file_name=file_name, file_hash=file_hash, destination_path=destination_path, status=status, generated_at=generated_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

