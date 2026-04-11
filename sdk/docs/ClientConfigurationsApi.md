# finbourne_horizon.ClientConfigurationsApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client_configuration_draft**](ClientConfigurationsApi.md#create_client_configuration_draft) | **POST** /api/clientconfiguration/{configType}/{name}/draft | [EXPERIMENTAL] CreateClientConfigurationDraft: Create a draft client configuration.
[**get_client_configuration**](ClientConfigurationsApi.md#get_client_configuration) | **GET** /api/clientconfiguration/{configType}/{name} | [EXPERIMENTAL] GetClientConfiguration: Get a client configuration.
[**list_client_configurations**](ClientConfigurationsApi.md#list_client_configurations) | **GET** /api/clientconfiguration/{configType} | [EXPERIMENTAL] ListClientConfigurations: List client configurations.
[**lock_client_configuration_version**](ClientConfigurationsApi.md#lock_client_configuration_version) | **POST** /api/clientconfiguration/{configType}/{name}/{majorVersion}/{minorVersion}/lock | [EXPERIMENTAL] LockClientConfigurationVersion: Lock a client configuration version.
[**update_client_configuration_draft**](ClientConfigurationsApi.md#update_client_configuration_draft) | **PUT** /api/clientconfiguration/{configType}/{name}/{majorVersion}/{minorVersion}/draft | [EXPERIMENTAL] UpdateClientConfigurationDraft: Update a draft client configuration.


# **create_client_configuration_draft**
> ClientConfigurationResponse create_client_configuration_draft(config_type, name, create_client_configuration_draft_request=create_client_configuration_draft_request)

[EXPERIMENTAL] CreateClientConfigurationDraft: Create a draft client configuration.

Creates a new draft configuration record. Configurations follow a draft/locked lifecycle: create a draft here, refine it with the update endpoint, then commit it with the lock endpoint. If both majorVersion and minorVersion are omitted in the request body, the next version is assigned automatically by incrementing the minor version of the current highest version (starting at 1.0 if none exists). The user must be authenticated and entitled to call this method.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ClientConfigurationsApi
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
    api_instance = api_client_factory.build(ClientConfigurationsApi)
    config_type = 'config_type_example' # str | The category of configuration.
    name = 'name_example' # str | The logical name of the configuration.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_client_configuration_draft_request = CreateClientConfigurationDraftRequest.from_json("")
    # create_client_configuration_draft_request = CreateClientConfigurationDraftRequest.from_dict({})
    create_client_configuration_draft_request = CreateClientConfigurationDraftRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_client_configuration_draft(config_type, name, create_client_configuration_draft_request=create_client_configuration_draft_request, opts=opts)

        # [EXPERIMENTAL] CreateClientConfigurationDraft: Create a draft client configuration.
        api_response = api_instance.create_client_configuration_draft(config_type, name, create_client_configuration_draft_request=create_client_configuration_draft_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ClientConfigurationsApi->create_client_configuration_draft: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | 
 **name** | **str**| The logical name of the configuration. | 
 **create_client_configuration_draft_request** | [**CreateClientConfigurationDraftRequest**](CreateClientConfigurationDraftRequest.md)| Options for the new draft, including optional explicit version and source version. | [optional] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client does not exist. |  -  |
**409** | A configuration with the specified version already exists. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_client_configuration**
> ClientConfigurationResponse get_client_configuration(config_type, name, major_version=major_version, minor_version=minor_version)

[EXPERIMENTAL] GetClientConfiguration: Get a client configuration.

Returns a specific configuration record. When both majorVersion and minorVersion are omitted, the highest available version is returned. Both must be supplied together or both omitted. The user must be authenticated and entitled to call this method.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ClientConfigurationsApi
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
    api_instance = api_client_factory.build(ClientConfigurationsApi)
    config_type = 'config_type_example' # str | The category of configuration.
    name = 'name_example' # str | The logical name of the configuration.
    major_version = 56 # int | The major version to retrieve. Must be supplied together with minorVersion, or both omitted. (optional)
    minor_version = 56 # int | The minor version to retrieve. Must be supplied together with majorVersion, or both omitted. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_client_configuration(config_type, name, major_version=major_version, minor_version=minor_version, opts=opts)

        # [EXPERIMENTAL] GetClientConfiguration: Get a client configuration.
        api_response = api_instance.get_client_configuration(config_type, name, major_version=major_version, minor_version=minor_version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ClientConfigurationsApi->get_client_configuration: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | 
 **name** | **str**| The logical name of the configuration. | 
 **major_version** | **int**| The major version to retrieve. Must be supplied together with minorVersion, or both omitted. | [optional] 
 **minor_version** | **int**| The minor version to retrieve. Must be supplied together with majorVersion, or both omitted. | [optional] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client or configuration does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_client_configurations**
> List[ClientConfigurationResponse] list_client_configurations(config_type)

[EXPERIMENTAL] ListClientConfigurations: List client configurations.

Returns all configuration records for the given config type, across all versions and states (both draft and locked), ordered by version descending. The user must be authenticated and entitled to call this method.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ClientConfigurationsApi
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
    api_instance = api_client_factory.build(ClientConfigurationsApi)
    config_type = 'config_type_example' # str | The category of configuration to list.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_client_configurations(config_type, opts=opts)

        # [EXPERIMENTAL] ListClientConfigurations: List client configurations.
        api_response = api_instance.list_client_configurations(config_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ClientConfigurationsApi->list_client_configurations: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration to list. | 

### Return type

[**List[ClientConfigurationResponse]**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **lock_client_configuration_version**
> ClientConfigurationResponse lock_client_configuration_version(config_type, name, major_version, minor_version)

[EXPERIMENTAL] LockClientConfigurationVersion: Lock a client configuration version.

Locks a draft configuration version, making it immutable and ready for use. Once locked, a version cannot be edited or unlocked. All versions are retained permanently. The user must be authenticated and entitled to call this method.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ClientConfigurationsApi
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
    api_instance = api_client_factory.build(ClientConfigurationsApi)
    config_type = 'config_type_example' # str | The category of configuration.
    name = 'name_example' # str | The logical name of the configuration.
    major_version = 56 # int | The major version to lock.
    minor_version = 56 # int | The minor version to lock.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.lock_client_configuration_version(config_type, name, major_version, minor_version, opts=opts)

        # [EXPERIMENTAL] LockClientConfigurationVersion: Lock a client configuration version.
        api_response = api_instance.lock_client_configuration_version(config_type, name, major_version, minor_version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ClientConfigurationsApi->lock_client_configuration_version: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | 
 **name** | **str**| The logical name of the configuration. | 
 **major_version** | **int**| The major version to lock. | 
 **minor_version** | **int**| The minor version to lock. | 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client or configuration version does not exist, or the version is already locked. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_client_configuration_draft**
> ClientConfigurationResponse update_client_configuration_draft(config_type, name, major_version, minor_version, update_client_configuration_draft_request=update_client_configuration_draft_request)

[EXPERIMENTAL] UpdateClientConfigurationDraft: Update a draft client configuration.

Updates the value of an existing draft configuration. Only draft versions can be updated; locked versions are immutable. This endpoint can be called multiple times before locking. The user must be authenticated and entitled to call this method.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    ClientConfigurationsApi
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
    api_instance = api_client_factory.build(ClientConfigurationsApi)
    config_type = 'config_type_example' # str | The category of configuration.
    name = 'name_example' # str | The logical name of the configuration.
    major_version = 56 # int | The major version of the draft to update.
    minor_version = 56 # int | The minor version of the draft to update.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_client_configuration_draft_request = UpdateClientConfigurationDraftRequest.from_json("")
    # update_client_configuration_draft_request = UpdateClientConfigurationDraftRequest.from_dict({})
    update_client_configuration_draft_request = UpdateClientConfigurationDraftRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_client_configuration_draft(config_type, name, major_version, minor_version, update_client_configuration_draft_request=update_client_configuration_draft_request, opts=opts)

        # [EXPERIMENTAL] UpdateClientConfigurationDraft: Update a draft client configuration.
        api_response = api_instance.update_client_configuration_draft(config_type, name, major_version, minor_version, update_client_configuration_draft_request=update_client_configuration_draft_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ClientConfigurationsApi->update_client_configuration_draft: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**| The category of configuration. | 
 **name** | **str**| The logical name of the configuration. | 
 **major_version** | **int**| The major version of the draft to update. | 
 **minor_version** | **int**| The minor version of the draft to update. | 
 **update_client_configuration_draft_request** | [**UpdateClientConfigurationDraftRequest**](UpdateClientConfigurationDraftRequest.md)| The updated value. | [optional] 

### Return type

[**ClientConfigurationResponse**](ClientConfigurationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**404** | The client or configuration version does not exist, or the version is already locked. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

