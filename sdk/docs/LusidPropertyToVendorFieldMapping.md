# LusidPropertyToVendorFieldMapping

The mapping of a LUSID Property from the Vendor Field that would populate it
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LusidPropertyDefinition**](LusidPropertyDefinition.md) |  | 
**vendor_field** | **str** |  | 
**vendor_package** | **str** |  | 
**vendor_namespace** | **str** |  | 
**optionality** | **str** |  | 
## Example

```python
from finbourne_horizon.models.lusid_property_to_vendor_field_mapping import LusidPropertyToVendorFieldMapping
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_property: LusidPropertyDefinition = # Replace with your value
vendor_field: StrictStr = "example_vendor_field"
vendor_package: StrictStr = "example_vendor_package"
vendor_namespace: StrictStr = "example_vendor_namespace"
optionality: StrictStr = "example_optionality"
lusid_property_to_vendor_field_mapping_instance = LusidPropertyToVendorFieldMapping(var_property=var_property, vendor_field=vendor_field, vendor_package=vendor_package, vendor_namespace=vendor_namespace, optionality=optionality)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

