# IPropertyMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_sub_type** | **str** |  | [optional] 
**entity_type** | **str** |  | 
**optionality** | **str** |  | 
**var_property** | [**LusidPropertyDefinition**](LusidPropertyDefinition.md) |  | 
**transformation_description** | **str** |  | [optional] 
**vendor_fields** | [**List[VendorField]**](VendorField.md) |  | 
**versions** | **List[str]** |  | 
## Example

```python
from finbourne_horizon.models.i_property_mapping import IPropertyMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_sub_type: Optional[StrictStr] = "example_entity_sub_type"
entity_type: StrictStr = "example_entity_type"
optionality: StrictStr = "example_optionality"
var_property: LusidPropertyDefinition = # Replace with your value
transformation_description: Optional[StrictStr] = "example_transformation_description"
vendor_fields: List[VendorField] = # Replace with your value
versions: List[StrictStr]
i_property_mapping_instance = IPropertyMapping(entity_sub_type=entity_sub_type, entity_type=entity_type, optionality=optionality, var_property=var_property, transformation_description=transformation_description, vendor_fields=vendor_fields, versions=versions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

