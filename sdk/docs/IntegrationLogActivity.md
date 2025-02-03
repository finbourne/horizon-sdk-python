# IntegrationLogActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**resulting_status** | **str** |  | 
**message_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from finbourne_horizon.models.integration_log_activity import IntegrationLogActivity

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationLogActivity from a JSON string
integration_log_activity_instance = IntegrationLogActivity.from_json(json)
# print the JSON string representation of the object
print IntegrationLogActivity.to_json()

# convert the object into a dict
integration_log_activity_dict = integration_log_activity_instance.to_dict()
# create an instance of IntegrationLogActivity from a dict
integration_log_activity_form_dict = integration_log_activity.from_dict(integration_log_activity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


