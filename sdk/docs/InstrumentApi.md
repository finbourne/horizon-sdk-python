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

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.onboard_instrument_request import OnboardInstrumentRequest
from finbourne_horizon.models.onboard_instrument_response import OnboardInstrumentResponse
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.InstrumentApi)
    onboard_instrument_request = finbourne_horizon.OnboardInstrumentRequest() # OnboardInstrumentRequest | 

    try:
        # [EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.
        api_response = await api_instance.create_instrument(onboard_instrument_request)
        print("The response of InstrumentApi->create_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->create_instrument: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **onboard_instrument_request** | [**OnboardInstrumentRequest**](OnboardInstrumentRequest.md)|  | 

### Return type

[**OnboardInstrumentResponse**](OnboardInstrumentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrich_instrument**
> EnrichmentResponse enrich_instrument(vendor_product_key, identifiers)

[EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.enrichment_response import EnrichmentResponse
from finbourne_horizon.models.identifiers import Identifiers
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.InstrumentApi)
    vendor_product_key = 'vendor_product_key_example' # str | 
    identifiers = finbourne_horizon.Identifiers() # Identifiers | 

    try:
        # [EARLY ACCESS] EnrichInstrument: Enriches an existing LUSID instrument using vendor data. Enrichment included identifiers, properties and market data.
        api_response = await api_instance.enrich_instrument(vendor_product_key, identifiers)
        print("The response of InstrumentApi->enrich_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->enrich_instrument: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_product_key** | **str**|  | 
 **identifiers** | [**Identifiers**](Identifiers.md)|  | 

### Return type

[**EnrichmentResponse**](EnrichmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_figi_parameter_option**
> List[AllowedParameterValue] get_open_figi_parameter_option(parameter_name)

[EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.allowed_parameter_value import AllowedParameterValue
from finbourne_horizon.models.open_figi_parameter_option_name import OpenFigiParameterOptionName
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.InstrumentApi)
    parameter_name = finbourne_horizon.OpenFigiParameterOptionName() # OpenFigiParameterOptionName | 

    try:
        # [EARLY ACCESS] GetOpenFigiParameterOption: Get all supported market sector values for OpenFigi search
        api_response = await api_instance.get_open_figi_parameter_option(parameter_name)
        print("The response of InstrumentApi->get_open_figi_parameter_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->get_open_figi_parameter_option: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_name** | [**OpenFigiParameterOptionName**](.md)|  | 

### Return type

[**List[AllowedParameterValue]**](AllowedParameterValue.md)

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

# **retrieve_perm_id_result**
> List[PermIdData] retrieve_perm_id_result(id)

[EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.perm_id_data import PermIdData
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.InstrumentApi)
    id = 'id_example' # str | The execution ID returned by a previous query

    try:
        # [EARLY ACCESS] RetrievePermIdResult: Retrieve PermId results from a previous query.
        api_response = await api_instance.retrieve_perm_id_result(id)
        print("The response of InstrumentApi->retrieve_perm_id_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->retrieve_perm_id_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The execution ID returned by a previous query | 

### Return type

[**List[PermIdData]**](PermIdData.md)

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

# **search_open_figi**
> OpenFigiSearchResult search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector)

[EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.open_figi_search_result import OpenFigiSearchResult
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.InstrumentApi)
    query = 'query_example' # str | 
    use_perm_id = False # bool | Should also search PermId for additional information, defaults to `false`. (default to False)
    limit = 25 # int | Only affects results rom OpenFigi general text search (optional) (default to 25)
    market_sector = 'All' # str | The market sector to search, defaults to `All`. (optional) (default to 'All')

    try:
        # [EARLY ACCESS] SearchOpenFigi: Search OpenFigi for instruments that match the specified terms.
        api_response = await api_instance.search_open_figi(query, use_perm_id, limit=limit, market_sector=market_sector)
        print("The response of InstrumentApi->search_open_figi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->search_open_figi: %s\n" % e)
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

# **vendors**
> List[VendorProduct] vendors(market_sector, security_type, limit=limit)

[EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_horizon
from finbourne_horizon.rest import ApiException
from finbourne_horizon.models.vendor_product import VendorProduct
from pprint import pprint

from finbourne_horizon import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_horizon.InstrumentApi)
    market_sector = 'market_sector_example' # str | 
    security_type = 'security_type_example' # str | 
    limit = 56 # int |  (optional)

    try:
        # [EARLY ACCESS] Vendors: Gets the VendorProducts of any supported and licenced integrations for a given market sector and security type.
        api_response = await api_instance.vendors(market_sector, security_type, limit=limit)
        print("The response of InstrumentApi->vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstrumentApi->vendors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market_sector** | **str**|  | 
 **security_type** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[VendorProduct]**](VendorProduct.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

