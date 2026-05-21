# TransactionResponse

Response containing details of a single transaction for a run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | 
**publication_status** | **str** |  | 
**portfolio_scope** | **str** |  | [optional] 
**portfolio_code** | **str** |  | [optional] 
**instrument_id** | **str** |  | 
**instrument_type** | **str** |  | 
**instrument_name** | **str** |  | 
**trade_date** | **datetime** |  | 
**settlement_date** | **datetime** |  | 
**status** | **str** |  | 
**skip_reason** | **str** |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**output_file_name** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**destinations** | [**List[DestinationResponse]**](DestinationResponse.md) |  | 
## Example

```python
from finbourne_horizon.models.transaction_response import TransactionResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_id: StrictStr = "example_transaction_id"
publication_status: StrictStr = "example_publication_status"
portfolio_scope: Optional[StrictStr] = "example_portfolio_scope"
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
instrument_id: StrictStr = "example_instrument_id"
instrument_type: StrictStr = "example_instrument_type"
instrument_name: StrictStr = "example_instrument_name"
trade_date: datetime = # Replace with your value
settlement_date: datetime = # Replace with your value
status: StrictStr = "example_status"
skip_reason: Optional[StrictStr] = "example_skip_reason"
failure_reason: Optional[StrictStr] = "example_failure_reason"
output_file_name: Optional[StrictStr] = "example_output_file_name"
sent_at: Optional[datetime] = # Replace with your value
destinations: List[DestinationResponse]
transaction_response_instance = TransactionResponse(transaction_id=transaction_id, publication_status=publication_status, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, instrument_id=instrument_id, instrument_type=instrument_type, instrument_name=instrument_name, trade_date=trade_date, settlement_date=settlement_date, status=status, skip_reason=skip_reason, failure_reason=failure_reason, output_file_name=output_file_name, sent_at=sent_at, destinations=destinations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

