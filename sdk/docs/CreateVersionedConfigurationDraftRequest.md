# CreateVersionedConfigurationDraftRequest

Request to create a new draft versioned configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**major_version** | **int** | The major version for the new draft. Must be supplied together with minorVersion, or both omitted to auto-assign the next version. | [optional] 
**minor_version** | **int** | The minor version for the new draft. Must be supplied together with MajorVersion, or both omitted to auto-assign the next version. | [optional] 
**source_major_version** | **int** | The major version of an existing record to copy the value from. Must be supplied together with SourceMinorVersion. If omitted, the new draft is initialised with an empty JSON object. | [optional] 
**source_minor_version** | **int** | The minor version of an existing record to copy the value from. Must be supplied together with SourceMajorVersion. If omitted, the new draft is initialised with an empty JSON object. | [optional] 
## Example

```python
from finbourne_horizon.models.create_versioned_configuration_draft_request import CreateVersionedConfigurationDraftRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

major_version: Optional[StrictInt] = # Replace with your value
major_version: Optional[StrictInt] = None
minor_version: Optional[StrictInt] = # Replace with your value
minor_version: Optional[StrictInt] = None
source_major_version: Optional[StrictInt] = # Replace with your value
source_major_version: Optional[StrictInt] = None
source_minor_version: Optional[StrictInt] = # Replace with your value
source_minor_version: Optional[StrictInt] = None
create_versioned_configuration_draft_request_instance = CreateVersionedConfigurationDraftRequest(major_version=major_version, minor_version=minor_version, source_major_version=source_major_version, source_minor_version=source_minor_version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

