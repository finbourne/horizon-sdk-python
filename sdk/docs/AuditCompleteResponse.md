# AuditCompleteResponse

Response type for Horizon Audit Event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_name** | **str** | The name of the Process the events will be visible under | 
## Example

```python
from finbourne_horizon.models.audit_complete_response import AuditCompleteResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

process_name: StrictStr = "example_process_name"
audit_complete_response_instance = AuditCompleteResponse(process_name=process_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

