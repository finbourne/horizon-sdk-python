# LusidField

A field on a LUSID entity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the LUSID field. | 
**default_value** | **str** | The default value for the field. | [optional] 
**vendor_packages** | **List[str]** | The vendor package that contributes to this LUSID field. | 
**vendor_namespaces** | **List[str]** | The vendor namespace that contributes to this LUSID field. | 
**vendor_fields** | **List[str]** | The underlying fields on the vendor package that contribute to this LUSID field | 
**transformation_description** | **str** | A description of how the vendor package&#39;s field(s) get mapped to the LUSID field | [optional] 
**entity_type** | **str** | LUSID Entity this refers to (e.g. Instrument) | 
**entity_sub_type** | **str** | Sub-Entity this field refers to (e.g. Equity) | [optional] 
## Example

```python
from finbourne_horizon.models.lusid_field import LusidField
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

field_name: StrictStr = "example_field_name"
default_value: Optional[StrictStr] = "example_default_value"
vendor_packages: List[StrictStr] = # Replace with your value
vendor_namespaces: List[StrictStr] = # Replace with your value
vendor_fields: List[StrictStr] = # Replace with your value
transformation_description: Optional[StrictStr] = "example_transformation_description"
entity_type: StrictStr = "example_entity_type"
entity_sub_type: Optional[StrictStr] = "example_entity_sub_type"
lusid_field_instance = LusidField(field_name=field_name, default_value=default_value, vendor_packages=vendor_packages, vendor_namespaces=vendor_namespaces, vendor_fields=vendor_fields, transformation_description=transformation_description, entity_type=entity_type, entity_sub_type=entity_sub_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

