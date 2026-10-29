# WorkflowExecuteParametersResponse

The execute parameters a Workflow-driven integration instance accepts on executewithparams.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | The instance these parameters belong to. | 
**integration_type** | **str** | The integration type of the instance, e.g. ta-tax-processes. | 
**parameters** | [**List[WorkflowExecuteParameterResponse]**](WorkflowExecuteParameterResponse.md) | Every parameter the integration accepts, each listed once. | 
**stages** | [**List[WorkflowExecuteStageResponse]**](WorkflowExecuteStageResponse.md) | Per-stage breakdown of the steps that run and the parameters accepted. | 
## Example

```python
from finbourne_horizon.models.workflow_execute_parameters_response import WorkflowExecuteParametersResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instance_id: StrictStr = "example_instance_id"
integration_type: StrictStr = "example_integration_type"
parameters: List[WorkflowExecuteParameterResponse] = # Replace with your value
stages: List[WorkflowExecuteStageResponse] = # Replace with your value
workflow_execute_parameters_response_instance = WorkflowExecuteParametersResponse(instance_id=instance_id, integration_type=integration_type, parameters=parameters, stages=stages)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

