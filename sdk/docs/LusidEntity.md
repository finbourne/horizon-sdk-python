# LusidEntity

Information about the LUSID entity this data can be used with
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The entity type | 
**entity_type_display_name** | **str** | The display name for the entity type. | 
**entity_sub_type** | **str** | The entity sub-type | [optional] 
**entity_sub_type_display_name** | **str** | Display name for the entity sub-type | [optional] 
## Example

```python
from finbourne_horizon.models.lusid_entity import LusidEntity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_type_display_name: StrictStr = "example_entity_type_display_name"
entity_sub_type: Optional[StrictStr] = "example_entity_sub_type"
entity_sub_type_display_name: Optional[StrictStr] = "example_entity_sub_type_display_name"
lusid_entity_instance = LusidEntity(entity_type=entity_type, entity_type_display_name=entity_type_display_name, entity_sub_type=entity_sub_type, entity_sub_type_display_name=entity_sub_type_display_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

