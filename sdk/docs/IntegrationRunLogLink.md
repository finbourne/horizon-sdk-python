# IntegrationRunLogLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | 
**description** | **str** |  | 
## Example

```python
from finbourne_horizon.models.integration_run_log_link import IntegrationRunLogLink
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: StrictStr = "example_href"
description: StrictStr = "example_description"
integration_run_log_link_instance = IntegrationRunLogLink(href=href, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

