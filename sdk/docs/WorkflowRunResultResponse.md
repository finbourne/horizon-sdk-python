# WorkflowRunResultResponse

A single declared field and the value this run published for it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | One of the Workflow field types: String, Decimal, DateTime, Boolean, LusidUserId. | 
**value** | **str** | The published value, or null when the run published nothing for this field. | [optional] 
**display_name** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.workflow_run_result_response import WorkflowRunResultResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
type: StrictStr = "example_type"
value: Optional[StrictStr] = "example_value"
display_name: Optional[StrictStr] = "example_display_name"
workflow_run_result_response_instance = WorkflowRunResultResponse(name=name, type=type, value=value, display_name=display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

