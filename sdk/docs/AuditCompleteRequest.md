# AuditCompleteRequest

An incoming request for a Horizon Complete Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID identifiying the source of the event | 
**user_id** | **str** | A unique ID identifiying who owns the schedule | 
**scheduler_run_id** | **str** | The GUID of the schedule run | 
**start_time** | **datetime** | When the run was started in UTC | 
**end_time** | **datetime** | When the run finished in UTC | 
**message** | **str** | A descriptive message to accompany the status | 
**status** | [**AuditCompleteStatus**](AuditCompleteStatus.md) |  | 
**rows_total** | **int** | The number of data rows operated on | 
**rows_succeeded** | **int** | The number of data rows successfully operated on | 
**rows_failed** | **int** | The number of data rows that failed to be operated on | 
**rows_ignored** | **int** | The number of data rows that had no actions taken | 
**audit_files** | [**List[AuditFileDetails]**](AuditFileDetails.md) | A list of file details for attaching to the event | 
**process_name_override** | **str** | Optional Name for how the process appears in Data Feed Monitoring | [optional] 

## Example

```python
from finbourne_horizon.models.audit_complete_request import AuditCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCompleteRequest from a JSON string
audit_complete_request_instance = AuditCompleteRequest.from_json(json)
# print the JSON string representation of the object
print AuditCompleteRequest.to_json()

# convert the object into a dict
audit_complete_request_dict = audit_complete_request_instance.to_dict()
# create an instance of AuditCompleteRequest from a dict
audit_complete_request_form_dict = audit_complete_request.from_dict(audit_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


