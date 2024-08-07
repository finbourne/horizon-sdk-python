![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# Python SDK for the FINBOURNE Horizon API

## Contents

- [Summary](#summary)
- [Versions](#versions)
- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
    * [Environment variables](#environment-variables)
    * [Secrets file](#secrets-file)
    * [Example](#example)
- [Endpoints and models](#endpoints-and-models)

## Summary

This is the python SDK for the FINBOURNE Horizon API, part of the [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology) platform. To use it you'll need a LUSID account - [sign up for free at lusid.com](https://www.lusid.com/app/signup).



For more details on other applications in the LUSID platform, see [Understanding all the applications in the LUSID platform](https://support.lusid.com/knowledgebase/article/KA-01787).

This sdk supports `Production`, `Early Access`, `Beta` and `Experimental` API endpoints. For more details on API endpoint categories, see [What is the LUSID feature release lifecycle](https://support.lusid.com/knowledgebase/article/KA-01786). To find out which category an API endpoint falls into, see the [swagger page](https://fbn-prd.lusid.com/horizon/swagger/index.html).

This code is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project.

## Versions

- API version: 0.1.638
- SDK version: 2.1.91

## Requirements

- Python 3.7+

## Installation

If using [poetry](https://python-poetry.org/docs/)

```
poetry add finbourne-horizon-sdk
```

If using [pip](https://pypi.org/project/pip/)

```
pip install finbourne-horizon-sdk
```

Then import the package in your python file
```python
import finbourne_horizon
```

## Getting Started

You'll need to provide some configuration to connect to the FINBOURNE Horizon API - see the articles about [short-lived access tokens](https://support.lusid.com/knowledgebase/article/KA-01654) and a [long-lived Personal Access Token](https://support.lusid.com/knowledgebase/article/KA-01774). This configuration can be provided using a secrets file or environment variables. 

### Environment variables

Required for a short-lived access token
``` 
FBN_TOKEN_URL
FBN_HORIZON_URL
FBN_USERNAME
FBN_PASSWORD
FBN_CLIENT_ID
FBN_CLIENT_SECRET
```

Required for a long-lived access token
``` 
FBN_HORIZON_URL
FBN_ACCESS_TOKEN
```

You can send your requests to the FINBOURNE Horizon API via a proxy, by setting `FBN_PROXY_ADDRESS`. If your proxy has basic auth enabled, you must also set `FBN_PROXY_USERNAME` and `FBN_PROXY_PASSWORD`.

### Secrets file

The secrets file must be in the current working directory.

Required for a short-lived access token
```json
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "horizonUrl":"https://<your-domain>.lusid.com/horizon",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>",
    }
}
```

Required for a long-lived access token
```json
{
    "api":
    {
        "horizonUrl":"https://<your-domain>.lusid.com/horizon",
        "accessToken":"<your-access-token>"
    }
}
```

You can send your requests to the FINBOURNE Horizon API via a proxy, by adding a proxy section. If your proxy has basic auth enabled, you must also supply a `username` and `password` in this section.

```json
{
    "api":
    {
        "horizonUrl":"https://<your-domain>.lusid.com/horizon",
        "accessToken":"<your-access-token>"
    },
    "proxy":
    {
        "address":"<your-proxy-address>",
        "username":"<your-proxy-username>",
        "password":"<your-proxy-password>"
    }
}
```

### Example
```python
import asyncio
from finbourne_horizon.exceptions import ApiException
from finbourne_horizon.models import *
from pprint import pprint
from finbourne_horizon import (
    ApiClientFactory,
    InstrumentApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(InstrumentApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # onboard_instrument_request = OnboardInstrumentRequest()
        # onboard_instrument_request = OnboardInstrumentRequest.from_json("")
        onboard_instrument_request = OnboardInstrumentRequest.from_dict(finbourne_horizon.OnboardInstrumentRequest()) # OnboardInstrumentRequest | 

        try:
            # [EARLY ACCESS] CreateInstrument: Creates and masters instruments with third party vendors.
            api_response = await api_instance.create_instrument(onboard_instrument_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling InstrumentApi->create_instrument: %s\n" % e)

asyncio.run(main())
```


## Endpoints and models

- See [Documentation for API Endpoints](sdk/README.md#documentation-for-api-endpoints) for a description of each endpoint
- See [Documentation for Models](sdk/README.md#documentation-for-models) for descriptions of the models used

