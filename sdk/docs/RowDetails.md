# RowDetails

Information about the nuber of rows processed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows_total** | **int** | The number of rows processed. | [optional] 
**rows_succeeded** | **int** | The number of rows that were successfully processed. | [optional] 
**rows_ignored** | **int** | The number of rows that were not processed. | [optional] 
**rows_failed** | **int** | The number of rows that failed when being processed. | [optional] 
## Example

```python
from finbourne_horizon.models.row_details import RowDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rows_total: Optional[StrictInt] = # Replace with your value
rows_total: Optional[StrictInt] = None
rows_succeeded: Optional[StrictInt] = # Replace with your value
rows_succeeded: Optional[StrictInt] = None
rows_ignored: Optional[StrictInt] = # Replace with your value
rows_ignored: Optional[StrictInt] = None
rows_failed: Optional[StrictInt] = # Replace with your value
rows_failed: Optional[StrictInt] = None
row_details_instance = RowDetails(rows_total=rows_total, rows_succeeded=rows_succeeded, rows_ignored=rows_ignored, rows_failed=rows_failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

