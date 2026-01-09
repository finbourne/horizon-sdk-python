# IntegrationRunLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**link** | [**IntegrationRunLogLink**](IntegrationRunLogLink.md) |  | 
## Example

```python
from finbourne_horizon.models.integration_run_log import IntegrationRunLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

count: StrictInt
link: IntegrationRunLogLink
integration_run_log_instance = IntegrationRunLog(count=count, link=link)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

