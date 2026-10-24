# ValidationNoticeResponse

A non-blocking finding raised when an instance was saved. The save succeeded regardless.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | \&quot;Warning\&quot; or \&quot;Information\&quot;. | 
**field** | **str** | The configuration field the finding relates to. | 
**message** | **str** | What was found. | 
## Example

```python
from finbourne_horizon.models.validation_notice_response import ValidationNoticeResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

severity: StrictStr = "example_severity"
field: StrictStr = "example_field"
message: StrictStr = "example_message"
validation_notice_response_instance = ValidationNoticeResponse(severity=severity, field=field, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

