# LusidPropertyDefinitionOverridesByType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_sub_type** | **List[str]** |  | [optional] 
**vendor_package** | **List[str]** |  | [optional] 

## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides_by_type import LusidPropertyDefinitionOverridesByType

# TODO update the JSON string below
json = "{}"
# create an instance of LusidPropertyDefinitionOverridesByType from a JSON string
lusid_property_definition_overrides_by_type_instance = LusidPropertyDefinitionOverridesByType.from_json(json)
# print the JSON string representation of the object
print LusidPropertyDefinitionOverridesByType.to_json()

# convert the object into a dict
lusid_property_definition_overrides_by_type_dict = lusid_property_definition_overrides_by_type_instance.to_dict()
# create an instance of LusidPropertyDefinitionOverridesByType from a dict
lusid_property_definition_overrides_by_type_form_dict = lusid_property_definition_overrides_by_type.from_dict(lusid_property_definition_overrides_by_type_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


