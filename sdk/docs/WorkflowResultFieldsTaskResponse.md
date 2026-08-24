# WorkflowResultFieldsTaskResponse

One of the instance's enabled RunWorkflow post-process tasks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**trigger_on** | **str** | When this task fires: OnSuccess, OnFailure or Always. | 
**result_fields** | **List[str]** | Names of the fields this particular task declares. | 
## Example

```python
from finbourne_horizon.models.workflow_result_fields_task_response import WorkflowResultFieldsTaskResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
trigger_on: StrictStr = "example_trigger_on"
result_fields: List[StrictStr] = # Replace with your value
workflow_result_fields_task_response_instance = WorkflowResultFieldsTaskResponse(name=name, trigger_on=trigger_on, result_fields=result_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

