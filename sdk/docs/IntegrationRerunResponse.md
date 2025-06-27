# IntegrationRerunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**InstanceExecutionReferenceId**](InstanceExecutionReferenceId.md) |  | 
## Example

```python
from finbourne_horizon.models.integration_rerun_response import IntegrationRerunResponse
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

run_id: InstanceExecutionReferenceId = # Replace with your value
integration_rerun_response_instance = IntegrationRerunResponse(run_id=run_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

