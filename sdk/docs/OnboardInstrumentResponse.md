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

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardInstrumentResponse from a JSON string
onboard_instrument_response_instance = OnboardInstrumentResponse.from_json(json)
# print the JSON string representation of the object
print OnboardInstrumentResponse.to_json()

# convert the object into a dict
onboard_instrument_response_dict = onboard_instrument_response_instance.to_dict()
# create an instance of OnboardInstrumentResponse from a dict
onboard_instrument_response_form_dict = onboard_instrument_response.from_dict(onboard_instrument_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


