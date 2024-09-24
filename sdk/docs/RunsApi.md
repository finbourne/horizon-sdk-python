# finbourne_horizon.RunsApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_run_results**](RunsApi.md#get_run_results) | **GET** /api/runs | [EXPERIMENTAL] GetRunResults: 


# **get_run_results**
> IntegrationRunResponse get_run_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)

[EXPERIMENTAL] GetRunResults: 

Get run results

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    RunsApi
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
        api_instance = api_client_factory.build(RunsApi)
        filter = 'filter_example' # str |  (optional)
        sort_by = ['sort_by_example'] # List[str] |  (optional)
        limit = 10 # int |  (optional) (default to 10)
        page_token = '' # str |  (optional) (default to '')

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_run_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token, opts=opts)

            # [EXPERIMENTAL] GetRunResults: 
            api_response = await api_instance.get_run_results(filter=filter, sort_by=sort_by, limit=limit, page_token=page_token)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RunsApi->get_run_results: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | [optional] 
 **sort_by** | [**List[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **page_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**IntegrationRunResponse**](IntegrationRunResponse.md)

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

