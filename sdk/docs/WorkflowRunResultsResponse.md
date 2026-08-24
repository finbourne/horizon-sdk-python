# WorkflowRunResultsResponse

A run's status and the result values it published, which is what the Workflow AQS polls while it waits for an integration it started to finish.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The run these results belong to, as returned by the execute endpoint. | 
**instance_id** | **str** | The instance that ran. | 
**status** | **str** | The run&#39;s status, reported exactly as the runs endpoint reports it: Queued, Started, Completed, Errored or Interrupted. A caller waiting for the run to finish is waiting for one of the last three. | 
**queued_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** | Null until the run reaches a terminal status. | [optional] 
**attempt** | **int** | Which attempt this run is, counting reruns of the same work. | 
**reports_to_workflow** | **bool** | Whether this run was started by a Workflow task. False for a scheduled or file-triggered run, which publishes no results because nothing is waiting on them. | 
**results** | [**List[WorkflowRunResultResponse]**](WorkflowRunResultResponse.md) | One entry per field the instance declares, so the shape matches what the discovery endpoint promised when the worker was created. A declared field the run never published carries a null value. | 
## Example

```python
from finbourne_horizon.models.workflow_run_results_response import WorkflowRunResultsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: StrictStr = "example_run_id"
instance_id: StrictStr = "example_instance_id"
status: StrictStr = "example_status"
queued_at: Optional[datetime] = # Replace with your value
started_at: Optional[datetime] = # Replace with your value
completed_at: Optional[datetime] = # Replace with your value
attempt: StrictInt = # Replace with your value
attempt: StrictInt = 42
reports_to_workflow: StrictBool = # Replace with your value
reports_to_workflow:StrictBool = True
results: List[WorkflowRunResultResponse] = # Replace with your value
workflow_run_results_response_instance = WorkflowRunResultsResponse(run_id=run_id, instance_id=instance_id, status=status, queued_at=queued_at, started_at=started_at, completed_at=completed_at, attempt=attempt, reports_to_workflow=reports_to_workflow, results=results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

