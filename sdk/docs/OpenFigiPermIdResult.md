# OpenFigiPermIdResult

A packed WebAPI OpenFigi DTO and PermId DTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_figi_result** | [**OpenFigiData**](OpenFigiData.md) |  | 
**perm_id_result** | [**PermIdData**](PermIdData.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.open_figi_perm_id_result import OpenFigiPermIdResult

# TODO update the JSON string below
json = "{}"
# create an instance of OpenFigiPermIdResult from a JSON string
open_figi_perm_id_result_instance = OpenFigiPermIdResult.from_json(json)
# print the JSON string representation of the object
print OpenFigiPermIdResult.to_json()

# convert the object into a dict
open_figi_perm_id_result_dict = open_figi_perm_id_result_instance.to_dict()
# create an instance of OpenFigiPermIdResult from a dict
open_figi_perm_id_result_form_dict = open_figi_perm_id_result.from_dict(open_figi_perm_id_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


