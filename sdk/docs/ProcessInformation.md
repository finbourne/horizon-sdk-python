# ProcessInformation

Required information for each process
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**process_name** | **str** |  | 
**run_id** | **str** |  | 
**start_time** | **datetime** |  | 
**data_action** | **str** |  | 
**schema_version** | **str** |  | [optional] 
**user_id** | **str** |  | 
**process_summary** | [**ProcessSummary**](ProcessSummary.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.process_information import ProcessInformation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

domain: StrictStr = "example_domain"
process_name: StrictStr = "example_process_name"
run_id: StrictStr = "example_run_id"
start_time: datetime = # Replace with your value
data_action: StrictStr = "example_data_action"
schema_version: Optional[StrictStr] = "example_schema_version"
user_id: StrictStr = "example_user_id"
process_summary: Optional[ProcessSummary] = # Replace with your value
process_information_instance = ProcessInformation(domain=domain, process_name=process_name, run_id=run_id, start_time=start_time, data_action=data_action, schema_version=schema_version, user_id=user_id, process_summary=process_summary)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

