# IntegrationLogActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**resulting_status** | **str** |  | 
**message_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.integration_log_activity import IntegrationLogActivity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

timestamp: datetime
resulting_status: StrictStr = "example_resulting_status"
message_type: Optional[StrictStr] = "example_message_type"
description: Optional[StrictStr] = "example_description"
integration_log_activity_instance = IntegrationLogActivity(timestamp=timestamp, resulting_status=resulting_status, message_type=message_type, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

