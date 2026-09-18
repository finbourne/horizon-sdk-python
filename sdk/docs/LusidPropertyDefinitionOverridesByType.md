# LusidPropertyDefinitionOverridesByType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_sub_type** | **List[str]** |  | [optional] 
**vendor_package** | **List[str]** |  | [optional] 
**effective_from_override** | **str** | ISO-8601 instant to use as the property value&#39;s effectiveFrom instead of the date the integration derives, e.g. \&quot;0001-01-01T00:00:00Z\&quot;. Only accepted for integrations reporting supportsEffectiveFromOverride, and only for TimeVariant property definitions. Omit to leave any stored value untouched; send an empty string to clear it. | [optional] 
## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides_by_type import LusidPropertyDefinitionOverridesByType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name_override: Optional[StrictStr] = "example_display_name_override"
description_override: Optional[StrictStr] = "example_description_override"
entity_type: Optional[StrictStr] = "example_entity_type"
entity_sub_type: Optional[List[StrictStr]] = # Replace with your value
vendor_package: Optional[List[StrictStr]] = # Replace with your value
effective_from_override: Optional[StrictStr] = "example_effective_from_override"
lusid_property_definition_overrides_by_type_instance = LusidPropertyDefinitionOverridesByType(display_name_override=display_name_override, description_override=description_override, entity_type=entity_type, entity_sub_type=entity_sub_type, vendor_package=vendor_package, effective_from_override=effective_from_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

