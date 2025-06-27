# LusidPropertyDefinitionOverrides

Override values for property Display Name and Description
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides import LusidPropertyDefinitionOverrides
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

display_name_override: Optional[StrictStr] = "example_display_name_override"
description_override: Optional[StrictStr] = "example_description_override"
lusid_property_definition_overrides_instance = LusidPropertyDefinitionOverrides(display_name_override=display_name_override, description_override=description_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

