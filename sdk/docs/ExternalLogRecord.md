# ExternalLogRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logid** | **int** |  | 
**parentlogid** | **int** |  | [optional] 
**loglevel** | **str** |  | 
**logstatus** | **str** |  | 
**sourcerecordtype** | **str** |  | [optional] 
**sourceprimaryidtype** | **str** |  | [optional] 
**sourceprimaryidvalue** | **str** |  | [optional] 
**targetrecordtype** | **str** |  | [optional] 
**targetrecordaction** | **str** |  | [optional] 
**targetprimaryidtype** | **str** |  | [optional] 
**targetprimaryidvalue** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**messagetype** | **str** |  | [optional] 
**timestamp** | **str** |  | 
## Example

```python
from finbourne_horizon.models.external_log_record import ExternalLogRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

logid: StrictInt
parentlogid: Optional[StrictInt] = None
loglevel: StrictStr = "example_loglevel"
logstatus: StrictStr = "example_logstatus"
sourcerecordtype: Optional[StrictStr] = "example_sourcerecordtype"
sourceprimaryidtype: Optional[StrictStr] = "example_sourceprimaryidtype"
sourceprimaryidvalue: Optional[StrictStr] = "example_sourceprimaryidvalue"
targetrecordtype: Optional[StrictStr] = "example_targetrecordtype"
targetrecordaction: Optional[StrictStr] = "example_targetrecordaction"
targetprimaryidtype: Optional[StrictStr] = "example_targetprimaryidtype"
targetprimaryidvalue: Optional[StrictStr] = "example_targetprimaryidvalue"
message: Optional[StrictStr] = "example_message"
messagetype: Optional[StrictStr] = "example_messagetype"
timestamp: StrictStr = "example_timestamp"
external_log_record_instance = ExternalLogRecord(logid=logid, parentlogid=parentlogid, loglevel=loglevel, logstatus=logstatus, sourcerecordtype=sourcerecordtype, sourceprimaryidtype=sourceprimaryidtype, sourceprimaryidvalue=sourceprimaryidvalue, targetrecordtype=targetrecordtype, targetrecordaction=targetrecordaction, targetprimaryidtype=targetprimaryidtype, targetprimaryidvalue=targetprimaryidvalue, message=message, messagetype=messagetype, timestamp=timestamp)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

