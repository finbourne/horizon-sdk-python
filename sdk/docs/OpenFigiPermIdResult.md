# OpenFigiPermIdResult

A packed WebAPI OpenFigi DTO and PermId DTO
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_figi_result** | [**OpenFigiData**](OpenFigiData.md) |  | 
**perm_id_result** | [**PermIdData**](PermIdData.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.open_figi_perm_id_result import OpenFigiPermIdResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

open_figi_result: OpenFigiData = # Replace with your value
perm_id_result: Optional[PermIdData] = # Replace with your value
open_figi_perm_id_result_instance = OpenFigiPermIdResult(open_figi_result=open_figi_result, perm_id_result=perm_id_result)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

