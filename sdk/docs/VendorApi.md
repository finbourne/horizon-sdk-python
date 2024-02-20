# finbourne_horizon.VendorApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_core_field_mappings_for_product_entity**](VendorApi.md#get_core_field_mappings_for_product_entity) | **GET** /api/vendor/mappings/fields | [EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product&#39;s entity.
[**get_optional_mappings_for_product_entity**](VendorApi.md#get_optional_mappings_for_product_entity) | **GET** /api/vendor/mappings/optional | [EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.
[**get_property_mappings_for_product_entity**](VendorApi.md#get_property_mappings_for_product_entity) | **GET** /api/vendor/mappings/properties | [EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product&#39;s entity
[**query_vendors**](VendorApi.md#query_vendors) | **POST** /api/vendor/$query | [EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.
[**set_optional_mappings_for_product_entity**](VendorApi.md#set_optional_mappings_for_product_entity) | **POST** /api/vendor/mappings/optional | [EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.


# **get_core_field_mappings_for_product_entity**
> List[LusidField] get_core_field_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product's entity.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.lusid_field import LusidField
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.VendorApi)
    vendor_name = 'vendor_name_example' # str | 
    product_name = 'product_name_example' # str | 
    lusid_entity_type = 'lusid_entity_type_example' # str | 
    lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

    try:
        # [EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product's entity.
        api_response = await api_instance.get_core_field_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
        print("The response of VendorApi->get_core_field_mappings_for_product_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->get_core_field_mappings_for_product_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | 
 **product_name** | **str**|  | 
 **lusid_entity_type** | **str**|  | 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**List[LusidField]**](LusidField.md)

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

# **get_optional_mappings_for_product_entity**
> Dict[str, LusidPropertyDefinitionOverrides] get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.lusid_property_definition_overrides import LusidPropertyDefinitionOverrides
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.VendorApi)
    vendor_name = 'vendor_name_example' # str | 
    product_name = 'product_name_example' # str | 
    lusid_entity_type = 'lusid_entity_type_example' # str | 
    lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

    try:
        # [EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.
        api_response = await api_instance.get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
        print("The response of VendorApi->get_optional_mappings_for_product_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->get_optional_mappings_for_product_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | 
 **product_name** | **str**|  | 
 **lusid_entity_type** | **str**|  | 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverrides]**](LusidPropertyDefinitionOverrides.md)

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

# **get_property_mappings_for_product_entity**
> List[LusidPropertyToVendorFieldMapping] get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product's entity

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.lusid_property_to_vendor_field_mapping import LusidPropertyToVendorFieldMapping
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.VendorApi)
    vendor_name = 'vendor_name_example' # str | 
    product_name = 'product_name_example' # str | 
    lusid_entity_type = 'lusid_entity_type_example' # str | 
    lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

    try:
        # [EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product's entity
        api_response = await api_instance.get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
        print("The response of VendorApi->get_property_mappings_for_product_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->get_property_mappings_for_product_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | 
 **product_name** | **str**|  | 
 **lusid_entity_type** | **str**|  | 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**List[LusidPropertyToVendorFieldMapping]**](LusidPropertyToVendorFieldMapping.md)

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

# **query_vendors**
> PagedResourceListOfVendorProduct query_vendors(query_request)

[EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.paged_resource_list_of_vendor_product import PagedResourceListOfVendorProduct
from finbourne_horizon.models.query_request import QueryRequest
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.VendorApi)
    query_request = finbourne_horizon.QueryRequest() # QueryRequest | 

    try:
        # [EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.
        api_response = await api_instance.query_vendors(query_request)
        print("The response of VendorApi->query_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->query_vendors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**PagedResourceListOfVendorProduct**](PagedResourceListOfVendorProduct.md)

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

# **set_optional_mappings_for_product_entity**
> Dict[str, LusidPropertyDefinitionOverridesResponse] set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.lusid_property_definition_overrides import LusidPropertyDefinitionOverrides
from finbourne_horizon.models.lusid_property_definition_overrides_response import LusidPropertyDefinitionOverridesResponse
from pprint import pprint

import os
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.VendorApi)
    vendor_name = 'vendor_name_example' # str | 
    product_name = 'product_name_example' # str | 
    lusid_entity_type = 'lusid_entity_type_example' # str | 
    request_body = {"Domain/LUSID-Scope/Code1":{"displayNameOverride":"descriptionOverride","descriptionOverride":"displayNameOverride"},"Domain/LUSID-Scope/Code2":{"displayNameOverride":"descriptionOverride","descriptionOverride":"displayNameOverride"}} # Dict[str, LusidPropertyDefinitionOverrides] | 
    lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

    try:
        # [EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.
        api_response = await api_instance.set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type)
        print("The response of VendorApi->set_optional_mappings_for_product_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->set_optional_mappings_for_product_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_name** | **str**|  | 
 **product_name** | **str**|  | 
 **lusid_entity_type** | **str**|  | 
 **request_body** | [**Dict[str, LusidPropertyDefinitionOverrides]**](LusidPropertyDefinitionOverrides.md)|  | 
 **lusid_entity_sub_type** | **str**|  | [optional] 

### Return type

[**Dict[str, LusidPropertyDefinitionOverridesResponse]**](LusidPropertyDefinitionOverridesResponse.md)

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

