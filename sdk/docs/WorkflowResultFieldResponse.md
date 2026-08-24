# WorkflowResultFieldResponse

A single declared field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | One of the Workflow field types: String, Decimal, DateTime, Boolean, LusidUserId. | 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.workflow_result_field_response import WorkflowResultFieldResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
type: StrictStr = "example_type"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
workflow_result_field_response_instance = WorkflowResultFieldResponse(name=name, type=type, display_name=display_name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

