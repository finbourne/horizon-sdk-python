# FileDetails

Information associated with files

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**file_type** | **str** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from finbourne_horizon.models.file_details import FileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FileDetails from a JSON string
file_details_instance = FileDetails.from_json(json)
# print the JSON string representation of the object
print FileDetails.to_json()

# convert the object into a dict
file_details_dict = file_details_instance.to_dict()
# create an instance of FileDetails from a dict
file_details_form_dict = file_details.from_dict(file_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


