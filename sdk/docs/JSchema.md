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
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist

schema_version: Optional[StrictStr] = "example_schema_version"
valid: Optional[StrictBool] = None
valid:Optional[StrictBool] = None
reference: Optional[StrictStr] = "example_reference"
ref: Optional[JSchema] = None
recursive_reference: Optional[StrictStr] = "example_recursive_reference"
recursive_anchor: Optional[StrictBool] = # Replace with your value
recursive_anchor:Optional[StrictBool] = None
id: Optional[StrictStr] = "example_id"
anchor: Optional[StrictStr] = "example_anchor"
type: Optional[JSchemaType] = None
default: Optional[Any] = None
properties: Dict[str, JSchema] = # Replace with your value
items: conlist(JSchema) = # Replace with your value
items_position_validation: StrictBool = # Replace with your value
items_position_validation:StrictBool = True
required: conlist(StrictStr) = # Replace with your value
all_of: conlist(JSchema) = # Replace with your value
any_of: conlist(JSchema) = # Replace with your value
one_of: conlist(JSchema) = # Replace with your value
var_if: Optional[JSchema] = # Replace with your value
then: Optional[JSchema] = None
var_else: Optional[JSchema] = # Replace with your value
var_not: Optional[JSchema] = # Replace with your value
contains: Optional[JSchema] = None
property_names: Optional[JSchema] = # Replace with your value
enum: conlist(Any) = # Replace with your value
const: Optional[Any] = None
unique_items: StrictBool = # Replace with your value
unique_items:StrictBool = True
minimum_length: Optional[StrictInt] = # Replace with your value
maximum_length: Optional[StrictInt] = # Replace with your value
minimum: Optional[Union[StrictFloat, StrictInt]] = None
maximum: Optional[Union[StrictFloat, StrictInt]] = None
exclusive_minimum: StrictBool = # Replace with your value
exclusive_minimum:StrictBool = True
exclusive_maximum: StrictBool = # Replace with your value
exclusive_maximum:StrictBool = True
minimum_items: Optional[StrictInt] = # Replace with your value
maximum_items: Optional[StrictInt] = # Replace with your value
minimum_properties: Optional[StrictInt] = # Replace with your value
maximum_properties: Optional[StrictInt] = # Replace with your value
minimum_contains: Optional[StrictInt] = # Replace with your value
maximum_contains: Optional[StrictInt] = # Replace with your value
content_encoding: Optional[StrictStr] = "example_content_encoding"
content_media_type: Optional[StrictStr] = "example_content_media_type"
write_only: Optional[StrictBool] = # Replace with your value
write_only:Optional[StrictBool] = None
read_only: Optional[StrictBool] = # Replace with your value
read_only:Optional[StrictBool] = None
extension_data: Dict[str, Any] = # Replace with your value
title: Optional[StrictStr] = "example_title"
description: Optional[StrictStr] = "example_description"
multiple_of: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pattern: Optional[StrictStr] = "example_pattern"
dependencies: Dict[str, Any] = # Replace with your value
dependent_required: Dict[str, conlist(StrictStr)] = # Replace with your value
dependent_schemas: Dict[str, JSchema] = # Replace with your value
pattern_properties: Dict[str, JSchema] = # Replace with your value
additional_properties: Optional[JSchema] = # Replace with your value
allow_additional_properties: StrictBool = # Replace with your value
allow_additional_properties:StrictBool = True
allow_additional_properties_specified: StrictBool = # Replace with your value
allow_additional_properties_specified:StrictBool = True
unevaluated_properties: Optional[JSchema] = # Replace with your value
allow_unevaluated_properties: Optional[StrictBool] = # Replace with your value
allow_unevaluated_properties:Optional[StrictBool] = None
additional_items: Optional[JSchema] = # Replace with your value
allow_additional_items: StrictBool = # Replace with your value
allow_additional_items:StrictBool = True
allow_additional_items_specified: StrictBool = # Replace with your value
allow_additional_items_specified:StrictBool = True
unevaluated_items: Optional[JSchema] = # Replace with your value
allow_unevaluated_items: Optional[StrictBool] = # Replace with your value
allow_unevaluated_items:Optional[StrictBool] = None
format: Optional[StrictStr] = "example_format"
validators: conlist(Dict[str, Any]) = # Replace with your value
j_schema_instance = JSchema(schema_version=schema_version, valid=valid, reference=reference, ref=ref, recursive_reference=recursive_reference, recursive_anchor=recursive_anchor, id=id, anchor=anchor, type=type, default=default, properties=properties, items=items, items_position_validation=items_position_validation, required=required, all_of=all_of, any_of=any_of, one_of=one_of, var_if=var_if, then=then, var_else=var_else, var_not=var_not, contains=contains, property_names=property_names, enum=enum, const=const, unique_items=unique_items, minimum_length=minimum_length, maximum_length=maximum_length, minimum=minimum, maximum=maximum, exclusive_minimum=exclusive_minimum, exclusive_maximum=exclusive_maximum, minimum_items=minimum_items, maximum_items=maximum_items, minimum_properties=minimum_properties, maximum_properties=maximum_properties, minimum_contains=minimum_contains, maximum_contains=maximum_contains, content_encoding=content_encoding, content_media_type=content_media_type, write_only=write_only, read_only=read_only, extension_data=extension_data, title=title, description=description, multiple_of=multiple_of, pattern=pattern, dependencies=dependencies, dependent_required=dependent_required, dependent_schemas=dependent_schemas, pattern_properties=pattern_properties, additional_properties=additional_properties, allow_additional_properties=allow_additional_properties, allow_additional_properties_specified=allow_additional_properties_specified, unevaluated_properties=unevaluated_properties, allow_unevaluated_properties=allow_unevaluated_properties, additional_items=additional_items, allow_additional_items=allow_additional_items, allow_additional_items_specified=allow_additional_items_specified, unevaluated_items=unevaluated_items, allow_unevaluated_items=allow_unevaluated_items, format=format, validators=validators)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

