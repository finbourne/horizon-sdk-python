# finbourne_horizon.TradePublicationFrameworkApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tpf_transaction_history_search**](TradePublicationFrameworkApi.md#get_tpf_transaction_history_search) | **GET** /api/trade-publication-framework/transactions/search | [EXPERIMENTAL] GetTpfTransactionHistorySearch: Endpoint to search TPF transaction by transaction ID and/or instrument identifier, with filtering by instance and date range
[**get_transaction_payload**](TradePublicationFrameworkApi.md#get_transaction_payload) | **GET** /api/trade-publication-framework/instances/{instanceId}/runs/{runId}/transactions/{transactionId}/payload | [EXPERIMENTAL] GetTransactionPayload: Transaction payload detail
[**list_instance_run_history**](TradePublicationFrameworkApi.md#list_instance_run_history) | **GET** /api/trade-publication-framework/instances/{instanceId}/runs | [EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.
[**list_instances_with_status**](TradePublicationFrameworkApi.md#list_instances_with_status) | **GET** /api/trade-publication-framework/instances | [EXPERIMENTAL] ListInstancesWithStatus: Lists all instances of the Trade Publication Framework (TPF).
[**list_run_files**](TradePublicationFrameworkApi.md#list_run_files) | **GET** /api/trade-publication-framework/instances/{instanceId}/runs/{runId}/files | [EXPERIMENTAL] ListRunFiles: List Files in a run
[**list_run_transactions**](TradePublicationFrameworkApi.md#list_run_transactions) | **GET** /api/trade-publication-framework/instances/{instanceId}/runs/{runId}/transactions | [EXPERIMENTAL] ListRunTransactions: List Transactions in a run.
[**replay_transactions**](TradePublicationFrameworkApi.md#replay_transactions) | **POST** /api/trade-publication-framework/instances/{instanceId}/replay | [EXPERIMENTAL] ReplayTransactions: Replay one or more transactions through a TPF instance
[**retry_tpf_sftp_delivery**](TradePublicationFrameworkApi.md#retry_tpf_sftp_delivery) | **POST** /api/trade-publication-framework/instances/{instanceId}/files/{fileId}/retry-sftp | [EXPERIMENTAL] RetryTpfSftpDelivery: Retry SFTP delivery for a previously sent TPF file


# **get_tpf_transaction_history_search**
> PagedResourceListOfTpfTransactionSearchResponse get_tpf_transaction_history_search(transaction_id=transaction_id, instrument_id=instrument_id, date_from=date_from, date_to=date_to, status=status, instance_id=instance_id, page_size=page_size, page_token=page_token)

[EXPERIMENTAL] GetTpfTransactionHistorySearch: Endpoint to search TPF transaction by transaction ID and/or instrument identifier, with filtering by instance and date range

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    transaction_id = 'transaction_id_example' # str |  (optional)
    instrument_id = 'instrument_id_example' # str |  (optional)
    date_from = 'date_from_example' # str |  (optional)
    date_to = 'date_to_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    instance_id = 'instance_id_example' # str |  (optional)
    page_size = 400 # int |  (optional) (default to 400)
    page_token = '' # str |  (optional) (default to '')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_tpf_transaction_history_search(transaction_id=transaction_id, instrument_id=instrument_id, date_from=date_from, date_to=date_to, status=status, instance_id=instance_id, page_size=page_size, page_token=page_token, opts=opts)

        # [EXPERIMENTAL] GetTpfTransactionHistorySearch: Endpoint to search TPF transaction by transaction ID and/or instrument identifier, with filtering by instance and date range
        api_response = api_instance.get_tpf_transaction_history_search(transaction_id=transaction_id, instrument_id=instrument_id, date_from=date_from, date_to=date_to, status=status, instance_id=instance_id, page_size=page_size, page_token=page_token)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->get_tpf_transaction_history_search: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**|  | [optional] 
 **instrument_id** | **str**|  | [optional] 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **instance_id** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 400]
 **page_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**PagedResourceListOfTpfTransactionSearchResponse**](PagedResourceListOfTpfTransactionSearchResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_transaction_payload**
> TransactionPayloadResponse get_transaction_payload(instance_id, run_id, transaction_id)

[EXPERIMENTAL] GetTransactionPayload: Transaction payload detail

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    instance_id = 'instance_id_example' # str | 
    run_id = 'run_id_example' # str | 
    transaction_id = 'transaction_id_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_transaction_payload(instance_id, run_id, transaction_id, opts=opts)

        # [EXPERIMENTAL] GetTransactionPayload: Transaction payload detail
        api_response = api_instance.get_transaction_payload(instance_id, run_id, transaction_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->get_transaction_payload: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **run_id** | **str**|  | 
 **transaction_id** | **str**|  | 

### Return type

[**TransactionPayloadResponse**](TransactionPayloadResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance, run, or transaction payload does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_instance_run_history**
> PagedResourceListOfInstanceRunResponse list_instance_run_history(instance_id, page=page, page_size=page_size)

[EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    instance_id = 'instance_id_example' # str | 
    page = '' # str |  (optional) (default to '')
    page_size = 100 # int |  (optional) (default to 100)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_instance_run_history(instance_id, page=page, page_size=page_size, opts=opts)

        # [EXPERIMENTAL] ListInstanceRunHistory: List run history for a given TPF instance, with pagination support.
        api_response = api_instance.list_instance_run_history(instance_id, page=page, page_size=page_size)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->list_instance_run_history: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfInstanceRunResponse**](PagedResourceListOfInstanceRunResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_instances_with_status**
> InstancesResponse list_instances_with_status()

[EXPERIMENTAL] ListInstancesWithStatus: Lists all instances of the Trade Publication Framework (TPF).

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_instances_with_status(opts=opts)

        # [EXPERIMENTAL] ListInstancesWithStatus: Lists all instances of the Trade Publication Framework (TPF).
        api_response = api_instance.list_instances_with_status()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->list_instances_with_status: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InstancesResponse**](InstancesResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_run_files**
> PagedResourceListOfRunFileResponse list_run_files(instance_id, run_id, page=page, page_size=page_size)

[EXPERIMENTAL] ListRunFiles: List Files in a run

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    instance_id = 'instance_id_example' # str | 
    run_id = 'run_id_example' # str | 
    page = '' # str |  (optional) (default to '')
    page_size = 100 # int |  (optional) (default to 100)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_run_files(instance_id, run_id, page=page, page_size=page_size, opts=opts)

        # [EXPERIMENTAL] ListRunFiles: List Files in a run
        api_response = api_instance.list_run_files(instance_id, run_id, page=page, page_size=page_size)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->list_run_files: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **run_id** | **str**|  | 
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfRunFileResponse**](PagedResourceListOfRunFileResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance or run does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_run_transactions**
> PagedResourceListOfTransactionResponse list_run_transactions(instance_id, run_id, status, page=page, page_size=page_size)

[EXPERIMENTAL] ListRunTransactions: List Transactions in a run.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    instance_id = 'instance_id_example' # str | 
    run_id = 'run_id_example' # str | 
    status = 'status_example' # str | 
    page = '' # str |  (optional) (default to '')
    page_size = 100 # int |  (optional) (default to 100)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_run_transactions(instance_id, run_id, status, page=page, page_size=page_size, opts=opts)

        # [EXPERIMENTAL] ListRunTransactions: List Transactions in a run.
        api_response = api_instance.list_run_transactions(instance_id, run_id, status, page=page, page_size=page_size)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->list_run_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **run_id** | **str**|  | 
 **status** | **str**|  | 
 **page** | **str**|  | [optional] [default to &#39;&#39;]
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PagedResourceListOfTransactionResponse**](PagedResourceListOfTransactionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance or run does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **replay_transactions**
> ReplayTransactionsResponse replay_transactions(instance_id, replay_transactions_request)

[EXPERIMENTAL] ReplayTransactions: Replay one or more transactions through a TPF instance

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    instance_id = 'instance_id_example' # str | 

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # replay_transactions_request = ReplayTransactionsRequest.from_json("")
    # replay_transactions_request = ReplayTransactionsRequest.from_dict({})
    replay_transactions_request = ReplayTransactionsRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.replay_transactions(instance_id, replay_transactions_request, opts=opts)

        # [EXPERIMENTAL] ReplayTransactions: Replay one or more transactions through a TPF instance
        api_response = api_instance.replay_transactions(instance_id, replay_transactions_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->replay_transactions: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **replay_transactions_request** | [**ReplayTransactionsRequest**](ReplayTransactionsRequest.md)|  | 

### Return type

[**ReplayTransactionsResponse**](ReplayTransactionsResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The requested TPF instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **retry_tpf_sftp_delivery**
> TpfRetrySftpResponse retry_tpf_sftp_delivery(instance_id, file_id)

[EXPERIMENTAL] RetryTpfSftpDelivery: Retry SFTP delivery for a previously sent TPF file

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    TradePublicationFrameworkApi
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
    api_instance = api_client_factory.build(TradePublicationFrameworkApi)
    instance_id = 'instance_id_example' # str | Integration instance ID
    file_id = 56 # int | File delivery ID to retry

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.retry_tpf_sftp_delivery(instance_id, file_id, opts=opts)

        # [EXPERIMENTAL] RetryTpfSftpDelivery: Retry SFTP delivery for a previously sent TPF file
        api_response = api_instance.retry_tpf_sftp_delivery(instance_id, file_id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling TradePublicationFrameworkApi->retry_tpf_sftp_delivery: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Integration instance ID | 
 **file_id** | **int**| File delivery ID to retry | 

### Return type

[**TpfRetrySftpResponse**](TpfRetrySftpResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retry succeeded - file re-sent to SFTP |  -  |
**400** | The details of the input related failure |  -  |
**404** | File delivery record not found |  -  |
**409** | Duplicate file detected - same hash already delivered to destination |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

