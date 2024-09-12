# IntegrationRunVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_created** | **datetime** |  | [optional] 
**as_at_modified** | **datetime** |  | [optional] 

## Example

```python
from finbourne_horizon.models.integration_run_version import IntegrationRunVersion

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationRunVersion from a JSON string
integration_run_version_instance = IntegrationRunVersion.from_json(json)
# print the JSON string representation of the object
print IntegrationRunVersion.to_json()

# convert the object into a dict
integration_run_version_dict = integration_run_version_instance.to_dict()
# create an instance of IntegrationRunVersion from a dict
integration_run_version_form_dict = integration_run_version.from_dict(integration_run_version_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


