# FieldMapping

Mapping from a set of Vendor Fields to a LUSID core entity field
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The LUSID core entity field | 
**default_value** | **str** | Default value if needed | [optional] 
**vendor_fields** | [**List[VendorField]**](VendorField.md) | Fields that will be used to map to this field | 
**transformation_description** | **str** | The transformation, if required, to map from VendorFields to the LUSID Property | [optional] 
**entity_type** | **str** | The LUSID Entity this is valid for | 
**entity_sub_type** | **str** | The LUSID Entity sub type this is valid for | [optional] 
**versions** | **List[str]** | The versions of the Vendor integration this mapping is valid for | 
## Example

```python
from finbourne_horizon.models.field_mapping import FieldMapping
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

field_name: StrictStr = "example_field_name"
default_value: Optional[StrictStr] = "example_default_value"
vendor_fields: conlist(VendorField) = # Replace with your value
transformation_description: Optional[StrictStr] = "example_transformation_description"
entity_type: StrictStr = "example_entity_type"
entity_sub_type: Optional[StrictStr] = "example_entity_sub_type"
versions: conlist(StrictStr) = # Replace with your value
field_mapping_instance = FieldMapping(field_name=field_name, default_value=default_value, vendor_fields=vendor_fields, transformation_description=transformation_description, entity_type=entity_type, entity_sub_type=entity_sub_type, versions=versions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

