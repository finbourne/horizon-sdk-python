# Identifiers

A list of lusid instrument ids

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lusid_instrument_ids** | **List[str]** |  | 

## Example

```python
from finbourne_horizon.models.identifiers import Identifiers

# TODO update the JSON string below
json = "{}"
# create an instance of Identifiers from a JSON string
identifiers_instance = Identifiers.from_json(json)
# print the JSON string representation of the object
print Identifiers.to_json()

# convert the object into a dict
identifiers_dict = identifiers_instance.to_dict()
# create an instance of Identifiers from a dict
identifiers_form_dict = identifiers.from_dict(identifiers_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


