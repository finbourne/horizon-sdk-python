# QueryRequest

Used to control queries, including getting \"pages\" of data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification** | [**QuerySpecification**](QuerySpecification.md) |  | [optional] 

## Example

```python
from finbourne_horizon.models.query_request import QueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryRequest from a JSON string
query_request_instance = QueryRequest.from_json(json)
# print the JSON string representation of the object
print QueryRequest.to_json()

# convert the object into a dict
query_request_dict = query_request_instance.to_dict()
# create an instance of QueryRequest from a dict
query_request_form_dict = query_request.from_dict(query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


