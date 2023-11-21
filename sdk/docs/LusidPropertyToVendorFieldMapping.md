# LusidPropertyToVendorFieldMapping

The mapping of a LUSID Property to the Vendor Field that would populate it

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LusidPropertyDefinition**](LusidPropertyDefinition.md) |  | 
**vendor_field** | **str** |  | 
**optionality** | [**Optionality**](Optionality.md) |  | 

## Example

```python
from finbourne_horizon.models.lusid_property_to_vendor_field_mapping import LusidPropertyToVendorFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of LusidPropertyToVendorFieldMapping from a JSON string
lusid_property_to_vendor_field_mapping_instance = LusidPropertyToVendorFieldMapping.from_json(json)
# print the JSON string representation of the object
print LusidPropertyToVendorFieldMapping.to_json()

# convert the object into a dict
lusid_property_to_vendor_field_mapping_dict = lusid_property_to_vendor_field_mapping_instance.to_dict()
# create an instance of LusidPropertyToVendorFieldMapping from a dict
lusid_property_to_vendor_field_mapping_form_dict = lusid_property_to_vendor_field_mapping.from_dict(lusid_property_to_vendor_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


