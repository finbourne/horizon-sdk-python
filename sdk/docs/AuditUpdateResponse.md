# AuditUpdateResponse

Response type for Horizon Audit Event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_name** | **str** | The name of the Process the events will be visible under | 
## Example

```python
from finbourne_horizon.models.audit_update_response import AuditUpdateResponse
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

process_name: StrictStr = "example_process_name"
audit_update_response_instance = AuditUpdateResponse(process_name=process_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

