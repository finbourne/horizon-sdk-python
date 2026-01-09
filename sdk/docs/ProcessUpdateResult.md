# ProcessUpdateResult

Shows details relevant to update events for a query
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**entry_id** | **str** |  | 
**process_name** | **str** |  | 
**run_id** | **str** |  | 
**entry_date** | **datetime** |  | 
**status** | **str** |  | 
**message** | **str** |  | 
**schema_version** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.process_update_result import ProcessUpdateResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

domain: StrictStr = "example_domain"
entry_id: StrictStr = "example_entry_id"
process_name: StrictStr = "example_process_name"
run_id: StrictStr = "example_run_id"
entry_date: datetime = # Replace with your value
status: StrictStr = "example_status"
message: StrictStr = "example_message"
schema_version: Optional[StrictStr] = "example_schema_version"
process_update_result_instance = ProcessUpdateResult(domain=domain, entry_id=entry_id, process_name=process_name, run_id=run_id, entry_date=entry_date, status=status, message=message, schema_version=schema_version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

