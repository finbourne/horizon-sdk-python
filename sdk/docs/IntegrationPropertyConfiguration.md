# IntegrationPropertyConfiguration

Response containing the description of an integration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The Integration this property configuration applies to | 
**properties** | [**List[PropertyMapping]**](PropertyMapping.md) | The mandatory and optional properties available in this integration | 
**fields** | [**List[FieldMapping]**](FieldMapping.md) | The fields available in this integration | 
## Example

```python
from finbourne_horizon.models.integration_property_configuration import IntegrationPropertyConfiguration
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

type: StrictStr = "example_type"
properties: conlist(PropertyMapping) = # Replace with your value
fields: conlist(FieldMapping) = # Replace with your value
integration_property_configuration_instance = IntegrationPropertyConfiguration(type=type, properties=properties, fields=fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

