# LUSID<sup>®</sup> Horizon Python SDK

![LUSID_by_Finbourne](https://content.finbourne.com/LUSID_repo.png)

| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/finbourne-horizon-sdk?color=blue)

## Installation

The PyPi package for the LUSID Horizon SDK can installed using the following:

```
$ pip install finbourne-horizon-sdk finbourne-sdk-utilities
```

## Usage

```
import finbourne_horizon
from fbnsdkutilities import ApiClientFactory

api_factory = ApiClientFactory(finbourne_horizon, api_secrets_filename="secrets.json")
```
