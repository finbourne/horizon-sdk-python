# IFieldMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** |  | [optional] 
**entity_sub_type** | **str** |  | [optional] 
**entity_type** | **str** |  | 
**field_name** | **str** |  | 
**transformation_description** | **str** |  | [optional] 
**vendor_fields** | [**List[VendorField]**](VendorField.md) |  | 
**versions** | **List[str]** |  | 
## Example

```python
from finbourne_horizon.models.i_field_mapping import IFieldMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

default_value: Optional[StrictStr] = "example_default_value"
entity_sub_type: Optional[StrictStr] = "example_entity_sub_type"
entity_type: StrictStr = "example_entity_type"
field_name: StrictStr = "example_field_name"
transformation_description: Optional[StrictStr] = "example_transformation_description"
vendor_fields: List[VendorField] = # Replace with your value
versions: List[StrictStr]
i_field_mapping_instance = IFieldMapping(default_value=default_value, entity_sub_type=entity_sub_type, entity_type=entity_type, field_name=field_name, transformation_description=transformation_description, vendor_fields=vendor_fields, versions=versions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

