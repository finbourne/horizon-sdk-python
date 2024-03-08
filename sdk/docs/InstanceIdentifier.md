# InstanceIdentifier

Identifies a single instance of an integration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Instance identifier. | 

## Example

```python
from finbourne_horizon.models.instance_identifier import InstanceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceIdentifier from a JSON string
instance_identifier_instance = InstanceIdentifier.from_json(json)
# print the JSON string representation of the object
print InstanceIdentifier.to_json()

# convert the object into a dict
instance_identifier_dict = instance_identifier_instance.to_dict()
# create an instance of InstanceIdentifier from a dict
instance_identifier_form_dict = instance_identifier.from_dict(instance_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


