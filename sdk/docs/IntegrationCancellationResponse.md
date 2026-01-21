# IntegrationCancellationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **Dict[str, str]** |  | 
## Example

```python
from finbourne_horizon.models.integration_cancellation_response import IntegrationCancellationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

response: Dict[str, StrictStr]
integration_cancellation_response_instance = IntegrationCancellationResponse(response=response)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

