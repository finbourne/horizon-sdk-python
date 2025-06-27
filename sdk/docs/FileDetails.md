# FileDetails

Information associated with files
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**file_type** | **str** |  | [optional] 
**id** | **str** |  | 
## Example

```python
from finbourne_horizon.models.file_details import FileDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

file_name: StrictStr = "example_file_name"
file_type: Optional[StrictStr] = "example_file_type"
id: StrictStr = "example_id"
file_details_instance = FileDetails(file_name=file_name, file_type=file_type, id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

