# Trigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**cron_expression** | **str** |  | 
**time_zone** | **str** |  | 
## Example

```python
from finbourne_horizon.models.trigger import Trigger
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

type: StrictStr = "example_type"
cron_expression: StrictStr = "example_cron_expression"
time_zone: StrictStr = "example_time_zone"
trigger_instance = Trigger(type=type, cron_expression=cron_expression, time_zone=time_zone)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

