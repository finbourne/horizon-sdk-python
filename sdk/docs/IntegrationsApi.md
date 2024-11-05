# finbourne_horizon.IntegrationsApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance**](IntegrationsApi.md#create_instance) | **POST** /api/integrations/instances | [EXPERIMENTAL] CreateInstance: Create a single integration instance.
[**delete_instance**](IntegrationsApi.md#delete_instance) | **DELETE** /api/integrations/instances/{instanceId} | [EXPERIMENTAL] DeleteInstance: Delete a single integration instance.
[**execute_instance**](IntegrationsApi.md#execute_instance) | **POST** /api/integrations/instances/{instanceId}/execute | [EXPERIMENTAL] ExecuteInstance: Execute an integration instance.
[**get_execution_ids_for_instance**](IntegrationsApi.md#get_execution_ids_for_instance) | **GET** /api/integrations/instances/{instanceId}/executions | [EXPERIMENTAL] GetExecutionIdsForInstance: Get integration instance execution ids.
[**get_instance_optional_property_mapping**](IntegrationsApi.md#get_instance_optional_property_mapping) | **GET** /api/integrations/instances/configuration/{integration}/{instanceId} | [EXPERIMENTAL] GetInstanceOptionalPropertyMapping: Get the Optional Property Mapping for an Integration Instance
[**get_integration_configuration**](IntegrationsApi.md#get_integration_configuration) | **GET** /api/integrations/configuration/{integration} | [EXPERIMENTAL] GetIntegrationConfiguration: Get the Field and Property Mapping configuration for a given integration
[**get_schema**](IntegrationsApi.md#get_schema) | **GET** /api/integrations/schema/{integration} | [EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.
[**list_instances**](IntegrationsApi.md#list_instances) | **GET** /api/integrations/instances | [EXPERIMENTAL] ListInstances: List instances across all integrations.
[**list_integrations**](IntegrationsApi.md#list_integrations) | **GET** /api/integrations | [EXPERIMENTAL] ListIntegrations: List available integrations.
[**set_instance_optional_property_mapping**](IntegrationsApi.md#set_instance_optional_property_mapping) | **PUT** /api/integrations/instances/configuration/{integration}/{instanceId} | [EXPERIMENTAL] SetInstanceOptionalPropertyMapping: Set the Optional Property Mapping for an Integration Instance
[**update_instance**](IntegrationsApi.md#update_instance) | **PUT** /api/integrations/instances/{instanceId} | [EXPERIMENTAL] UpdateInstance: Update a single integration instance.


# **create_instance**
> InstanceIdentifier create_instance(create_instance_request=create_instance_request)

[EXPERIMENTAL] CreateInstance: Create a single integration instance.

<br>Creates a new instance of an integration, returning its identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_instance_request = CreateInstanceRequest.from_json("")
        # create_instance_request = CreateInstanceRequest.from_dict({})
        create_instance_request = CreateInstanceRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_instance(create_instance_request=create_instance_request, opts=opts)

            # [EXPERIMENTAL] CreateInstance: Create a single integration instance.
            api_response = await api_instance.create_instance(create_instance_request=create_instance_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->create_instance: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_instance_request** | [**CreateInstanceRequest**](CreateInstanceRequest.md)| The new integration instance. | [optional] 

### Return type

[**InstanceIdentifier**](InstanceIdentifier.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identifier of the created instance. |  -  |
**404** | The integration type does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_instance**
> delete_instance(instance_id)

[EXPERIMENTAL] DeleteInstance: Delete a single integration instance.

<br>Deletes an existing instance of an integration, returning its identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        instance_id = 'instance_id_example' # str | Instance identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.delete_instance(instance_id, opts=opts)

            # [EXPERIMENTAL] DeleteInstance: Delete a single integration instance.
            await api_instance.delete_instance(instance_id)        except ApiException as e:
            print("Exception when calling IntegrationsApi->delete_instance: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | The instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **execute_instance**
> ExecuteInstanceResponse execute_instance(instance_id)

[EXPERIMENTAL] ExecuteInstance: Execute an integration instance.

<br>Starts execution of an instance, returning its execution identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        instance_id = 'instance_id_example' # str | Instance identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.execute_instance(instance_id, opts=opts)

            # [EXPERIMENTAL] ExecuteInstance: Execute an integration instance.
            api_response = await api_instance.execute_instance(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->execute_instance: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 

### Return type

[**ExecuteInstanceResponse**](ExecuteInstanceResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution id |  -  |
**404** | The integration instance does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_execution_ids_for_instance**
> List[str] get_execution_ids_for_instance(instance_id, limit=limit)

[EXPERIMENTAL] GetExecutionIdsForInstance: Get integration instance execution ids.

<br>Get the most recent execution ids for an integration instance.  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        instance_id = 'instance_id_example' # str | Instance identifier e.g. \"30dc93c6-a127-46bf-aea8-e466d720b72d\".
        limit = 56 # int | Maximum number of returned execution ids (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_execution_ids_for_instance(instance_id, limit=limit, opts=opts)

            # [EXPERIMENTAL] GetExecutionIdsForInstance: Get integration instance execution ids.
            api_response = await api_instance.get_execution_ids_for_instance(instance_id, limit=limit)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->get_execution_ids_for_instance: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;30dc93c6-a127-46bf-aea8-e466d720b72d\&quot;. | 
 **limit** | **int**| Maximum number of returned execution ids | [optional] 

### Return type

**List[str]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution ids sorted by start date (descending) |  -  |
**404** | The integration instance does not exist |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_instance_optional_property_mapping**
> Dict[str, LusidPropertyDefinitionOverridesByType] get_instance_optional_property_mapping(integration, instance_id)

[EXPERIMENTAL] GetInstanceOptionalPropertyMapping: Get the Optional Property Mapping for an Integration Instance

Will return the full list of optional properties configured for this integration instance and any naming overrides

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        integration = 'integration_example' # str | The type of the integration e.g. \"copp-clark\".
        instance_id = 'instance_id_example' # str | Identifier of the instance

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_instance_optional_property_mapping(integration, instance_id, opts=opts)

            # [EXPERIMENTAL] GetInstanceOptionalPropertyMapping: Get the Optional Property Mapping for an Integration Instance
            api_response = await api_instance.get_instance_optional_property_mapping(integration, instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->get_instance_optional_property_mapping: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | 
 **instance_id** | **str**| Identifier of the instance | 

### Return type

[**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The requested instance(s) do not exist. |  -  |
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_integration_configuration**
> IntegrationPropertyConfiguration get_integration_configuration(integration)

[EXPERIMENTAL] GetIntegrationConfiguration: Get the Field and Property Mapping configuration for a given integration

<br>The user must be authenticated, entitled to call this method, but the user's domain does not need to be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        integration = 'integration_example' # str | 

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_integration_configuration(integration, opts=opts)

            # [EXPERIMENTAL] GetIntegrationConfiguration: Get the Field and Property Mapping configuration for a given integration
            api_response = await api_instance.get_integration_configuration(integration)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->get_integration_configuration: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**|  | 

### Return type

[**IntegrationPropertyConfiguration**](IntegrationPropertyConfiguration.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The requested integration does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_schema**
> JSchema get_schema(integration)

[EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.

<br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        integration = 'integration_example' # str | The type of the integration e.g. \"copp-clark\".

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_schema(integration, opts=opts)

            # [EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.
            api_response = await api_instance.get_schema(integration)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->get_schema: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | 

### Return type

[**JSchema**](JSchema.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The system defined JSON schema for the details of a specified integration. |  -  |
**404** | The integration type does not exist or is not enabled. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_instances**
> List[IntegrationInstance] list_instances()

[EXPERIMENTAL] ListInstances: List instances across all integrations.

<br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_instances(opts=opts)

            # [EXPERIMENTAL] ListInstances: List instances across all integrations.
            api_response = await api_instance.list_instances()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->list_instances: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[IntegrationInstance]**](IntegrationInstance.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The requested instance(s) do not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_integrations**
> List[IntegrationDescription] list_integrations()

[EXPERIMENTAL] ListIntegrations: List available integrations.

<br>List all available integrations.  <br />  <br>    ```\"licensed\"``` indicates your domain is licensed to use this integration. To request a licence              contact your [FINBOURNE sales representative](https://www.finbourne.com/contact/).  <br />  <br>Any authenticated user can call this method.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_integrations(opts=opts)

            # [EXPERIMENTAL] ListIntegrations: List available integrations.
            api_response = await api_instance.list_integrations()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->list_integrations: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[IntegrationDescription]**](IntegrationDescription.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_instance_optional_property_mapping**
> Dict[str, LusidPropertyDefinitionOverridesByType] set_instance_optional_property_mapping(instance_id, integration, request_body=request_body)

[EXPERIMENTAL] SetInstanceOptionalPropertyMapping: Set the Optional Property Mapping for an Integration Instance

The full list of properties must be supplied, the removal of a property from this list will remove it from the integration instance

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        instance_id = 'instance_id_example' # str | Identifier of the instance
        integration = 'integration_example' # str | The type of the integration e.g. \"copp-clark\".
        request_body = {"Instrument/TestVendor/CreditRating":{"displayNameOverride":"Vendor Credit Rating","entityType":"Instrument","entitySubType":["Equity"],"vendorPackage":["Transaction"]}} # Dict[str, LusidPropertyDefinitionOverridesByType] | Properties to be included and any overrides (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.set_instance_optional_property_mapping(instance_id, integration, request_body=request_body, opts=opts)

            # [EXPERIMENTAL] SetInstanceOptionalPropertyMapping: Set the Optional Property Mapping for an Integration Instance
            api_response = await api_instance.set_instance_optional_property_mapping(instance_id, integration, request_body=request_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IntegrationsApi->set_instance_optional_property_mapping: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Identifier of the instance | 
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | 
 **request_body** | [**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md)| Properties to be included and any overrides | [optional] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverridesByType]**](LusidPropertyDefinitionOverridesByType.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | The requested instance(s) do not exist. |  -  |
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_instance**
> update_instance(instance_id, update_instance_request=update_instance_request)

[EXPERIMENTAL] UpdateInstance: Update a single integration instance.

<br>Updates an existing instance of an integration, returning its identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi
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
        api_instance = api_client_factory.build(IntegrationsApi)
        instance_id = 'instance_id_example' # str | Instance identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_instance_request = UpdateInstanceRequest.from_json("")
        # update_instance_request = UpdateInstanceRequest.from_dict({})
        update_instance_request = UpdateInstanceRequest()

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.update_instance(instance_id, update_instance_request=update_instance_request, opts=opts)

            # [EXPERIMENTAL] UpdateInstance: Update a single integration instance.
            await api_instance.update_instance(instance_id, update_instance_request=update_instance_request)        except ApiException as e:
            print("Exception when calling IntegrationsApi->update_instance: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 
 **update_instance_request** | [**UpdateInstanceRequest**](UpdateInstanceRequest.md)| The new integration instance. | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | The instance does not exist. |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

