# IntegrationRunResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**instance_id** | **str** |  | [optional] 
**instance_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**integration** | [**IntegrationRunIntegration**](IntegrationRunIntegration.md) |  | 
**version** | [**IntegrationRunVersion**](IntegrationRunVersion.md) |  | 
**integration_logs** | **Dict[str, Dict[str, IntegrationRunLog]]** |  | [optional] 

## Example

```python
from finbourne_horizon.models.integration_run_response import IntegrationRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationRunResponse from a JSON string
integration_run_response_instance = IntegrationRunResponse.from_json(json)
# print the JSON string representation of the object
print IntegrationRunResponse.to_json()

# convert the object into a dict
integration_run_response_dict = integration_run_response_instance.to_dict()
# create an instance of IntegrationRunResponse from a dict
integration_run_response_form_dict = integration_run_response.from_dict(integration_run_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


