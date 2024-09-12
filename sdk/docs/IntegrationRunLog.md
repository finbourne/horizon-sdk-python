# IntegrationRunLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**link** | [**IntegrationRunLogLink**](IntegrationRunLogLink.md) |  | 

## Example

```python
from finbourne_horizon.models.integration_run_log import IntegrationRunLog

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationRunLog from a JSON string
integration_run_log_instance = IntegrationRunLog.from_json(json)
# print the JSON string representation of the object
print IntegrationRunLog.to_json()

# convert the object into a dict
integration_run_log_dict = integration_run_log_instance.to_dict()
# create an instance of IntegrationRunLog from a dict
integration_run_log_form_dict = integration_run_log.from_dict(integration_run_log_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


