# ReplayOptions

Optional parameters for replay operations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_publication_status** | **str** | Override publication status for all transactions (e.g., force as \&quot;New\&quot;). | [optional] 
## Example

```python
from finbourne_horizon.models.replay_options import ReplayOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

override_publication_status: Optional[StrictStr] = "example_override_publication_status"
replay_options_instance = ReplayOptions(override_publication_status=override_publication_status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

