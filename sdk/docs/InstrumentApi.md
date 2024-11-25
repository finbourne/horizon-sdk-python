# finbourne_horizon.InstrumentApi

All URIs are relative to *https://fbn-prd.lusid.com/horizon*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_instrument**](InstrumentApi.md#create_instrument) | **POST** /api/instrument/onboarding/create | [EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.
[**enrich_instrument**](InstrumentApi.md#enrich_instrument) | **POST** /api/instrument/onboarding/enrich | [EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.
[**get_open_figi_parameter_option**](InstrumentApi.md#get_open_figi_parameter_option) | **GET** /api/instrument/onboarding/search/openfigi/parameterOptions | [EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search
[**retrieve_perm_id_result**](InstrumentApi.md#retrieve_perm_id_result) | **GET** /api/instrument/onboarding/search/permid/{id} | [EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.
[**search_open_figi**](InstrumentApi.md#search_open_figi) | **GET** /api/instrument/onboarding/search/openfigi | [EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.
[**vendors**](InstrumentApi.md#vendors) | **GET** /api/instrument/onboarding/vendors | [EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.


# **create_instrument**
> OnboardInstrumentResponse create_instrument(onboard_instrument_request)

[EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    InstrumentApi
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
    api_instance = api_client_factory.build(InstrumentApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # onboard_instrument_request = OnboardInstrumentRequest.from_json("")
    # onboard_instrument_request = OnboardInstrumentRequest.from_dict({})
    onboard_instrument_request = OnboardInstrumentRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_instrument(onboard_instrument_request, opts=opts)

        # [EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.
        api_response = api_instance.create_instrument(onboard_instrument_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentApi->create_instrument: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboard_instrument_request** | [**OnboardInstrumentRequest**](OnboardInstrumentRequest.md)|  | 

### Return type

[**OnboardInstrumentResponse**](OnboardInstrumentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **enrich_instrument**
> EnrichmentResponse enrich_instrument(vendor_product_key, identifiers)

[EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    InstrumentApi
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
    api_instance = api_client_factory.build(InstrumentApi)
    vendor_product_key = 'vendor_product_key_example' # str | 

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # identifiers = Identifiers.from_json("")
    # identifiers = Identifiers.from_dict({})
    identifiers = Identifiers()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.enrich_instrument(vendor_product_key, identifiers, opts=opts)

        # [EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.
        api_response = api_instance.enrich_instrument(vendor_product_key, identifiers)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentApi->enrich_instrument: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_product_key** | **str**|  | 
 **identifiers** | [**Identifiers**](Identifiers.md)|  | 

### Return type

[**EnrichmentResponse**](EnrichmentResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_open_figi_parameter_option**
> List[AllowedParameterValue] get_open_figi_parameter_option(parameter_name)

[EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    InstrumentApi
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
    api_instance = api_client_factory.build(InstrumentApi)
    parameter_name = finbourne_horizon.OpenFigiParameterOptionName() # OpenFigiParameterOptionName | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_open_figi_parameter_option(parameter_name, opts=opts)

        # [EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search
        api_response = api_instance.get_open_figi_parameter_option(parameter_name)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentApi->get_open_figi_parameter_option: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_name** | [**OpenFigiParameterOptionName**](.md)|  | 

### Return type

[**List[AllowedParameterValue]**](AllowedParameterValue.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **retrieve_perm_id_result**
> List[PermIdData] retrieve_perm_id_result(id)

[EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    InstrumentApi
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
    api_instance = api_client_factory.build(InstrumentApi)
    id = 'id_example' # str | The execution ID returned by a previous query

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.retrieve_perm_id_result(id, opts=opts)

        # [EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.
        api_response = api_instance.retrieve_perm_id_result(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentApi->retrieve_perm_id_result: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The execution ID returned by a previous query | 

### Return type

[**List[PermIdData]**](PermIdData.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **search_open_figi**
> OpenFigiSearchResult search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector)

[EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    InstrumentApi
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
    api_instance = api_client_factory.build(InstrumentApi)
    query = 'query_example' # str | 
    use_perm_id = False # bool | Should also search PermId for additional information, defaults to `false`. (default to False)
    limit = 25 # int | Only affects results rom OpenFigi general text search (optional) (default to 25)
    market_sector = 'All' # str | The market sector to search, defaults to `All`. (optional) (default to 'All')

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector, opts=opts)

        # [EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.
        api_response = api_instance.search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentApi->search_open_figi: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **use_perm_id** | **bool**| Should also search PermId for additional information, defaults to &#x60;false&#x60;. | [default to False]
 **limit** | **int**| Only affects results rom OpenFigi general text search | [optional] [default to 25]
 **market_sector** | **str**| The market sector to search, defaults to &#x60;All&#x60;. | [optional] [default to &#39;All&#39;]

### Return type

[**OpenFigiSearchResult**](OpenFigiSearchResult.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **vendors**
> List[VendorProduct] vendors(market_sector, security_type, general_security_type)

[EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.

### Example

```python
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    SyncApiClientFactory,
    InstrumentApi
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
    api_instance = api_client_factory.build(InstrumentApi)
    market_sector = 'market_sector_example' # str | 
    security_type = 'security_type_example' # str | 
    general_security_type = 'general_security_type_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.vendors(market_sector, security_type, general_security_type, opts=opts)

        # [EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.
        api_response = api_instance.vendors(market_sector, security_type, general_security_type)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling InstrumentApi->vendors: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_sector** | **str**|  | 
 **security_type** | **str**|  | 
 **general_security_type** | **str**|  | 

### Return type

[**List[VendorProduct]**](VendorProduct.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

