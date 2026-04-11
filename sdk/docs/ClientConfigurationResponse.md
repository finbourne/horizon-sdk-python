# ClientConfigurationResponse

Represents a versioned client configuration record.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The logical name of the configuration. | 
**config_type** | **str** | The category of configuration. | 
**major_version** | **int** | The major version number. | 
**minor_version** | **int** | The minor version number. | 
**value** | **str** | The JSON configuration value. | 
**is_draft** | **bool** | Whether this version is still in draft state. Draft versions can be edited; locked versions cannot. | 
## Example

```python
from finbourne_horizon.models.client_configuration_response import ClientConfigurationResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
config_type: StrictStr = "example_config_type"
major_version: StrictInt = # Replace with your value
major_version: StrictInt = 42
minor_version: StrictInt = # Replace with your value
minor_version: StrictInt = 42
value: StrictStr = "example_value"
is_draft: StrictBool = # Replace with your value
is_draft:StrictBool = True
client_configuration_response_instance = ClientConfigurationResponse(name=name, config_type=config_type, major_version=major_version, minor_version=minor_version, value=value, is_draft=is_draft)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

