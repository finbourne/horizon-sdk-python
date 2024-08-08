# QuerySpecification

Defines the information that can be used to query a set of data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of results to be returned in a \&quot;page\&quot; | [optional] 

## Example

```python
from finbourne_horizon.models.query_specification import QuerySpecification

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySpecification from a JSON string
query_specification_instance = QuerySpecification.from_json(json)
# print the JSON string representation of the object
print QuerySpecification.to_json()

# convert the object into a dict
query_specification_dict = query_specification_instance.to_dict()
# create an instance of QuerySpecification from a dict
query_specification_form_dict = query_specification.from_dict(query_specification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


