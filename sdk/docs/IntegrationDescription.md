# IntegrationDescription

Response containing the description of an integration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Unique identifier of the integration e.g. \&quot;copp-clark\&quot;. | 
**name** | **str** | Readable name of the integration e.g. \&quot;Copp Clark\&quot;. | 
**description** | **str** | Describes the purpose of the integration. | 
**supported_trigger_types** | **List[str]** | Trigger types (Time, File) the integration supports. | 
**licensed** | **bool** | True if your domain is licensed to use this integration, otherwise false. | 

## Example

```python
from finbourne_horizon.models.integration_description import IntegrationDescription

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDescription from a JSON string
integration_description_instance = IntegrationDescription.from_json(json)
# print the JSON string representation of the object
print IntegrationDescription.to_json()

# convert the object into a dict
integration_description_dict = integration_description_instance.to_dict()
# create an instance of IntegrationDescription from a dict
integration_description_form_dict = integration_description.from_dict(integration_description_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


