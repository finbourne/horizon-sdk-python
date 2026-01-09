# OpenFigiSearchResult

Response coming back from a search request to OpenFIGI
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OpenFigiData]**](OpenFigiData.md) | Enumerable list of OpenFIGI results | 
**perm_id_uri** | **str** | URI of the related PermID response, if requested | [optional] 
## Example

```python
from finbourne_horizon.models.open_figi_search_result import OpenFigiSearchResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

results: List[OpenFigiData] = # Replace with your value
perm_id_uri: Optional[StrictStr] = "example_perm_id_uri"
open_figi_search_result_instance = OpenFigiSearchResult(results=results, perm_id_uri=perm_id_uri)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

