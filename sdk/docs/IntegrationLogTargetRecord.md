# IntegrationLogTargetRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_action** | **str** |  | [optional] 
**record_type** | **str** |  | [optional] 
**id_type** | **str** |  | [optional] 
**id_value** | **str** |  | [optional] 
**attribute_name** | **str** |  | [optional] 
**attribute_value** | **str** |  | [optional] 
## Example

```python
from finbourne_horizon.models.integration_log_target_record import IntegrationLogTargetRecord
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

record_action: Optional[StrictStr] = "example_record_action"
record_type: Optional[StrictStr] = "example_record_type"
id_type: Optional[StrictStr] = "example_id_type"
id_value: Optional[StrictStr] = "example_id_value"
attribute_name: Optional[StrictStr] = "example_attribute_name"
attribute_value: Optional[StrictStr] = "example_attribute_value"
integration_log_target_record_instance = IntegrationLogTargetRecord(record_action=record_action, record_type=record_type, id_type=id_type, id_value=id_value, attribute_name=attribute_name, attribute_value=attribute_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

