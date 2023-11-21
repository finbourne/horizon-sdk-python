# RowDetails

Information about the nuber of rows processed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows_total** | **int** | The number of rows processed. | [optional] 
**rows_succeeded** | **int** | The number of rows that were successfully processed. | [optional] 
**rows_ignored** | **int** | The number of rows that were not processed. | [optional] 
**rows_failed** | **int** | The number of rows that failed when being processed. | [optional] 

## Example

```python
from finbourne_horizon.models.row_details import RowDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RowDetails from a JSON string
row_details_instance = RowDetails.from_json(json)
# print the JSON string representation of the object
print RowDetails.to_json()

# convert the object into a dict
row_details_dict = row_details_instance.to_dict()
# create an instance of RowDetails from a dict
row_details_form_dict = row_details.from_dict(row_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


