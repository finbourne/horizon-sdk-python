# IntegrationRerunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**InstanceExecutionReferenceId**](InstanceExecutionReferenceId.md) |  | 
## Example

```python
from finbourne_horizon.models.integration_rerun_response import IntegrationRerunResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: InstanceExecutionReferenceId = # Replace with your value
integration_rerun_response_instance = IntegrationRerunResponse(run_id=run_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

