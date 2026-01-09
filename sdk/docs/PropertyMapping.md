# PropertyMapping

Mapping from a set of VendorFields to a LUSID Property
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LusidPropertyDefinition**](LusidPropertyDefinition.md) |  | 
**vendor_fields** | [**List[VendorField]**](VendorField.md) | Fields that will be used to map to this Property Definition | 
**optionality** | [**Optionality**](Optionality.md) |  | 
**entity_type** | **str** | The LUSID Entity this is valid for | 
**entity_sub_type** | **str** | The LUSID Entity sub type this is valid for | [optional] 
**transformation_description** | **str** | The transformation, if required, to map from VendorFields to the LUSID Property | [optional] 
**versions** | **List[str]** | The versions of the Vendor integration this mapping is valid for | 
## Example

```python
from finbourne_horizon.models.property_mapping import PropertyMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_property: LusidPropertyDefinition = # Replace with your value
vendor_fields: List[VendorField] = # Replace with your value
optionality: Optionality
entity_type: StrictStr = "example_entity_type"
entity_sub_type: Optional[StrictStr] = "example_entity_sub_type"
transformation_description: Optional[StrictStr] = "example_transformation_description"
versions: List[StrictStr] = # Replace with your value
property_mapping_instance = PropertyMapping(var_property=var_property, vendor_fields=vendor_fields, optionality=optionality, entity_type=entity_type, entity_sub_type=entity_sub_type, transformation_description=transformation_description, versions=versions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

