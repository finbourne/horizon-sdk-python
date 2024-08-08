# PagedResourceListOfVendorProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[VendorProduct]**](VendorProduct.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.paged_resource_list_of_vendor_product import PagedResourceListOfVendorProduct

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfVendorProduct from a JSON string
paged_resource_list_of_vendor_product_instance = PagedResourceListOfVendorProduct.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfVendorProduct.to_json()

# convert the object into a dict
paged_resource_list_of_vendor_product_dict = paged_resource_list_of_vendor_product_instance.to_dict()
# create an instance of PagedResourceListOfVendorProduct from a dict
paged_resource_list_of_vendor_product_form_dict = paged_resource_list_of_vendor_product.from_dict(paged_resource_list_of_vendor_product_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


