# ExternalLogInsertionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[ExternalLogRecord]**](ExternalLogRecord.md) |  | 

## Example

```python
from finbourne_horizon.models.external_log_insertion_request import ExternalLogInsertionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLogInsertionRequest from a JSON string
external_log_insertion_request_instance = ExternalLogInsertionRequest.from_json(json)
# print the JSON string representation of the object
print ExternalLogInsertionRequest.to_json()

# convert the object into a dict
external_log_insertion_request_dict = external_log_insertion_request_instance.to_dict()
# create an instance of ExternalLogInsertionRequest from a dict
external_log_insertion_request_form_dict = external_log_insertion_request.from_dict(external_log_insertion_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


