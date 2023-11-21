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

# TODO update the JSON string below
json = "{}"
# create an instance of OpenFigiData from a JSON string
open_figi_data_instance = OpenFigiData.from_json(json)
# print the JSON string representation of the object
print OpenFigiData.to_json()

# convert the object into a dict
open_figi_data_dict = open_figi_data_instance.to_dict()
# create an instance of OpenFigiData from a dict
open_figi_data_form_dict = open_figi_data.from_dict(open_figi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


