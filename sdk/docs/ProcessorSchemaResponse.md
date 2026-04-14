# ProcessorSchemaResponse

DTO ProcessorSchemaResponse fields with JObject
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processor_name** | **str** |  | 
**version** | **str** |  | 
**configuration_schema** | **object** |  | 
## Example

```python
from finbourne_horizon.models.processor_schema_response import ProcessorSchemaResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

processor_name: StrictStr = "example_processor_name"
version: StrictStr = "example_version"
configuration_schema: Optional[Any] = # Replace with your value
processor_schema_response_instance = ProcessorSchemaResponse(processor_name=processor_name, version=version, configuration_schema=configuration_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

