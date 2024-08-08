# IntegrationInstance

Response containing an integration instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the instance within the integration. | 
**integration_type** | **str** | The integration type. | 
**name** | **str** | Name of the instance. | 
**description** | **str** | Description of the instance. | 
**enabled** | **bool** | If true the instance will be executed if its trigger is satisfied. | 
**triggers** | [**List[Trigger]**](Trigger.md) | Defines what triggers execution of the instance. | 
**details** | **object** |  | 

## Example

```python
from finbourne_horizon.models.integration_instance import IntegrationInstance

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationInstance from a JSON string
integration_instance_instance = IntegrationInstance.from_json(json)
# print the JSON string representation of the object
print IntegrationInstance.to_json()

# convert the object into a dict
integration_instance_dict = integration_instance_instance.to_dict()
# create an instance of IntegrationInstance from a dict
integration_instance_form_dict = integration_instance.from_dict(integration_instance_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


