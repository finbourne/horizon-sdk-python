# ExternalLogInsertionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[ExternalLogRecord]**](ExternalLogRecord.md) |  | 
## Example

```python
from finbourne_horizon.models.external_log_insertion_request import ExternalLogInsertionRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

logs: conlist(ExternalLogRecord) = # Replace with your value
external_log_insertion_request_instance = ExternalLogInsertionRequest(logs=logs)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

