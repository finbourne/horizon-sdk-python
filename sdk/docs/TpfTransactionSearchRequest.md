# TpfTransactionSearchRequest

Request body for the POST transaction-search endpoint. Multiple values in TransactionIds and InstrumentIdentifiers are OR'd within each filter; both filters together are AND'd.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** | One or more LUSID transaction IDs to search for (max 50). Values are OR&#39;d. | [optional] 
**instrument_identifiers** | **List[str]** | One or more instrument identifiers to search for (max 50). Values are OR&#39;d. Accepts LusidInstrumentId, Isin, Figi, Ticker, Cusip, Sedol or ClientInternal values. Every value is matched exactly against the stored instrument id; non-LUID values are also resolved against LUSID instruments in the default scope, whose own matching rules (including case) apply. | [optional] 
**instance_id** | **str** | Instance ID to filter by. Omit or leave null to search all instances the caller has access to. | [optional] 
**var_from** | **datetime** | Start of the date range (inclusive). Defaults to 30 days ago if neither From nor To is provided. | [optional] 
**to** | **datetime** | End of the date range (inclusive). Defaults to now if not provided. | [optional] 
**limit** | **int** | Maximum number of results to return per page. | [optional] 
**page** | **str** | Pagination token from a previous response NextPage or PreviousPage. Omit for the first page. | [optional] 
**status** | **str** | Publication status to filter by. Valid values: Sent, Skipped, Failed. Optional. | [optional] 
**filter** | **str** | Filter expression to apply to the results, in the format \&quot;property operator value\&quot; (e.g., eq, ne, gt, lt), combined with \&quot;and\&quot;/\&quot;or\&quot; as needed. Filterable properties are transactionId, instanceName, runStartTime, instrumentName, instrumentType, instrumentId, tradeDate, settlementDate, skipReason, failureReason, fileName, portfolioScope, portfolioCode, and runId. PublicationStatus is not filterable here — use the Status body parameter instead. Dates are quoted ISO-8601. Destinations is not filterable. Must remain the same across pages — the page token includes a hash of both filter and sortBy. | [optional] 
**sort_by** | **List[str]** | Up to two sortable fields, each optionally suffixed \&quot; ASC\&quot; or \&quot; DESC\&quot;. Deterministic tiebreakers are appended automatically: RunStartTime DESC, TransactionId ASC, BatchUuid ASC, FileName ASC. Must remain the same across pages — the page token includes a hash of both filter and sortBy. | [optional] 
## Example

```python
from finbourne_horizon.models.tpf_transaction_search_request import TpfTransactionSearchRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_ids: Optional[List[StrictStr]] = # Replace with your value
instrument_identifiers: Optional[List[StrictStr]] = # Replace with your value
instance_id: Optional[StrictStr] = "example_instance_id"
var_from: Optional[datetime] = # Replace with your value
to: Optional[datetime] = # Replace with your value
limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
page: Optional[StrictStr] = "example_page"
status: Optional[StrictStr] = "example_status"
filter: Optional[StrictStr] = "example_filter"
sort_by: Optional[List[StrictStr]] = # Replace with your value
tpf_transaction_search_request_instance = TpfTransactionSearchRequest(transaction_ids=transaction_ids, instrument_identifiers=instrument_identifiers, instance_id=instance_id, var_from=var_from, to=to, limit=limit, page=page, status=status, filter=filter, sort_by=sort_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

