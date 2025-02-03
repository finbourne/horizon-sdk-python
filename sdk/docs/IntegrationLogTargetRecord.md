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

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationLogTargetRecord from a JSON string
integration_log_target_record_instance = IntegrationLogTargetRecord.from_json(json)
# print the JSON string representation of the object
print IntegrationLogTargetRecord.to_json()

# convert the object into a dict
integration_log_target_record_dict = integration_log_target_record_instance.to_dict()
# create an instance of IntegrationLogTargetRecord from a dict
integration_log_target_record_form_dict = integration_log_target_record.from_dict(integration_log_target_record_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


