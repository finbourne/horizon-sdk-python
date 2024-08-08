# LusidPropertyDefinitionOverrides

Override values for property Display Name and Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 

## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides import LusidPropertyDefinitionOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of LusidPropertyDefinitionOverrides from a JSON string
lusid_property_definition_overrides_instance = LusidPropertyDefinitionOverrides.from_json(json)
# print the JSON string representation of the object
print LusidPropertyDefinitionOverrides.to_json()

# convert the object into a dict
lusid_property_definition_overrides_dict = lusid_property_definition_overrides_instance.to_dict()
# create an instance of LusidPropertyDefinitionOverrides from a dict
lusid_property_definition_overrides_form_dict = lusid_property_definition_overrides.from_dict(lusid_property_definition_overrides_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


