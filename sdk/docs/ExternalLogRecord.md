# ExternalLogRecord

Represents an external log record.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logid** | **int** | The unique log identifier. | 
**parentlogid** | **int** | The parent log identifier (null is allowed). | [optional] 
**loglevel** | **str** | The log level. | 
**logstatus** | **str** | The log status. | 
**sourcerecordtype** | **str** | The source record type. | [optional] 
**sourceprimaryidtype** | **str** | The source primary ID type. | [optional] 
**sourceprimaryidvalue** | **str** | The source primary ID value. | [optional] 
**targetrecordtype** | **str** | The target record type. | [optional] 
**targetrecordaction** | **str** | The target record action. | [optional] 
**targetprimaryidtype** | **str** | The target primary ID type. | [optional] 
**targetprimaryidvalue** | **str** | The target primary ID value. | [optional] 
**message** | **str** | The log message. | [optional] 
**messagetype** | **str** | The message type. | [optional] 
**timestamp** | **str** | The timestamp of the log record. | 
## Example

```python
from finbourne_horizon.models.external_log_record import ExternalLogRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

logid: StrictInt = # Replace with your value
parentlogid: Optional[StrictInt] = # Replace with your value
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

