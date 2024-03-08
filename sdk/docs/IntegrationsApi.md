# finbourne_horizon.IntegrationsApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instance**](IntegrationsApi.md#create_instance) | **POST** /api/integrations/instances | [EXPERIMENTAL] CreateInstance: Create a single integration instance.
[**delete_instance**](IntegrationsApi.md#delete_instance) | **DELETE** /api/integrations/instances/{instanceId} | [EXPERIMENTAL] DeleteInstance: Delete a single integration instance.
[**execute_instance**](IntegrationsApi.md#execute_instance) | **POST** /api/integrations/instances/{instanceId}/execute | [EXPERIMENTAL] ExecuteInstance: Execute an integration instance.
[**get_schema**](IntegrationsApi.md#get_schema) | **GET** /api/integrations/schema/{integration} | [EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.
[**list_instances**](IntegrationsApi.md#list_instances) | **GET** /api/integrations/instances | [EXPERIMENTAL] ListInstances: List instances across all integrations.
[**list_integrations**](IntegrationsApi.md#list_integrations) | **GET** /api/integrations | [EXPERIMENTAL] ListIntegrations: List available integrations.
[**update_instance**](IntegrationsApi.md#update_instance) | **PUT** /api/integrations/instances/{instanceId} | [EXPERIMENTAL] UpdateInstance: Update a single integration instance.


# **create_instance**
> InstanceIdentifier create_instance(create_instance_request=create_instance_request)

[EXPERIMENTAL] CreateInstance: Create a single integration instance.

<br>Creates a new instance of an integration, returning its identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.create_instance_request import CreateInstanceRequest
from finbourne_horizon.models.instance_identifier import InstanceIdentifier
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)
    create_instance_request = {"integrationType":"copp-clark","name":"Payment Systems","description":"Payment systems calendar for GBP only","enabled":false,"triggers":[{"type":"time","cronExpression":"0 0 2 ? * *","timeZone":"UTC"}],"details":{"paymentSystemsCalendar":{"currencyFilter":["EUR"],"importUnqualified":false}}} # CreateInstanceRequest | The new integration instance. (optional)

    try:
        # [EXPERIMENTAL] CreateInstance: Create a single integration instance.
        api_response = await api_instance.create_instance(create_instance_request=create_instance_request)
        print("The response of IntegrationsApi->create_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->create_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_instance_request** | [**CreateInstanceRequest**](CreateInstanceRequest.md)| The new integration instance. | [optional] 

### Return type

[**InstanceIdentifier**](InstanceIdentifier.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Identifier of the created instance. |  -  |
**404** | The integration type does not exist. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_instance**
> delete_instance(instance_id)

[EXPERIMENTAL] DeleteInstance: Delete a single integration instance.

<br>Deletes an existing instance of an integration, returning its identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)
    instance_id = 'instance_id_example' # str | Instance identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

    try:
        # [EXPERIMENTAL] DeleteInstance: Delete a single integration instance.
        await api_instance.delete_instance(instance_id)
    except Exception as e:
        print("Exception when calling IntegrationsApi->delete_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The instance was deleted. |  -  |
**404** | The instance does not exist. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_instance**
> ExecuteInstanceResponse execute_instance(instance_id)

[EXPERIMENTAL] ExecuteInstance: Execute an integration instance.

<br>Starts execution of an instance, returning its execution identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.execute_instance_response import ExecuteInstanceResponse
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)
    instance_id = 'instance_id_example' # str | Instance identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".

    try:
        # [EXPERIMENTAL] ExecuteInstance: Execute an integration instance.
        api_response = await api_instance.execute_instance(instance_id)
        print("The response of IntegrationsApi->execute_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->execute_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 

### Return type

[**ExecuteInstanceResponse**](ExecuteInstanceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The execution id |  -  |
**404** | The integration instance does not exist |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema**
> str get_schema(integration)

[EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.

<br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)
    integration = 'integration_example' # str | The type of the integration e.g. \"copp-clark\".

    try:
        # [EXPERIMENTAL] GetSchema: Get the JSON schema for the details section of an integration instance.
        api_response = await api_instance.get_schema(integration)
        print("The response of IntegrationsApi->get_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| The type of the integration e.g. \&quot;copp-clark\&quot;. | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The system defined JSON schema for the details of a specified integration. |  -  |
**404** | The integration type does not exist or is not enabled. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_instances**
> IntegrationInstance list_instances()

[EXPERIMENTAL] ListInstances: List instances across all integrations.

<br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.integration_instance import IntegrationInstance
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)

    try:
        # [EXPERIMENTAL] ListInstances: List instances across all integrations.
        api_response = await api_instance.list_instances()
        print("The response of IntegrationsApi->list_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_instances: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IntegrationInstance**](IntegrationInstance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | The requested instance(s) do not exist. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> List[IntegrationDescription] list_integrations()

[EXPERIMENTAL] ListIntegrations: List available integrations.

<br>List all available integrations.  <br />  <br>    ```\"licensed\"``` indicates your domain is licensed to use this integration. To request a licence              contact your [FINBOURNE sales representative](https://www.finbourne.com/contact/).  <br />  <br>Any authenticated user can call this method.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.integration_description import IntegrationDescription
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)

    try:
        # [EXPERIMENTAL] ListIntegrations: List available integrations.
        api_response = await api_instance.list_integrations()
        print("The response of IntegrationsApi->list_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->list_integrations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[IntegrationDescription]**](IntegrationDescription.md)

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

# **update_instance**
> update_instance(instance_id, update_instance_request=update_instance_request)

[EXPERIMENTAL] UpdateInstance: Update a single integration instance.

<br>Updates an existing instance of an integration, returning its identifier.  <br />  <br />  <br>The user must be authenticated, entitled to call this method, and the user's domain must be licensed for the integration.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.update_instance_request import UpdateInstanceRequest
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    IntegrationsApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.IntegrationsApi)
    instance_id = 'instance_id_example' # str | Instance identifier e.g. \"b64135e7-98a0-41af-a845-d86167d54cc7\".
    update_instance_request = {"id":"b64135e7-98a0-41af-a845-d86167d54cc7","integrationType":"copp-clark","name":"Payment Systems","description":"Payment Systems calendar for EUR only","enabled":false,"triggers":[{"type":"time","cronExpression":"0 0 5 ? * *","timeZone":"UTC"}],"details":{"paymentSystemsCalendar":{"currencyFilter":["EUR"],"importUnqualified":false}}} # UpdateInstanceRequest | The new integration instance. (optional)

    try:
        # [EXPERIMENTAL] UpdateInstance: Update a single integration instance.
        await api_instance.update_instance(instance_id, update_instance_request=update_instance_request)
    except Exception as e:
        print("Exception when calling IntegrationsApi->update_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance identifier e.g. \&quot;b64135e7-98a0-41af-a845-d86167d54cc7\&quot;. | 
 **update_instance_request** | [**UpdateInstanceRequest**](UpdateInstanceRequest.md)| The new integration instance. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The instance was updated. |  -  |
**404** | The instance does not exist. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

