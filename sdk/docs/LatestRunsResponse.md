# LatestRunsResponse

record containing the 24-hour run summary grouped by external status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**status_counts** | [**List[RunStatusCount]**](RunStatusCount.md) |  | 
## Example

```python
from finbourne_horizon.models.latest_runs_response import LatestRunsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

total: StrictInt
total: StrictInt = 42
status_counts: List[RunStatusCount] = # Replace with your value
latest_runs_response_instance = LatestRunsResponse(total=total, status_counts=status_counts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

