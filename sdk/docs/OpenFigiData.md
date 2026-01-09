# OpenFigiData

OpenFIGI data structure
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**figi** | **str** | FIGI assigned to the instrument. | 
**name** | **str** | Various attributes of the instrument | [optional] 
**ticker** | **str** | Various attributes of the instrument | [optional] 
**exchange_code** | **str** | Exchange code of the desired instrument(s) | [optional] 
**mic** | **str** | ISO market identification code(MIC) of the desired instrument(s) | [optional] 
**exchange_name** | **str** | Exchange name of the desired instrument(s) | [optional] 
**market_sector** | **str** | Market sector description of the desired instrument(s) | [optional] 
**general_security_type** | **str** | Enum-like attributes of the instrument | [optional] 
**security_type** | **str** | Enum-like attributes of the instrument | [optional] 
**security_description** | **str** | Various attributes of the instrument | [optional] 
**composite_figi** | **str** | Various attributes of the instrument | [optional] 
**share_class_figi** | **str** | Various attributes of the instrument | [optional] 
**match_type** | **str** | Type that the instrument matched against | [optional] 
**search_input** | **str** | Search input used to generate this response | [optional] 
**lusid_instrument_id** | **str** | If an instrument with this FIGI exists, the LUID of that instrument in LUSID | [optional] 
**lusid_instrument_scope** | **str** | If an instrument with this FIGI exists, the Scope of that instrument in LUSID | [optional] 
## Example

```python
from finbourne_horizon.models.open_figi_data import OpenFigiData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

figi: StrictStr = "example_figi"
name: Optional[StrictStr] = "example_name"
ticker: Optional[StrictStr] = "example_ticker"
exchange_code: Optional[StrictStr] = "example_exchange_code"
mic: Optional[StrictStr] = "example_mic"
exchange_name: Optional[StrictStr] = "example_exchange_name"
market_sector: Optional[StrictStr] = "example_market_sector"
general_security_type: Optional[StrictStr] = "example_general_security_type"
security_type: Optional[StrictStr] = "example_security_type"
security_description: Optional[StrictStr] = "example_security_description"
composite_figi: Optional[StrictStr] = "example_composite_figi"
share_class_figi: Optional[StrictStr] = "example_share_class_figi"
match_type: Optional[StrictStr] = "example_match_type"
search_input: Optional[StrictStr] = "example_search_input"
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
lusid_instrument_scope: Optional[StrictStr] = "example_lusid_instrument_scope"
open_figi_data_instance = OpenFigiData(figi=figi, name=name, ticker=ticker, exchange_code=exchange_code, mic=mic, exchange_name=exchange_name, market_sector=market_sector, general_security_type=general_security_type, security_type=security_type, security_description=security_description, composite_figi=composite_figi, share_class_figi=share_class_figi, match_type=match_type, search_input=search_input, lusid_instrument_id=lusid_instrument_id, lusid_instrument_scope=lusid_instrument_scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

