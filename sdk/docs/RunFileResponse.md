# RunFileResponse

One delivery of a file to one destination within a run, keyed by FileUuid. A file sent to two destinations appears as two rows, so Destinations always holds exactly one element.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**generated_at** | **datetime** | When the file was built, or when the attempt failed before a file was built. | 
**row_count** | **int** |  | 
**file_hash** | **str** |  | 
**encrypted** | **bool** |  | 
**destinations** | [**List[FileDestinationResponse]**](FileDestinationResponse.md) |  | 
**transaction_ids** | **List[str]** |  | 
**file_uuid** | **str** |  | 
**failed_transaction_ids** | **List[str]** |  | 
**can_resend** | **bool** | Whether the data the file is rebuilt from is still retained, so a resend can be requested. | 
## Example

```python
from finbourne_horizon.models.run_file_response import RunFileResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

file_name: StrictStr = "example_file_name"
generated_at: datetime = # Replace with your value
row_count: StrictInt = # Replace with your value
row_count: StrictInt = 42
file_hash: StrictStr = "example_file_hash"
encrypted: StrictBool
encrypted:StrictBool = True
destinations: List[FileDestinationResponse]
transaction_ids: List[StrictStr] = # Replace with your value
file_uuid: StrictStr = "example_file_uuid"
failed_transaction_ids: List[StrictStr] = # Replace with your value
can_resend: StrictBool = # Replace with your value
can_resend:StrictBool = True
run_file_response_instance = RunFileResponse(file_name=file_name, generated_at=generated_at, row_count=row_count, file_hash=file_hash, encrypted=encrypted, destinations=destinations, transaction_ids=transaction_ids, file_uuid=file_uuid, failed_transaction_ids=failed_transaction_ids, can_resend=can_resend)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

