# WorkflowExecuteParameterResponse

A single execute parameter.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** | One of the Workflow field types: String, Decimal, DateTime, Boolean. | 
**required** | **bool** | Whether every run must supply the parameter, whatever its stage. | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**format** | **str** | The shape a String value must take, e.g. YYYY-MM, when it has one. | [optional] 
**allowed_values** | **List[str]** | The closed set of accepted values, when there is one. | [optional] 
**required_for_stages** | **List[str]** | The stages for which the parameter is mandatory. | 
## Example

```python
from finbourne_horizon.models.workflow_execute_parameter_response import WorkflowExecuteParameterResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
type: StrictStr = "example_type"
required: StrictBool = # Replace with your value
required:StrictBool = True
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
format: Optional[StrictStr] = "example_format"
allowed_values: Optional[List[StrictStr]] = # Replace with your value
required_for_stages: List[StrictStr] = # Replace with your value
workflow_execute_parameter_response_instance = WorkflowExecuteParameterResponse(name=name, type=type, required=required, display_name=display_name, description=description, format=format, allowed_values=allowed_values, required_for_stages=required_for_stages)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

