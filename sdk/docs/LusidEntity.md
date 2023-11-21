# LusidEntity

Information about the LUSID entity this data can be used with

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The entity type | 
**entity_type_display_name** | **str** | The display name for the entity type. | 
**entity_sub_type** | **str** | The entity sub-type | [optional] 
**entity_sub_type_display_name** | **str** | Display name for the entity sub-type | [optional] 

## Example

```python
from finbourne_horizon.models.lusid_entity import LusidEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LusidEntity from a JSON string
lusid_entity_instance = LusidEntity.from_json(json)
# print the JSON string representation of the object
print LusidEntity.to_json()

# convert the object into a dict
lusid_entity_dict = lusid_entity_instance.to_dict()
# create an instance of LusidEntity from a dict
lusid_entity_form_dict = lusid_entity.from_dict(lusid_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


