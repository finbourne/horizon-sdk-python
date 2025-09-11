# IntegrationRunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**ref_run_id** | **str** |  | [optional] 
**attempt** | **int** |  | 
**instance_id** | **str** |  | [optional] 
**instance_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**integration** | [**IntegrationRunIntegration**](IntegrationRunIntegration.md) |  | 
**version** | [**IntegrationRunVersion**](IntegrationRunVersion.md) |  | 
**integration_logs** | **Dict[str, Dict[str, IntegrationRunLog]]** |  | [optional] 
## Example

```python
from finbourne_horizon.models.integration_run_response import IntegrationRunResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr

run_id: StrictStr = "example_run_id"
ref_run_id: Optional[StrictStr] = "example_ref_run_id"
attempt: StrictInt = # Replace with your value
attempt: StrictInt = 42
instance_id: Optional[StrictStr] = "example_instance_id"
instance_name: Optional[StrictStr] = "example_instance_name"
status: Optional[StrictStr] = "example_status"
message: Optional[StrictStr] = "example_message"
integration: IntegrationRunIntegration = # Replace with your value
version: IntegrationRunVersion = # Replace with your value
integration_logs: Optional[Dict[str, Dict[str, IntegrationRunLog]]] = # Replace with your value
integration_run_response_instance = IntegrationRunResponse(run_id=run_id, ref_run_id=ref_run_id, attempt=attempt, instance_id=instance_id, instance_name=instance_name, status=status, message=message, integration=integration, version=version, integration_logs=integration_logs)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

