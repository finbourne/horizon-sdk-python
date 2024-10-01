# IntegrationRerunResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**InstanceExecutionReferenceId**](InstanceExecutionReferenceId.md) |  | 

## Example

```python
from finbourne_horizon.models.integration_rerun_response import IntegrationRerunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationRerunResponse from a JSON string
integration_rerun_response_instance = IntegrationRerunResponse.from_json(json)
# print the JSON string representation of the object
print IntegrationRerunResponse.to_json()

# convert the object into a dict
integration_rerun_response_dict = integration_rerun_response_instance.to_dict()
# create an instance of IntegrationRerunResponse from a dict
integration_rerun_response_form_dict = integration_rerun_response.from_dict(integration_rerun_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


