# Identifiers

A list of lusid instrument ids
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_ids** | **List[str]** | The collection of LUSID instrument identifiers | 
## Example

```python
from finbourne_horizon.models.identifiers import Identifiers
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

lusid_instrument_ids: conlist(StrictStr) = # Replace with your value
identifiers_instance = Identifiers(lusid_instrument_ids=lusid_instrument_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

