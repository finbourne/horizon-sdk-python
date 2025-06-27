# OnboardInstrumentResponse

Simplified structure converted from the LUSID UpsertInstrumentReponse
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **List[str]** | The instruments which have been successfully updated or created. | 
**failed** | **Dict[str, str]** | The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure. | 
## Example

```python
from finbourne_horizon.models.onboard_instrument_response import OnboardInstrumentResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: conlist(StrictStr) = # Replace with your value
failed: Dict[str, StrictStr] = # Replace with your value
onboard_instrument_response_instance = OnboardInstrumentResponse(href=href, values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

