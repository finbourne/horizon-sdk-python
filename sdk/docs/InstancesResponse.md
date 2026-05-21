# InstancesResponse

record containing a list of instances.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[InstanceResponse]**](InstanceResponse.md) |  | 
## Example

```python
from finbourne_horizon.models.instances_response import InstancesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instances: List[InstanceResponse]
instances_response_instance = InstancesResponse(instances=instances)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

