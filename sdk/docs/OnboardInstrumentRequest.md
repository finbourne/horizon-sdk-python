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

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardInstrumentRequest from a JSON string
onboard_instrument_request_instance = OnboardInstrumentRequest.from_json(json)
# print the JSON string representation of the object
print OnboardInstrumentRequest.to_json()

# convert the object into a dict
onboard_instrument_request_dict = onboard_instrument_request_instance.to_dict()
# create an instance of OnboardInstrumentRequest from a dict
onboard_instrument_request_form_dict = onboard_instrument_request.from_dict(onboard_instrument_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


