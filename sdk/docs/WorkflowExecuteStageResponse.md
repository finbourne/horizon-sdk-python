# WorkflowExecuteStageResponse

One stage of a staged integration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**steps** | **List[str]** | The steps that run for this stage. | 
**parameters** | **List[str]** | Names of every parameter this stage accepts. | 
**rules** | **List[str]** | Cross-field rules the stage enforces, in plain text. | 
## Example

```python
from finbourne_horizon.models.workflow_execute_stage_response import WorkflowExecuteStageResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
steps: List[StrictStr] = # Replace with your value
parameters: List[StrictStr] = # Replace with your value
rules: List[StrictStr] = # Replace with your value
workflow_execute_stage_response_instance = WorkflowExecuteStageResponse(name=name, steps=steps, parameters=parameters, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

