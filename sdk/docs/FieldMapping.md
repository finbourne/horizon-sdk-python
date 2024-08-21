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

# TODO update the JSON string below
json = "{}"
# create an instance of FieldMapping from a JSON string
field_mapping_instance = FieldMapping.from_json(json)
# print the JSON string representation of the object
print FieldMapping.to_json()

# convert the object into a dict
field_mapping_dict = field_mapping_instance.to_dict()
# create an instance of FieldMapping from a dict
field_mapping_form_dict = field_mapping.from_dict(field_mapping_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


