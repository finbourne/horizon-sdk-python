# ReplayTransactionsRequest

Request to replay one or more transactions through a TPF instance. The instance ID is specified in the route path.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** | List of transaction IDs to replay. | 
**mode** | **str** | Replay mode - DryRun (preview only) or Committed (real send). | 
**destinations** | **List[str]** | Target destinations for Committed mode. Required for Committed, forbidden for DryRun. Valid values: Drive, Sftp, S3, Local | [optional] 
**options** | [**ReplayOptions**](ReplayOptions.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.replay_transactions_request import ReplayTransactionsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_ids: List[StrictStr] = # Replace with your value
mode: StrictStr = "example_mode"
destinations: Optional[List[StrictStr]] = # Replace with your value
options: Optional[ReplayOptions] = None
replay_transactions_request_instance = ReplayTransactionsRequest(transaction_ids=transaction_ids, mode=mode, destinations=destinations, options=options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

