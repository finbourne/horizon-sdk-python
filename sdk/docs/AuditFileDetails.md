# AuditFileDetails

Holds information about Horizon Audit Files
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | [**AuditFileType**](AuditFileType.md) |  | 
**file_path_and_name** | **str** | The file path and name | 
## Example

```python
from finbourne_horizon.models.audit_file_details import AuditFileDetails
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

file_type: AuditFileType = # Replace with your value
file_path_and_name: StrictStr = "example_file_path_and_name"
audit_file_details_instance = AuditFileDetails(file_type=file_type, file_path_and_name=file_path_and_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

