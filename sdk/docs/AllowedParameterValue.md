# AllowedParameterValue

An allowed parameter value for an OpenFigi Parameter Option.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_value** | **str** |  | 

## Example

```python
from finbourne_horizon.models.allowed_parameter_value import AllowedParameterValue

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedParameterValue from a JSON string
allowed_parameter_value_instance = AllowedParameterValue.from_json(json)
# print the JSON string representation of the object
print AllowedParameterValue.to_json()

# convert the object into a dict
allowed_parameter_value_dict = allowed_parameter_value_instance.to_dict()
# create an instance of AllowedParameterValue from a dict
allowed_parameter_value_form_dict = allowed_parameter_value.from_dict(allowed_parameter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


