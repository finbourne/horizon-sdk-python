# TransactionPayload

record containing the payload for a single transaction. Columns is compiled once from the TPF instance configuration and is identical across every item in the paginated result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**columns** | **List[str]** |  | 
**values** | **Dict[str, str]** |  | 
**raw_csv_row** | **str** |  | 
## Example

```python
from finbourne_horizon.models.transaction_payload import TransactionPayload
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_id: StrictStr = "example_transaction_id"
columns: List[StrictStr]
values: Dict[str, StrictStr]
raw_csv_row: StrictStr = "example_raw_csv_row"
transaction_payload_instance = TransactionPayload(transaction_id=transaction_id, columns=columns, values=values, raw_csv_row=raw_csv_row)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

