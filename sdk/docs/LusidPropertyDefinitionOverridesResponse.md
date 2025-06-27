# LusidPropertyDefinitionOverridesResponse

An item that has been updated as a result of setting LusidPropertyDefinitionOverrides.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action performed on this property. \&quot;upsert\&quot; for setting values for new and existing              properties. \&quot;delete\&quot; for existing properties that were removed | 
**write_error** | **str** |  | [optional] 
**write_error_detail** | **str** |  | [optional] 
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides_response import LusidPropertyDefinitionOverridesResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

action: StrictStr = "example_action"
write_error: Optional[StrictStr] = "example_write_error"
write_error_detail: Optional[StrictStr] = "example_write_error_detail"
display_name_override: Optional[StrictStr] = "example_display_name_override"
description_override: Optional[StrictStr] = "example_description_override"
lusid_property_definition_overrides_response_instance = LusidPropertyDefinitionOverridesResponse(action=action, write_error=write_error, write_error_detail=write_error_detail, display_name_override=display_name_override, description_override=description_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

