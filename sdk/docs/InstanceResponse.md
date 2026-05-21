# InstanceResponse

record containing details of a single instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**enabled** | **bool** |  | 
**portfolios** | [**List[TpfPortfolio]**](TpfPortfolio.md) |  | 
**schedule** | **str** |  | [optional] 
**schedule_timezone** | **str** |  | [optional] 
**last_run_at** | **datetime** |  | [optional] 
**last_run_status** | **str** |  | [optional] 
**latest_runs_in24_hours** | **str** |  | [optional] 
**destinations** | [**List[InstanceDestinations]**](InstanceDestinations.md) |  | 
## Example

```python
from finbourne_horizon.models.instance_response import InstanceResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
name: StrictStr = "example_name"
enabled: StrictBool
enabled:StrictBool = True
portfolios: List[TpfPortfolio]
schedule: Optional[StrictStr] = "example_schedule"
schedule_timezone: Optional[StrictStr] = "example_schedule_timezone"
last_run_at: Optional[datetime] = # Replace with your value
last_run_status: Optional[StrictStr] = "example_last_run_status"
latest_runs_in24_hours: Optional[StrictStr] = "example_latest_runs_in24_hours"
destinations: List[InstanceDestinations]
instance_response_instance = InstanceResponse(id=id, name=name, enabled=enabled, portfolios=portfolios, schedule=schedule, schedule_timezone=schedule_timezone, last_run_at=last_run_at, last_run_status=last_run_status, latest_runs_in24_hours=latest_runs_in24_hours, destinations=destinations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

