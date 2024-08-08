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

# TODO update the JSON string below
json = "{}"
# create an instance of PermIdData from a JSON string
perm_id_data_instance = PermIdData.from_json(json)
# print the JSON string representation of the object
print PermIdData.to_json()

# convert the object into a dict
perm_id_data_dict = perm_id_data_instance.to_dict()
# create an instance of PermIdData from a dict
perm_id_data_form_dict = perm_id_data.from_dict(perm_id_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


