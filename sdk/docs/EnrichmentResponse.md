# EnrichmentResponse

Collated enrichment result information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enriched_instruments** | **List[str]** |  | 
**ignored_instruments** | **List[str]** |  | 
**error_file_id** | **str** | Error File ID, if one was created | [optional] 

## Example

```python
from finbourne_horizon.models.enrichment_response import EnrichmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentResponse from a JSON string
enrichment_response_instance = EnrichmentResponse.from_json(json)
# print the JSON string representation of the object
print EnrichmentResponse.to_json()

# convert the object into a dict
enrichment_response_dict = enrichment_response_instance.to_dict()
# create an instance of EnrichmentResponse from a dict
enrichment_response_form_dict = enrichment_response.from_dict(enrichment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


