# finbourne_horizon.LogsApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_integration_log_results**](LogsApi.md#get_integration_log_results) | **GET** /api/logs | [EXPERIMENTAL] GetIntegrationLogResults: Get integration log results


# **get_integration_log_results**
> IIntegrationLogResponse get_integration_log_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)

[EXPERIMENTAL] GetIntegrationLogResults: Get integration log results

Get integration log results

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    LogsApi
)

async def main():

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

    # Use the finbourne_horizon ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(LogsApi)
        filter = 'filter_example' # str | Expression to filter the result set. (optional)
        sort_by = ['sort_by_example'] # List[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
        limit = 100 # int | When paginating, limit the results to this number. (optional) (default to 100)
        page_token = '' # str | The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915. (optional) (default to '')

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_integration_log_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token, opts=opts)

            # [EXPERIMENTAL] GetIntegrationLogResults: Get integration log results
            api_response = await api_instance.get_integration_log_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling LogsApi->get_integration_log_results: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. | [optional] 
 **sort_by** | [**List[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] [default to 100]
 **page_token** | **str**| The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the &lt;i&gt;sortBy&lt;/i&gt; and &lt;i&gt;filter&lt;/i&gt; fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915. | [optional] [default to &#39;&#39;]

### Return type

[**IIntegrationLogResponse**](IIntegrationLogResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

