# OpenFigiSearchResult

Response coming back from a search request to OpenFIGI

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OpenFigiData]**](OpenFigiData.md) | Enumerable list of OpenFIGI results | 
**perm_id_uri** | **str** | URI of the related PermID response, if requested | [optional] 

## Example

```python
from finbourne_horizon.models.open_figi_search_result import OpenFigiSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of OpenFigiSearchResult from a JSON string
open_figi_search_result_instance = OpenFigiSearchResult.from_json(json)
# print the JSON string representation of the object
print OpenFigiSearchResult.to_json()

# convert the object into a dict
open_figi_search_result_dict = open_figi_search_result_instance.to_dict()
# create an instance of OpenFigiSearchResult from a dict
open_figi_search_result_form_dict = open_figi_search_result.from_dict(open_figi_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


