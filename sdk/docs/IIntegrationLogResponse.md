# IIntegrationLogResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **int** |  | [readonly] 
**run_id** | **str** |  | [optional] [readonly] 
**parent_log_id** | **int** |  | [optional] [readonly] 
**log_type** | **str** |  | [readonly] 
**first_activity** | **datetime** |  | [optional] [readonly] 
**last_activity** | **datetime** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**source_record** | [**IntegrationLogRecord**](IntegrationLogRecord.md) |  | [optional] 
**target_record** | [**IntegrationLogTargetRecord**](IntegrationLogTargetRecord.md) |  | [optional] 
**activities** | [**List[IntegrationLogActivity]**](IntegrationLogActivity.md) |  | [readonly] 

## Example

```python
from finbourne_horizon.models.i_integration_log_response import IIntegrationLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IIntegrationLogResponse from a JSON string
i_integration_log_response_instance = IIntegrationLogResponse.from_json(json)
# print the JSON string representation of the object
print IIntegrationLogResponse.to_json()

# convert the object into a dict
i_integration_log_response_dict = i_integration_log_response_instance.to_dict()
# create an instance of IIntegrationLogResponse from a dict
i_integration_log_response_form_dict = i_integration_log_response.from_dict(i_integration_log_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


