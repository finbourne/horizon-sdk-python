# TransactionPayloadResponse

record containing details of a transaction payload.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** |  | 
**values** | **Dict[str, str]** |  | 
**raw_csv_row** | **str** |  | 
## Example

```python
from finbourne_horizon.models.transaction_payload_response import TransactionPayloadResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

columns: List[StrictStr]
values: Dict[str, StrictStr]
raw_csv_row: StrictStr = "example_raw_csv_row"
transaction_payload_response_instance = TransactionPayloadResponse(columns=columns, values=values, raw_csv_row=raw_csv_row)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

