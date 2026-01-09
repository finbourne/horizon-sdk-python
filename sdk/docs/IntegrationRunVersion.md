# IntegrationRunVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_created** | **datetime** |  | [optional] 
**as_at_modified** | **datetime** |  | [optional] 
## Example

```python
from finbourne_horizon.models.integration_run_version import IntegrationRunVersion
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at_created: Optional[datetime] = # Replace with your value
as_at_modified: Optional[datetime] = # Replace with your value
integration_run_version_instance = IntegrationRunVersion(as_at_created=as_at_created, as_at_modified=as_at_modified)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

