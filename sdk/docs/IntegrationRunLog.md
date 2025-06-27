# IntegrationRunLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**link** | [**IntegrationRunLogLink**](IntegrationRunLogLink.md) |  | 
## Example

```python
from finbourne_horizon.models.integration_run_log import IntegrationRunLog
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

count: StrictInt = # Replace with your value
link: IntegrationRunLogLink = # Replace with your value
integration_run_log_instance = IntegrationRunLog(count=count, link=link)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

