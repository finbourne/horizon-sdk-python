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

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ProcessHistoryApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "horizonUrl":"https://<your-domain>.lusid.com/horizon",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_horizon SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ProcessHistoryApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # audit_complete_request = AuditCompleteRequest.from_json("")
    # audit_complete_request = AuditCompleteRequest.from_dict({})
    audit_complete_request = AuditCompleteRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_complete_event(audit_complete_request, opts=opts)

        # [EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard
        api_response = api_instance.create_complete_event(audit_complete_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessHistoryApi->create_complete_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_complete_request** | [**AuditCompleteRequest**](AuditCompleteRequest.md)|  | 

### Return type

[**AuditCompleteResponse**](AuditCompleteResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_update_event**
> AuditUpdateResponse create_update_event(audit_update_request)

[EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ProcessHistoryApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "horizonUrl":"https://<your-domain>.lusid.com/horizon",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_horizon SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ProcessHistoryApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # audit_update_request = AuditUpdateRequest.from_json("")
    # audit_update_request = AuditUpdateRequest.from_dict({})
    audit_update_request = AuditUpdateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_update_event(audit_update_request, opts=opts)

        # [EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard
        api_response = api_instance.create_update_event(audit_update_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessHistoryApi->create_update_event: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_update_request** | [**AuditUpdateRequest**](AuditUpdateRequest.md)|  | 

### Return type

[**AuditUpdateResponse**](AuditUpdateResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_latest_runs**
> List[ProcessInformation] get_latest_runs()

[EARLY ACCESS] GetLatestRuns: Get latest run for each process

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ProcessHistoryApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "horizonUrl":"https://<your-domain>.lusid.com/horizon",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_horizon SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ProcessHistoryApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_latest_runs(opts=opts)

        # [EARLY ACCESS] GetLatestRuns: Get latest run for each process
        api_response = api_instance.get_latest_runs()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessHistoryApi->get_latest_runs: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ProcessInformation]**](ProcessInformation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **process_entry_updates**
> PagedResourceListOfProcessUpdateResult process_entry_updates(run_id, query_request)

[EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ProcessHistoryApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "horizonUrl":"https://<your-domain>.lusid.com/horizon",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_horizon SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ProcessHistoryApi)
    run_id = 'run_id_example' # str | 

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_request = QueryRequest.from_json("")
    # query_request = QueryRequest.from_dict({})
    query_request = QueryRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.process_entry_updates(run_id, query_request, opts=opts)

        # [EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query
        api_response = api_instance.process_entry_updates(run_id, query_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessHistoryApi->process_entry_updates: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**PagedResourceListOfProcessUpdateResult**](PagedResourceListOfProcessUpdateResult.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **process_history_entries**
> PagedResourceListOfProcessInformation process_history_entries(query_request, process_name=process_name)

[EARLY ACCESS] ProcessHistoryEntries: Get process history entries

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ProcessHistoryApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "horizonUrl":"https://<your-domain>.lusid.com/horizon",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_horizon SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ProcessHistoryApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # query_request = QueryRequest.from_json("")
    # query_request = QueryRequest.from_dict({})
    query_request = QueryRequest()
    process_name = 'process_name_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.process_history_entries(query_request, process_name=process_name, opts=opts)

        # [EARLY ACCESS] ProcessHistoryEntries: Get process history entries
        api_response = api_instance.process_history_entries(query_request, process_name=process_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ProcessHistoryApi->process_history_entries: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 
 **process_name** | **str**|  | [optional] 

### Return type

[**PagedResourceListOfProcessInformation**](PagedResourceListOfProcessInformation.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

