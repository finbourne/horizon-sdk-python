# InstanceDestinations

record containing details of the destinations for an instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | **str** |  | 
**name** | **str** |  | 
**destination_path** | **str** |  | 
## Example

```python
from finbourne_horizon.models.instance_destinations import InstanceDestinations
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

destination_type: StrictStr = "example_destination_type"
name: StrictStr = "example_name"
destination_path: StrictStr = "example_destination_path"
instance_destinations_instance = InstanceDestinations(destination_type=destination_type, name=name, destination_path=destination_path)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

