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
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

vendor_name: StrictStr = "example_vendor_name"
product_name: StrictStr = "example_product_name"
vendor_product_key: StrictStr = "example_vendor_product_key"
lusid_entity: LusidEntity = # Replace with your value
vendor_product_instance = VendorProduct(vendor_name=vendor_name, product_name=product_name, vendor_product_key=vendor_product_key, lusid_entity=lusid_entity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

