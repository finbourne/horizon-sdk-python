# ReplayTransactionsResponse

Response from a replay transactions operation. For DryRun, Finbourne.Horizon.Integrations.Web.Dto.Integrations.TradePublicationFramework.Response.ReplayTransactionsResponse.PayloadOutput carries the preview payload in the instance's configured output format (CSV or XML); for Committed it is empty.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_reference_id** | **str** |  | 
**mode** | **str** |  | 
**transaction_count** | **int** |  | 
**payload_output** | **str** |  | 
**message** | **str** |  | 
## Example

```python
from finbourne_horizon.models.replay_transactions_response import ReplayTransactionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

batch_reference_id: StrictStr = "example_batch_reference_id"
mode: StrictStr = "example_mode"
transaction_count: StrictInt = # Replace with your value
transaction_count: StrictInt = 42
payload_output: StrictStr = "example_payload_output"
message: StrictStr = "example_message"
replay_transactions_response_instance = ReplayTransactionsResponse(batch_reference_id=batch_reference_id, mode=mode, transaction_count=transaction_count, payload_output=payload_output, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

