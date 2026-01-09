# OnboardInstrumentRequest

The full structure of a instrument creation / onboarding request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_results** | [**List[OpenFigiPermIdResult]**](OpenFigiPermIdResult.md) | Enumerable packed OpenFigi/PermId information used to create instruments | 
**primary_vendor_key** | **str** | Primary vendor used to master instrument from Unknown to an asset type | [optional] 
**secondary_vendor_keys** | **List[str]** | Secondary vendors used to decorate additional properties | [optional] 
## Example

```python
from finbourne_horizon.models.onboard_instrument_request import OnboardInstrumentRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data_results: List[OpenFigiPermIdResult] = # Replace with your value
primary_vendor_key: Optional[StrictStr] = "example_primary_vendor_key"
secondary_vendor_keys: Optional[List[StrictStr]] = # Replace with your value
onboard_instrument_request_instance = OnboardInstrumentRequest(data_results=data_results, primary_vendor_key=primary_vendor_key, secondary_vendor_keys=secondary_vendor_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

