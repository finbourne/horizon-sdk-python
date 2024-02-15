# AuditUpdateResponse

Response type for Horizon Audit Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_name** | **str** | The name of the Process the events will be visible under | 

## Example

```python
from finbourne_horizon.models.audit_update_response import AuditUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditUpdateResponse from a JSON string
audit_update_response_instance = AuditUpdateResponse.from_json(json)
# print the JSON string representation of the object
print AuditUpdateResponse.to_json()

# convert the object into a dict
audit_update_response_dict = audit_update_response_instance.to_dict()
# create an instance of AuditUpdateResponse from a dict
audit_update_response_form_dict = audit_update_response.from_dict(audit_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


