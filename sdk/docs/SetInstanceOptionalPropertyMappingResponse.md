# SetInstanceOptionalPropertyMappingResponse

Response for SetInstanceOptionalPropertyMapping.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_overrides** | [**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md) | The full, current optional property mapping for the instance, after the write. | 
**warnings** | **List[str]** | Advisory warnings about a write that succeeded regardless, e.g. a future-dated effectiveFromOverride, or another enabled instance of the same integration holding a different effectiveFromOverride for the same property. | 
## Example

```python
from finbourne_horizon.models.set_instance_optional_property_mapping_response import SetInstanceOptionalPropertyMappingResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_overrides: Dict[str, LusidPropertyDefinitionOverridesByType] = # Replace with your value
warnings: List[StrictStr] = # Replace with your value
set_instance_optional_property_mapping_response_instance = SetInstanceOptionalPropertyMappingResponse(property_overrides=property_overrides, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

