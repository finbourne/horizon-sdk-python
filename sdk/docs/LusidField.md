# LusidField

A field on a LUSID entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the LUSID field. | 
**default_value** | **str** | The default value for the field. | [optional] 
**vendor_packages** | **List[str]** | The vendor package that contributes to this LUSID field. | 
**vendor_namespaces** | **List[str]** | The vendor namespace that contributes to this LUSID field. | 
**vendor_fields** | **List[str]** | The underlying fields on the vendor package that contribute to this LUSID field | 
**transformation_description** | **str** | A description of how the vendor package&#39;s field(s) get mapped to the LUSID field | [optional] 

## Example

```python
from finbourne_horizon.models.lusid_field import LusidField

# TODO update the JSON string below
json = "{}"
# create an instance of LusidField from a JSON string
lusid_field_instance = LusidField.from_json(json)
# print the JSON string representation of the object
print LusidField.to_json()

# convert the object into a dict
lusid_field_dict = lusid_field_instance.to_dict()
# create an instance of LusidField from a dict
lusid_field_form_dict = lusid_field.from_dict(lusid_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


