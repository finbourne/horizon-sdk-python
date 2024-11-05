# JSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 
**reference** | **str** |  | [optional] 
**ref** | [**JSchema**](JSchema.md) |  | [optional] 
**recursive_reference** | **str** |  | [optional] 
**recursive_anchor** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**anchor** | **str** |  | [optional] 
**type** | [**JSchemaType**](JSchemaType.md) |  | [optional] 
**default** | **object** |  | [optional] 
**properties** | [**Dict[str, JSchema]**](JSchema.md) |  | [readonly] 
**items** | [**List[JSchema]**](JSchema.md) |  | [readonly] 
**items_position_validation** | **bool** |  | 
**required** | **List[str]** |  | [readonly] 
**all_of** | [**List[JSchema]**](JSchema.md) |  | [readonly] 
**any_of** | [**List[JSchema]**](JSchema.md) |  | [readonly] 
**one_of** | [**List[JSchema]**](JSchema.md) |  | [readonly] 
**var_if** | [**JSchema**](JSchema.md) |  | [optional] 
**then** | [**JSchema**](JSchema.md) |  | [optional] 
**var_else** | [**JSchema**](JSchema.md) |  | [optional] 
**var_not** | [**JSchema**](JSchema.md) |  | [optional] 
**contains** | [**JSchema**](JSchema.md) |  | [optional] 
**property_names** | [**JSchema**](JSchema.md) |  | [optional] 
**enum** | **List[object]** |  | [readonly] 
**const** | **object** |  | [optional] 
**unique_items** | **bool** |  | 
**minimum_length** | **int** |  | [optional] 
**maximum_length** | **int** |  | [optional] 
**minimum** | **float** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_minimum** | **bool** |  | 
**exclusive_maximum** | **bool** |  | 
**minimum_items** | **int** |  | [optional] 
**maximum_items** | **int** |  | [optional] 
**minimum_properties** | **int** |  | [optional] 
**maximum_properties** | **int** |  | [optional] 
**minimum_contains** | **int** |  | [optional] 
**maximum_contains** | **int** |  | [optional] 
**content_encoding** | **str** |  | [optional] 
**content_media_type** | **str** |  | [optional] 
**write_only** | **bool** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**extension_data** | **Dict[str, object]** |  | [readonly] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**multiple_of** | **float** |  | [optional] 
**pattern** | **str** |  | [optional] 
**dependencies** | **Dict[str, object]** |  | [readonly] 
**dependent_required** | **Dict[str, List[str]]** |  | [readonly] 
**dependent_schemas** | [**Dict[str, JSchema]**](JSchema.md) |  | [readonly] 
**pattern_properties** | [**Dict[str, JSchema]**](JSchema.md) |  | [readonly] 
**additional_properties** | [**JSchema**](JSchema.md) |  | [optional] 
**allow_additional_properties** | **bool** |  | 
**allow_additional_properties_specified** | **bool** |  | 
**unevaluated_properties** | [**JSchema**](JSchema.md) |  | [optional] 
**allow_unevaluated_properties** | **bool** |  | [optional] 
**additional_items** | [**JSchema**](JSchema.md) |  | [optional] 
**allow_additional_items** | **bool** |  | 
**allow_additional_items_specified** | **bool** |  | 
**unevaluated_items** | [**JSchema**](JSchema.md) |  | [optional] 
**allow_unevaluated_items** | **bool** |  | [optional] 
**format** | **str** |  | [optional] 
**validators** | **List[object]** |  | [readonly] 

## Example

```python
from finbourne_horizon.models.j_schema import JSchema

# TODO update the JSON string below
json = "{}"
# create an instance of JSchema from a JSON string
j_schema_instance = JSchema.from_json(json)
# print the JSON string representation of the object
print JSchema.to_json()

# convert the object into a dict
j_schema_dict = j_schema_instance.to_dict()
# create an instance of JSchema from a dict
j_schema_form_dict = j_schema.from_dict(j_schema_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


