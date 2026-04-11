# ProcessorDescription

Represents a processor in the Horizon integration system.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**category** | **str** |  | 
**is_active** | **bool** |  | 
## Example

```python
from finbourne_horizon.models.processor_description import ProcessorDescription
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
category: StrictStr = "example_category"
is_active: StrictBool = # Replace with your value
is_active:StrictBool = True
processor_description_instance = ProcessorDescription(name=name, display_name=display_name, description=description, category=category, is_active=is_active)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

