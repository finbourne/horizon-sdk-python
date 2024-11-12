# InstancePropertyDefinitionOverrides


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name_override** | **str** |  | [optional] 
**description_override** | **str** |  | [optional] 
**entity_type** | **str** |  | 
**entity_sub_type** | **List[str]** |  | [optional] 
**vendor_package** | **List[str]** |  | [optional] 

## Example

```python
from finbourne_horizon.models.instance_property_definition_overrides import InstancePropertyDefinitionOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of InstancePropertyDefinitionOverrides from a JSON string
instance_property_definition_overrides_instance = InstancePropertyDefinitionOverrides.from_json(json)
# print the JSON string representation of the object
print InstancePropertyDefinitionOverrides.to_json()

# convert the object into a dict
instance_property_definition_overrides_dict = instance_property_definition_overrides_instance.to_dict()
# create an instance of InstancePropertyDefinitionOverrides from a dict
instance_property_definition_overrides_form_dict = instance_property_definition_overrides.from_dict(instance_property_definition_overrides_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

