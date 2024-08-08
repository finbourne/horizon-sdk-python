# AuditFileDetails

Holds information about Horizon Audit Files

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | [**AuditFileType**](AuditFileType.md) |  | 
**file_path_and_name** | **str** |  | 

## Example

```python
from finbourne_horizon.models.audit_file_details import AuditFileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuditFileDetails from a JSON string
audit_file_details_instance = AuditFileDetails.from_json(json)
# print the JSON string representation of the object
print AuditFileDetails.to_json()

# convert the object into a dict
audit_file_details_dict = audit_file_details_instance.to_dict()
# create an instance of AuditFileDetails from a dict
audit_file_details_form_dict = audit_file_details.from_dict(audit_file_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


