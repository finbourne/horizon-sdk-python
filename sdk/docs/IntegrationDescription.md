# IntegrationDescription

Response containing the description of an integration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Unique identifier of the integration e.g. \&quot;copp-clark\&quot;. | 
**name** | **str** | Readable name of the integration e.g. \&quot;Copp Clark\&quot;. | 
**description** | **str** | Describes the purpose of the integration. | 
**supported_trigger_types** | **List[str]** | Trigger types (Time, File) the integration supports. | 
**licensed** | **bool** | True if your domain is licensed to use this integration, otherwise false. | 
## Example

```python
from finbourne_horizon.models.integration_description import IntegrationDescription
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist

type: StrictStr = "example_type"
name: StrictStr = "example_name"
description: StrictStr = "example_description"
supported_trigger_types: conlist(StrictStr) = # Replace with your value
licensed: StrictBool = # Replace with your value
licensed:StrictBool = True
integration_description_instance = IntegrationDescription(type=type, name=name, description=description, supported_trigger_types=supported_trigger_types, licensed=licensed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

