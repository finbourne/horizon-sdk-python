# UpdateInstanceResponse

The outcome of updating an instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[ValidationNoticeResponse]**](ValidationNoticeResponse.md) | Non-blocking findings about the saved configuration. Empty when there are none. | [optional] 
## Example

```python
from finbourne_horizon.models.update_instance_response import UpdateInstanceResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

warnings: Optional[List[ValidationNoticeResponse]] = # Replace with your value
update_instance_response_instance = UpdateInstanceResponse(warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

