# LusidPropertyDefinition

Defines the information in a LUSID Property Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Property key associated with the mapping | [readonly] 
**domain** | **str** | The domain of this definition. | 
**scope** | **str** | The scope of this definition. | 
**code** | **str** | The code of this definition. | 
**display_name** | **str** | The name used when this definition is displayed. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** |  | 
**lifetime** | **str** |  | 
**constraint_style** | **str** |  | 

## Example

```python
from finbourne_horizon.models.lusid_property_definition import LusidPropertyDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of LusidPropertyDefinition from a JSON string
lusid_property_definition_instance = LusidPropertyDefinition.from_json(json)
# print the JSON string representation of the object
print LusidPropertyDefinition.to_json()

# convert the object into a dict
lusid_property_definition_dict = lusid_property_definition_instance.to_dict()
# create an instance of LusidPropertyDefinition from a dict
lusid_property_definition_form_dict = lusid_property_definition.from_dict(lusid_property_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


