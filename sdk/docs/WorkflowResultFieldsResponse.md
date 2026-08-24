# WorkflowResultFieldsResponse

The result fields an instance returns to the Workflow task that started its run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | The instance these fields belong to. | 
**reports_to_workflow** | **bool** | Whether this instance has an enabled RunWorkflow post-process task at all. | 
**result_fields** | [**List[WorkflowResultFieldResponse]**](WorkflowResultFieldResponse.md) | Every distinct field declared across this instance&#39;s RunWorkflow tasks. | 
**tasks** | [**List[WorkflowResultFieldsTaskResponse]**](WorkflowResultFieldsTaskResponse.md) | Per-task breakdown: an instance may declare different fields on success and on failure. | 
## Example

```python
from finbourne_horizon.models.workflow_result_fields_response import WorkflowResultFieldsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instance_id: StrictStr = "example_instance_id"
reports_to_workflow: StrictBool = # Replace with your value
reports_to_workflow:StrictBool = True
result_fields: List[WorkflowResultFieldResponse] = # Replace with your value
tasks: List[WorkflowResultFieldsTaskResponse] = # Replace with your value
workflow_result_fields_response_instance = WorkflowResultFieldsResponse(instance_id=instance_id, reports_to_workflow=reports_to_workflow, result_fields=result_fields, tasks=tasks)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

