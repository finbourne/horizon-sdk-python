# VendorField

Reference to a specific vendor field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | **str** | The vendor package it is included in | 
**field** | **str** | The name of the field | 

## Example

```python
from finbourne_horizon.models.vendor_field import VendorField

# TODO update the JSON string below
json = "{}"
# create an instance of VendorField from a JSON string
vendor_field_instance = VendorField.from_json(json)
# print the JSON string representation of the object
print VendorField.to_json()

# convert the object into a dict
vendor_field_dict = vendor_field_instance.to_dict()
# create an instance of VendorField from a dict
vendor_field_form_dict = vendor_field.from_dict(vendor_field_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


