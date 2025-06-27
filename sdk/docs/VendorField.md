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
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

package: StrictStr = "example_package"
field: StrictStr = "example_field"
vendor_field_instance = VendorField(package=package, field=field)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

