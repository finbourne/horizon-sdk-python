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

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi
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
        api_instance = api_client_factory.build(VendorApi)
        vendor_name = 'vendor_name_example' # str | 
        product_name = 'product_name_example' # str | 
        lusid_entity_type = 'lusid_entity_type_example' # str | 
        lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_core_field_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type, opts=opts)

            # [EARLY ACCESS] GetCoreFieldMappingsForProductEntity: Get core field mappings for a given vendor product's entity.
            api_response = await api_instance.get_core_field_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorApi->get_core_field_mappings_for_product_entity: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_optional_mappings_for_product_entity**
> Dict[str, LusidPropertyDefinitionOverrides] get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi
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
        api_instance = api_client_factory.build(VendorApi)
        vendor_name = 'vendor_name_example' # str | 
        product_name = 'product_name_example' # str | 
        lusid_entity_type = 'lusid_entity_type_example' # str | 
        lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type, opts=opts)

            # [EARLY ACCESS] GetOptionalMappingsForProductEntity: Get a user defined LUSID property mappings for the specified vendor / LUSID entity.
            api_response = await api_instance.get_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorApi->get_optional_mappings_for_product_entity: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_property_mappings_for_product_entity**
> List[LusidPropertyToVendorFieldMapping] get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product's entity

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi
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
        api_instance = api_client_factory.build(VendorApi)
        vendor_name = 'vendor_name_example' # str | 
        product_name = 'product_name_example' # str | 
        lusid_entity_type = 'lusid_entity_type_example' # str | 
        lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type, opts=opts)

            # [EARLY ACCESS] GetPropertyMappingsForProductEntity: Gets the property mappings for a given vendor product's entity
            api_response = await api_instance.get_property_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, lusid_entity_sub_type=lusid_entity_sub_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorApi->get_property_mappings_for_product_entity: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **query_vendors**
> PagedResourceListOfVendorProduct query_vendors(query_request)

[EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi
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
        api_instance = api_client_factory.build(VendorApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # query_request = QueryRequest.from_json("")
        # query_request = QueryRequest.from_dict({})
        query_request = QueryRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.query_vendors(query_request, opts=opts)

            # [EARLY ACCESS] QueryVendors: Query for vendors and their packages with entities and sub-entities.
            api_response = await api_instance.query_vendors(query_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorApi->query_vendors: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)|  | 

### Return type

[**PagedResourceListOfVendorProduct**](PagedResourceListOfVendorProduct.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_optional_mappings_for_product_entity**
> Dict[str, LusidPropertyDefinitionOverridesResponse] set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type)

[EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.

### Example

```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    VendorApi
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
        api_instance = api_client_factory.build(VendorApi)
        vendor_name = 'vendor_name_example' # str | 
        product_name = 'product_name_example' # str | 
        lusid_entity_type = 'lusid_entity_type_example' # str | 
        request_body = {"0":{"displayNameOverride":"descriptionOverride","descriptionOverride":"displayNameOverride"},"1":{"displayNameOverride":"descriptionOverride","descriptionOverride":"displayNameOverride"}} # Dict[str, LusidPropertyDefinitionOverrides] | 
        lusid_entity_sub_type = 'lusid_entity_sub_type_example' # str |  (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type, opts=opts)

            # [EARLY ACCESS] SetOptionalMappingsForProductEntity: Create a user defined LUSID property mappings for the specified vendor / LUSID entity.
            api_response = await api_instance.set_optional_mappings_for_product_entity(vendor_name, product_name, lusid_entity_type, request_body, lusid_entity_sub_type=lusid_entity_sub_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorApi->set_optional_mappings_for_product_entity: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

