# TpfRetryElementResult

Result for a single batch element retry attempt
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_element_reference_id** | **str** | Batch element reference identifier | 
**status** | **str** | Status of the retry attempt (e.g., \&quot;Retrying\&quot;, \&quot;NotFound\&quot;) | 
## Example

```python
from finbourne_horizon.models.tpf_retry_element_result import TpfRetryElementResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

batch_element_reference_id: StrictStr = "example_batch_element_reference_id"
status: StrictStr = "example_status"
tpf_retry_element_result_instance = TpfRetryElementResult(batch_element_reference_id=batch_element_reference_id, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

