# TpfTransactionSearchResponse

TPF send history record
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction identifier | 
**instance_id** | **str** | Integration instance ID where the transaction was processed | 
**instance_name** | **str** | Integration instance name | 
**batch_id** | **str** | Unique identifier of the batch | 
**run_start_time** | **datetime** | Timestamp when the batch/run started | 
**publication_status** | **str** | Publication status of the transaction (Sent | Skipped | Failed) | 
**instrument_name** | **str** | Instrument name | 
**instrument_type** | **str** | Instrument type | 
**trade_date** | **datetime** | Trade date of the transaction | 
**settlement_date** | **datetime** | Settlement date of the transaction | [optional] 
**skip_reason** | **str** | Reason the transaction was skipped (if applicable) | [optional] 
**file_name** | **str** | Output file associated with the publication run | [optional] 
**destinations** | **List[str]** | Destinations to which the transaction was published | [optional] 
**portfolio_code** | **str** | PortfolioCode showing portfolio code | [optional] 
**portfolio_scope** | **str** | PortfolioScope displaying portfolio scope | [optional] 
**failure_reason** | **str** | FailureReason to show failure reason | [optional] 
**instrument_id** | **str** | InstrumentId showing instrument id of transaction | [optional] 
## Example

```python
from finbourne_horizon.models.tpf_transaction_search_response import TpfTransactionSearchResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_id: StrictStr = "example_transaction_id"
instance_id: StrictStr = "example_instance_id"
instance_name: StrictStr = "example_instance_name"
batch_id: StrictStr = "example_batch_id"
run_start_time: datetime = # Replace with your value
publication_status: StrictStr = "example_publication_status"
instrument_name: StrictStr = "example_instrument_name"
instrument_type: StrictStr = "example_instrument_type"
trade_date: datetime = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
skip_reason: Optional[StrictStr] = "example_skip_reason"
file_name: Optional[StrictStr] = "example_file_name"
destinations: Optional[List[StrictStr]] = # Replace with your value
portfolio_code: Optional[StrictStr] = "example_portfolio_code"
portfolio_scope: Optional[StrictStr] = "example_portfolio_scope"
failure_reason: Optional[StrictStr] = "example_failure_reason"
instrument_id: Optional[StrictStr] = "example_instrument_id"
tpf_transaction_search_response_instance = TpfTransactionSearchResponse(transaction_id=transaction_id, instance_id=instance_id, instance_name=instance_name, batch_id=batch_id, run_start_time=run_start_time, publication_status=publication_status, instrument_name=instrument_name, instrument_type=instrument_type, trade_date=trade_date, settlement_date=settlement_date, skip_reason=skip_reason, file_name=file_name, destinations=destinations, portfolio_code=portfolio_code, portfolio_scope=portfolio_scope, failure_reason=failure_reason, instrument_id=instrument_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

