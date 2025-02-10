# finbourne_horizon.RunsApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_instance**](RunsApi.md#cancel_instance) | **PUT** /api/runs/{runId}/cancel | [EXPERIMENTAL] CancelInstance: Cancels a single instance execution.
[**get_run_results**](RunsApi.md#get_run_results) | **GET** /api/runs | [EXPERIMENTAL] GetRunResults: Get run results
[**rerun_instance**](RunsApi.md#rerun_instance) | **PUT** /api/runs/{runId}/rerun | [EXPERIMENTAL] RerunInstance: Reruns a single instance execution.


# **cancel_instance**
> object cancel_instance(run_id)

[EXPERIMENTAL] CancelInstance: Cancels a single instance execution.

Cancels an execution instance of an integration.  The execution instance must be queued, the user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    RunsApi
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
    api_instance = api_client_factory.build(RunsApi)
    run_id = 'run_id_example' # str | Run identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.cancel_instance(run_id, opts=opts)

        # [EXPERIMENTAL] CancelInstance: Cancels a single instance execution.
        api_response = api_instance.cancel_instance(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RunsApi->cancel_instance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 

### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instance was cancelled. |  -  |
**400** | The details of the input related failure |  -  |
**404** | The execution does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_run_results**
> PagedResourceListOfIntegrationRunResponse get_run_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)

[EXPERIMENTAL] GetRunResults: Get run results

Get run results

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    RunsApi
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
    api_instance = api_client_factory.build(RunsApi)
    filter = 'filter_example' # str | Expression to filter the result set. (optional)
    sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
    limit = 100 # int | When paginating, limit the results to this number. (optional) (default to 100)
    page_token = '' # str | The pagination token to use to continue listing integration runs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request. (optional) (default to '')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_run_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token, opts=opts)

        # [EXPERIMENTAL] GetRunResults: Get run results
        api_response = api_instance.get_run_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RunsApi->get_run_results: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] [default to 100]
 **page_token** | **str**| The pagination token to use to continue listing integration runs; this value is returned from              the previous call. If a pagination token is provided, the &lt;i&gt;sortBy&lt;/i&gt; and &lt;i&gt;filter&lt;/i&gt; fields must not have changed since the original request. | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfIntegrationRunResponse**](PagedResourceListOfIntegrationRunResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | Not Found |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **rerun_instance**
> IntegrationRerunResponse rerun_instance(run_id)

[EXPERIMENTAL] RerunInstance: Reruns a single instance execution.

Reruns an execution instance of an integration.  The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    RunsApi
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
    api_instance = api_client_factory.build(RunsApi)
    run_id = 'run_id_example' # str | Run identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.rerun_instance(run_id, opts=opts)

        # [EXPERIMENTAL] RerunInstance: Reruns a single instance execution.
        api_response = api_instance.rerun_instance(run_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RunsApi->rerun_instance: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 

### Return type

[**IntegrationRerunResponse**](IntegrationRerunResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The instance was rerun. |  -  |
**400** | The details of the input related failure |  -  |
**404** | The execution does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

