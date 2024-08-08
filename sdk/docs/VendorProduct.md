# VendorProduct

Denormalised information about vendors, the products they provide and the LUSID entity types they can be used to populate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** |  | 
**product_name** | **str** |  | 
**vendor_product_key** | **str** |  | 
**lusid_entity** | [**LusidEntity**](LusidEntity.md) |  | 

## Example

```python
from finbourne_horizon.models.vendor_product import VendorProduct

# TODO update the JSON string below
json = "{}"
# create an instance of VendorProduct from a JSON string
vendor_product_instance = VendorProduct.from_json(json)
# print the JSON string representation of the object
print VendorProduct.to_json()

# convert the object into a dict
vendor_product_dict = vendor_product_instance.to_dict()
# create an instance of VendorProduct from a dict
vendor_product_form_dict = vendor_product.from_dict(vendor_product_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


