# IntegrationPropertyConfiguration

Response containing the description of an integration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The Integration this property configuration applies to | 
**properties** | [**List[PropertyMapping]**](PropertyMapping.md) | The mandatory and optional properties available in this integration | 
**fields** | [**List[FieldMapping]**](FieldMapping.md) | The fields available in this integration | 

## Example

```python
from finbourne_horizon.models.integration_property_configuration import IntegrationPropertyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationPropertyConfiguration from a JSON string
integration_property_configuration_instance = IntegrationPropertyConfiguration.from_json(json)
# print the JSON string representation of the object
print IntegrationPropertyConfiguration.to_json()

# convert the object into a dict
integration_property_configuration_dict = integration_property_configuration_instance.to_dict()
# create an instance of IntegrationPropertyConfiguration from a dict
integration_property_configuration_form_dict = integration_property_configuration.from_dict(integration_property_configuration_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


