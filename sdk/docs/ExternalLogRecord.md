# ExternalLogRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logid** | **int** |  | 
**parentlogid** | **int** |  | [optional] 
**loglevel** | **str** |  | 
**logstatus** | **str** |  | 
**sourcerecordtype** | **str** |  | [optional] 
**sourceprimaryidtype** | **str** |  | [optional] 
**sourceprimaryidvalue** | **str** |  | [optional] 
**targetrecordtype** | **str** |  | [optional] 
**targetrecordaction** | **str** |  | [optional] 
**targetprimaryidtype** | **str** |  | [optional] 
**targetprimaryidvalue** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**messagetype** | **str** |  | [optional] 
**timestamp** | **str** |  | 

## Example

```python
from finbourne_horizon.models.external_log_record import ExternalLogRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLogRecord from a JSON string
external_log_record_instance = ExternalLogRecord.from_json(json)
# print the JSON string representation of the object
print ExternalLogRecord.to_json()

# convert the object into a dict
external_log_record_dict = external_log_record_instance.to_dict()
# create an instance of ExternalLogRecord from a dict
external_log_record_form_dict = external_log_record.from_dict(external_log_record_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


