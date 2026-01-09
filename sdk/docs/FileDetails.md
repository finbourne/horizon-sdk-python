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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

file_name: StrictStr = "example_file_name"
file_type: Optional[StrictStr] = "example_file_type"
id: StrictStr = "example_id"
file_details_instance = FileDetails(file_name=file_name, file_type=file_type, id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

