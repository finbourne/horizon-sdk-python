# PagedResourceListOfProcessUpdateResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ProcessUpdateResult]**](ProcessUpdateResult.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.paged_resource_list_of_process_update_result import PagedResourceListOfProcessUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfProcessUpdateResult from a JSON string
paged_resource_list_of_process_update_result_instance = PagedResourceListOfProcessUpdateResult.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfProcessUpdateResult.to_json()

# convert the object into a dict
paged_resource_list_of_process_update_result_dict = paged_resource_list_of_process_update_result_instance.to_dict()
# create an instance of PagedResourceListOfProcessUpdateResult from a dict
paged_resource_list_of_process_update_result_form_dict = paged_resource_list_of_process_update_result.from_dict(paged_resource_list_of_process_update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


