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

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyMapping from a JSON string
property_mapping_instance = PropertyMapping.from_json(json)
# print the JSON string representation of the object
print PropertyMapping.to_json()

# convert the object into a dict
property_mapping_dict = property_mapping_instance.to_dict()
# create an instance of PropertyMapping from a dict
property_mapping_form_dict = property_mapping.from_dict(property_mapping_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


