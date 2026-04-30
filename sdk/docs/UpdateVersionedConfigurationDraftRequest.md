# UpdateVersionedConfigurationDraftRequest

Request to update the value of an existing draft versioned configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The new JSON value to store. Must be valid JSON. | 
## Example

```python
from finbourne_horizon.models.update_versioned_configuration_draft_request import UpdateVersionedConfigurationDraftRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: StrictStr = "example_value"
update_versioned_configuration_draft_request_instance = UpdateVersionedConfigurationDraftRequest(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

