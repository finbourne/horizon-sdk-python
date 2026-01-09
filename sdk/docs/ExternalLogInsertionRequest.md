# ExternalLogInsertionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[ExternalLogRecord]**](ExternalLogRecord.md) |  | 
## Example

```python
from finbourne_horizon.models.external_log_insertion_request import ExternalLogInsertionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

logs: List[ExternalLogRecord]
external_log_insertion_request_instance = ExternalLogInsertionRequest(logs=logs)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

