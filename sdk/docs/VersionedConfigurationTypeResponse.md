# VersionedConfigurationTypeResponse

Represents a registered versioned configuration type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_type** | **str** |  | 
**display_name** | **str** |  | 
## Example

```python
from finbourne_horizon.models.versioned_configuration_type_response import VersionedConfigurationTypeResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

config_type: StrictStr = "example_config_type"
display_name: StrictStr = "example_display_name"
versioned_configuration_type_response_instance = VersionedConfigurationTypeResponse(config_type=config_type, display_name=display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

