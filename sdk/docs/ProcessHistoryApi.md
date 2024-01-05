# finbourne_horizon.ProcessHistoryApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_complete_event**](ProcessHistoryApi.md#create_complete_event) | **POST** /api/process-history/event/complete | [EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard
[**create_update_event**](ProcessHistoryApi.md#create_update_event) | **POST** /api/process-history/event/update | [EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard
[**get_latest_runs**](ProcessHistoryApi.md#get_latest_runs) | **GET** /api/process-history/$latestRuns | [EARLY ACCESS] GetLatestRuns: Get latest run for each process
[**process_entry_updates**](ProcessHistoryApi.md#process_entry_updates) | **POST** /api/process-history/entries/$query | [EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query
[**process_history_entries**](ProcessHistoryApi.md#process_history_entries) | **POST** /api/process-history/$query | [EARLY ACCESS] ProcessHistoryEntries: Get process history entries


# **create_complete_event**
> AuditCompleteResponse create_complete_event(audit_complete_request)

[EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.audit_complete_request import AuditCompleteRequest
from finbourne_horizon.models.audit_complete_response import AuditCompleteResponse
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_horizon ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/horizon"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_horizon.ProcessHistoryApi)
    audit_complete_request = finbourne_horizon.AuditCompleteRequest() # AuditCompleteRequest | 

    try:
        # [EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard
        api_response = await api_instance.create_complete_event(audit_complete_request)
        print("The response of ProcessHistoryApi->create_complete_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessHistoryApi->create_complete_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_complete_request** | [**AuditCompleteRequest**](AuditCompleteRequest.md)|  | 

### Return type

[**AuditCompleteResponse**](AuditCompleteResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_event**
> AuditUpdateResponse create_update_event(audit_update_request)

[EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.audit_update_request import AuditUpdateRequest
from finbourne_horizon.models.audit_update_response import AuditUpdateResponse
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_horizon ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/horizon"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_horizon.ProcessHistoryApi)
    audit_update_request = finbourne_horizon.AuditUpdateRequest() # AuditUpdateRequest | 

    try:
        # [EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard
        api_response = await api_instance.create_update_event(audit_update_request)
        print("The response of ProcessHistoryApi->create_update_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessHistoryApi->create_update_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_update_request** | [**AuditUpdateRequest**](AuditUpdateRequest.md)|  | 

### Return type

[**AuditUpdateResponse**](AuditUpdateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_runs**
> List[ProcessInformation] get_latest_runs()

[EARLY ACCESS] GetLatestRuns: Get latest run for each process

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.process_information import ProcessInformation
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_horizon ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/horizon"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_horizon.ProcessHistoryApi)

    try:
        # [EARLY ACCESS] GetLatestRuns: Get latest run for each process
        api_response = await api_instance.get_latest_runs()
        print("The response of ProcessHistoryApi->get_latest_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessHistoryApi->get_latest_runs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ProcessInformation]**](ProcessInformation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_entry_updates**
> PagedResourceListOfProcessUpdateResult process_entry_updates(query_request, run_id=run_id)

[EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.paged_resource_list_of_process_update_result import PagedResourceListOfProcessUpdateResult
from finbourne_horizon.models.query_request import QueryRequest
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_horizon ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/horizon"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_horizon.ProcessHistoryApi)
    query_request = finbourne_horizon.QueryRequest() # QueryRequest | 
    run_id = 'run_id_example' # str |  (optional)

    try:
        # [EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query
        api_response = await api_instance.process_entry_updates(query_request, run_id=run_id)
        print("The response of ProcessHistoryApi->process_entry_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessHistoryApi->process_entry_updates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 
 **run_id** | **str**|  | [optional] 

### Return type

[**PagedResourceListOfProcessUpdateResult**](PagedResourceListOfProcessUpdateResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_history_entries**
> PagedResourceListOfProcessInformation process_history_entries(query_request)

[EARLY ACCESS] ProcessHistoryEntries: Get process history entries

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.paged_resource_list_of_process_information import PagedResourceListOfProcessInformation
from finbourne_horizon.models.query_request import QueryRequest
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_horizon ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/horizon"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_horizon.ProcessHistoryApi)
    query_request = finbourne_horizon.QueryRequest() # QueryRequest | 

    try:
        # [EARLY ACCESS] ProcessHistoryEntries: Get process history entries
        api_response = await api_instance.process_history_entries(query_request)
        print("The response of ProcessHistoryApi->process_history_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessHistoryApi->process_history_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**PagedResourceListOfProcessInformation**](PagedResourceListOfProcessInformation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

