# IntegrationRunIntegration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
## Example

```python
from finbourne_horizon.models.integration_run_integration import IntegrationRunIntegration
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

name: StrictStr = "example_name"
type: StrictStr = "example_type"
integration_run_integration_instance = IntegrationRunIntegration(name=name, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

