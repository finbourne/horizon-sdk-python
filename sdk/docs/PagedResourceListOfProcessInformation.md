# PagedResourceListOfProcessInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ProcessInformation]**](ProcessInformation.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.paged_resource_list_of_process_information import PagedResourceListOfProcessInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfProcessInformation from a JSON string
paged_resource_list_of_process_information_instance = PagedResourceListOfProcessInformation.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfProcessInformation.to_json()

# convert the object into a dict
paged_resource_list_of_process_information_dict = paged_resource_list_of_process_information_instance.to_dict()
# create an instance of PagedResourceListOfProcessInformation from a dict
paged_resource_list_of_process_information_form_dict = paged_resource_list_of_process_information.from_dict(paged_resource_list_of_process_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


