# LusidPropertyDefinition

Defines the information in a LUSID Property Definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [readonly] 
**product_entity_item_key** | **str** | Property key associated with the mapping | 
**domain** | **str** | The domain of this definition. | 
**scope** | **str** | The scope of this definition. | 
**code** | **str** | The code of this definition. | 
**display_name** | **str** | The name used when this definition is displayed. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**description** | **str** |  | 
**lifetime** | **str** |  | 
**constraint_style** | **str** |  | 
## Example

```python
from finbourne_horizon.models.lusid_property_definition import LusidPropertyDefinition
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, constr

key: StrictStr = "example_key"
product_entity_item_key: StrictStr = "example_product_entity_item_key"
domain: StrictStr = "example_domain"
scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
data_type_id: ResourceId = # Replace with your value
description: StrictStr = "example_description"
lifetime: StrictStr = "example_lifetime"
constraint_style: StrictStr = "example_constraint_style"
lusid_property_definition_instance = LusidPropertyDefinition(key=key, product_entity_item_key=product_entity_item_key, domain=domain, scope=scope, code=code, display_name=display_name, data_type_id=data_type_id, description=description, lifetime=lifetime, constraint_style=constraint_style)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

