# AuditCompleteResponse

Response type for Horizon Audit Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_name** | **str** | The name of the Process the events will be visible under | 

## Example

```python
from finbourne_horizon.models.audit_complete_response import AuditCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditCompleteResponse from a JSON string
audit_complete_response_instance = AuditCompleteResponse.from_json(json)
# print the JSON string representation of the object
print AuditCompleteResponse.to_json()

# convert the object into a dict
audit_complete_response_dict = audit_complete_response_instance.to_dict()
# create an instance of AuditCompleteResponse from a dict
audit_complete_response_form_dict = audit_complete_response.from_dict(audit_complete_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


