# PagedResourceListOfIntegrationRunResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[IntegrationRunResponse]**](IntegrationRunResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.paged_resource_list_of_integration_run_response import PagedResourceListOfIntegrationRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfIntegrationRunResponse from a JSON string
paged_resource_list_of_integration_run_response_instance = PagedResourceListOfIntegrationRunResponse.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfIntegrationRunResponse.to_json()

# convert the object into a dict
paged_resource_list_of_integration_run_response_dict = paged_resource_list_of_integration_run_response_instance.to_dict()
# create an instance of PagedResourceListOfIntegrationRunResponse from a dict
paged_resource_list_of_integration_run_response_form_dict = paged_resource_list_of_integration_run_response.from_dict(paged_resource_list_of_integration_run_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


