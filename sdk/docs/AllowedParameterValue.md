# AllowedParameterValue

An allowed parameter value for an OpenFigi Parameter Option.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_value** | **str** |  | 
## Example

```python
from finbourne_horizon.models.allowed_parameter_value import AllowedParameterValue
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

allowed_value: StrictStr = "example_allowed_value"
allowed_parameter_value_instance = AllowedParameterValue(allowed_value=allowed_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

