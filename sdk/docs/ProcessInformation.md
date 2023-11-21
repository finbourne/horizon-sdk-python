# ProcessInformation

Required information for each process

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**process_name** | **str** |  | 
**run_id** | **str** |  | 
**start_time** | **datetime** |  | 
**data_action** | **str** |  | 
**schema_version** | **str** |  | [optional] 
**user_id** | **str** |  | 
**process_summary** | [**ProcessSummary**](ProcessSummary.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.process_information import ProcessInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessInformation from a JSON string
process_information_instance = ProcessInformation.from_json(json)
# print the JSON string representation of the object
print ProcessInformation.to_json()

# convert the object into a dict
process_information_dict = process_information_instance.to_dict()
# create an instance of ProcessInformation from a dict
process_information_form_dict = process_information.from_dict(process_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


