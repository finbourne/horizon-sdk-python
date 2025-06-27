# EnrichmentResponse

Collated enrichment result information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enriched_instruments** | **List[str]** |  | 
**ignored_instruments** | **List[str]** |  | 
**error_file_id** | **str** | Error File ID, if one was created | [optional] 
## Example

```python
from finbourne_horizon.models.enrichment_response import EnrichmentResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

enriched_instruments: conlist(StrictStr) = # Replace with your value
ignored_instruments: conlist(StrictStr) = # Replace with your value
error_file_id: Optional[StrictStr] = "example_error_file_id"
enrichment_response_instance = EnrichmentResponse(enriched_instruments=enriched_instruments, ignored_instruments=ignored_instruments, error_file_id=error_file_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

