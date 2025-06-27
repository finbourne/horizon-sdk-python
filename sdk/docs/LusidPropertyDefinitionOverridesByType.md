# LusidPropertyDefinitionOverridesByType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_sub_type** | **List[str]** |  | [optional] 
**vendor_package** | **List[str]** |  | [optional] 
## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides_by_type import LusidPropertyDefinitionOverridesByType
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

display_name_override: Optional[StrictStr] = "example_display_name_override"
description_override: Optional[StrictStr] = "example_description_override"
entity_type: Optional[StrictStr] = "example_entity_type"
entity_sub_type: Optional[conlist(StrictStr)] = # Replace with your value
vendor_package: Optional[conlist(StrictStr)] = # Replace with your value
lusid_property_definition_overrides_by_type_instance = LusidPropertyDefinitionOverridesByType(display_name_override=display_name_override, description_override=description_override, entity_type=entity_type, entity_sub_type=entity_sub_type, vendor_package=vendor_package)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

