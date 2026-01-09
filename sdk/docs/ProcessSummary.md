# ProcessSummary

Completed event details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** |  | [optional] 
**category** | **str** |  | [optional] 
**status** | **str** |  | 
**message** | **str** |  | 
**rows** | [**RowDetails**](RowDetails.md) |  | 
**file_details** | [**List[FileDetails]**](FileDetails.md) |  | [optional] 
## Example

```python
from finbourne_horizon.models.process_summary import ProcessSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

end_time: Optional[datetime] = # Replace with your value
category: Optional[StrictStr] = "example_category"
status: StrictStr = "example_status"
message: StrictStr = "example_message"
rows: RowDetails
file_details: Optional[List[FileDetails]] = # Replace with your value
process_summary_instance = ProcessSummary(end_time=end_time, category=category, status=status, message=message, rows=rows, file_details=file_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

