# AuditUpdateRequest

An incoming request for a Horizon Update Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique ID identifiying the source of the event | 
**user_id** | **str** | A unique ID identifiying who owns the schedule | 
**scheduler_run_id** | **str** | The GUID of the schedule run | 
**start_time** | **datetime** | When the run was started in UTC | 
**message** | **str** | A descriptive message to accompany the status | 
**process_name_override** | **str** | Optional Name for how the process appears in Data Feed Monitoring | [optional] 

## Example

```python
from finbourne_horizon.models.audit_update_request import AuditUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditUpdateRequest from a JSON string
audit_update_request_instance = AuditUpdateRequest.from_json(json)
# print the JSON string representation of the object
print AuditUpdateRequest.to_json()

# convert the object into a dict
audit_update_request_dict = audit_update_request_instance.to_dict()
# create an instance of AuditUpdateRequest from a dict
audit_update_request_form_dict = audit_update_request.from_dict(audit_update_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


