# ProcessSummary

Completed event details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** |  | [optional] 
**category** | **str** |  | [optional] 
**status** | **str** |  | 
**message** | **str** |  | 
**rows** | [**RowDetails**](RowDetails.md) |  | 
**file_details** | [**List[FileDetails]**](FileDetails.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.process_summary import ProcessSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessSummary from a JSON string
process_summary_instance = ProcessSummary.from_json(json)
# print the JSON string representation of the object
print ProcessSummary.to_json()

# convert the object into a dict
process_summary_dict = process_summary_instance.to_dict()
# create an instance of ProcessSummary from a dict
process_summary_form_dict = process_summary.from_dict(process_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


