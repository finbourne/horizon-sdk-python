# ProcessUpdateResult

Shows details relevant to update events for a query

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**entry_id** | **str** |  | 
**process_name** | **str** |  | 
**run_id** | **str** |  | 
**entry_date** | **datetime** |  | 
**status** | **str** |  | 
**message** | **str** |  | 
**schema_version** | **str** |  | [optional] 

## Example

```python
from finbourne_horizon.models.process_update_result import ProcessUpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessUpdateResult from a JSON string
process_update_result_instance = ProcessUpdateResult.from_json(json)
# print the JSON string representation of the object
print ProcessUpdateResult.to_json()

# convert the object into a dict
process_update_result_dict = process_update_result_instance.to_dict()
# create an instance of ProcessUpdateResult from a dict
process_update_result_form_dict = process_update_result.from_dict(process_update_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


