# AlertRule

An alert rule on an integration instance. Finbourne.Horizon.Integrations.Web.Dto.AlertRule.Type selects the rule and decides which of the optional fields apply. A field that does not belong to the selected type is rejected.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The rule type (Allowed: MustStartBy, MaxDuration, FailedAfterRetries) | 
**severity** | **str** | The severity alerts from this rule are raised at (Allowed: Critical, High, Medium, Low, Informational). Critical pages on-call for a client-facing outage. High needs action today. Medium is a missed or late run. Low is an overrun or record-count check. Informational never pages. Defaults per type when omitted: MustStartBy and FailedAfterRetries Medium, MaxDuration Low. | [optional] 
**time_of_day** | **str** | MustStartBy only. The local time of day, as HH:mm, by which a run must have started. | [optional] 
**time_zone** | **str** | MustStartBy only. The IANA or Windows time zone id that TimeOfDay is expressed in. | [optional] 
**days_of_week** | **List[str]** | MustStartBy only. The days the rule applies on, by name (e.g. Monday). Every day when omitted. | [optional] 
**grace_minutes** | **int** | MustStartBy only. Minutes after TimeOfDay before a missing run counts as a breach. 0 when omitted. | [optional] 
**max_minutes** | **int** | MaxDuration only. Alert once a run has been running for longer than this many minutes. Minimum 10. | [optional] 
**include_paused** | **bool** | MaxDuration only. Also measure paused runs. False when omitted. | [optional] 
**alert_on_first_failure** | **bool** | FailedAfterRetries only. Also alert on the first failure of a retry chain, not only when the retries are exhausted. False when omitted. | [optional] 
## Example

```python
from finbourne_horizon.models.alert_rule import AlertRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
severity: Optional[StrictStr] = "example_severity"
time_of_day: Optional[StrictStr] = "example_time_of_day"
time_zone: Optional[StrictStr] = "example_time_zone"
days_of_week: Optional[List[StrictStr]] = # Replace with your value
grace_minutes: Optional[StrictInt] = # Replace with your value
grace_minutes: Optional[StrictInt] = None
max_minutes: Optional[StrictInt] = # Replace with your value
max_minutes: Optional[StrictInt] = None
include_paused: Optional[StrictBool] = # Replace with your value
include_paused:Optional[StrictBool] = None
alert_on_first_failure: Optional[StrictBool] = # Replace with your value
alert_on_first_failure:Optional[StrictBool] = None
alert_rule_instance = AlertRule(type=type, severity=severity, time_of_day=time_of_day, time_zone=time_zone, days_of_week=days_of_week, grace_minutes=grace_minutes, max_minutes=max_minutes, include_paused=include_paused, alert_on_first_failure=alert_on_first_failure)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

