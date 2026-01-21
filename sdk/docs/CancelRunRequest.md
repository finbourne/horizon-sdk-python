# CancelRunRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_ids** | **List[str]** |  | 
**message** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.cancel_run_request import CancelRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_ids: List[StrictStr] = # Replace with your value
message: Optional[StrictStr] = "example_message"
cancel_run_request_instance = CancelRunRequest(run_ids=run_ids, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

