# PermIdData

PermId Data Structure
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**figi** | **str** | &gt;FIGI assigned to the instrument. | 
**ticker** | **str** | Ticker assigned to the instrument | 
**mic** | **str** | ISO market identification code(MIC) of the desired instrument(s) | 
**quote_perm_id** | **str** | QuotePermId of the instrument | 
**is_primary_quote** | **bool** | If the quote is primary | 
**legal_entity_identifier** | **str** | LEI assigned to the instrument | [optional] 
## Example

```python
from finbourne_horizon.models.perm_id_data import PermIdData
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

figi: StrictStr = "example_figi"
ticker: StrictStr = "example_ticker"
mic: StrictStr = "example_mic"
quote_perm_id: StrictStr = "example_quote_perm_id"
is_primary_quote: StrictBool = # Replace with your value
is_primary_quote:StrictBool = True
legal_entity_identifier: Optional[StrictStr] = "example_legal_entity_identifier"
perm_id_data_instance = PermIdData(figi=figi, ticker=ticker, mic=mic, quote_perm_id=quote_perm_id, is_primary_quote=is_primary_quote, legal_entity_identifier=legal_entity_identifier)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

