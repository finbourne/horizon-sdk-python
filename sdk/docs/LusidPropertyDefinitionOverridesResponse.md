# LusidPropertyDefinitionOverridesResponse

An item that has been updated as a result of setting LusidPropertyDefinitionOverrides.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action performed on this property. \&quot;upsert\&quot; for setting values for new and existing              properties. \&quot;delete\&quot; for existing properties that were removed | 
**write_error** | **str** |  | [optional] 
**write_error_detail** | **str** |  | [optional] 
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 

## Example

```python
from finbourne_horizon.models.lusid_property_definition_overrides_response import LusidPropertyDefinitionOverridesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LusidPropertyDefinitionOverridesResponse from a JSON string
lusid_property_definition_overrides_response_instance = LusidPropertyDefinitionOverridesResponse.from_json(json)
# print the JSON string representation of the object
print LusidPropertyDefinitionOverridesResponse.to_json()

# convert the object into a dict
lusid_property_definition_overrides_response_dict = lusid_property_definition_overrides_response_instance.to_dict()
# create an instance of LusidPropertyDefinitionOverridesResponse from a dict
lusid_property_definition_overrides_response_form_dict = lusid_property_definition_overrides_response.from_dict(lusid_property_definition_overrides_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


