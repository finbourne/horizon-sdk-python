# coding: utf-8

"""
    FINBOURNE Horizon API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic.v1 import Field, StrictStr, conint, conlist, constr, validator

from typing import Optional

from finbourne_horizon.models.paged_resource_list_of_i_integration_log_response import PagedResourceListOfIIntegrationLogResponse

from finbourne_horizon.api_client import ApiClient
from finbourne_horizon.api_response import ApiResponse
from finbourne_horizon.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions


class LogsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def get_integration_log_results(self, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set.")] = None, sort_by : Annotated[Optional[conlist(StrictStr)], Field(description="A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\".")] = None, limit : Annotated[Optional[conint(strict=True, le=5000, ge=1)], Field(description="When paginating, limit the results to this number.")] = None, page_token : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.")] = None, **kwargs) -> PagedResourceListOfIIntegrationLogResponse:  # noqa: E501
        ...

    @overload
    def get_integration_log_results(self, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set.")] = None, sort_by : Annotated[Optional[conlist(StrictStr)], Field(description="A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\".")] = None, limit : Annotated[Optional[conint(strict=True, le=5000, ge=1)], Field(description="When paginating, limit the results to this number.")] = None, page_token : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.")] = None, async_req: Optional[bool]=True, **kwargs) -> PagedResourceListOfIIntegrationLogResponse:  # noqa: E501
        ...

    @validate_arguments
    def get_integration_log_results(self, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set.")] = None, sort_by : Annotated[Optional[conlist(StrictStr)], Field(description="A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\".")] = None, limit : Annotated[Optional[conint(strict=True, le=5000, ge=1)], Field(description="When paginating, limit the results to this number.")] = None, page_token : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[PagedResourceListOfIIntegrationLogResponse, Awaitable[PagedResourceListOfIIntegrationLogResponse]]:  # noqa: E501
        """[EXPERIMENTAL] GetIntegrationLogResults: Get integration log results  # noqa: E501

        Get integration log results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_integration_log_results(filter, sort_by, limit, page_token, async_req=True)
        >>> result = thread.get()

        :param filter: Expression to filter the result set.
        :type filter: str
        :param sort_by: A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\".
        :type sort_by: List[str]
        :param limit: When paginating, limit the results to this number.
        :type limit: int
        :param page_token: The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.
        :type page_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PagedResourceListOfIIntegrationLogResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_integration_log_results_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_integration_log_results_with_http_info(filter, sort_by, limit, page_token, **kwargs)  # noqa: E501

    @validate_arguments
    def get_integration_log_results_with_http_info(self, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set.")] = None, sort_by : Annotated[Optional[conlist(StrictStr)], Field(description="A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\".")] = None, limit : Annotated[Optional[conint(strict=True, le=5000, ge=1)], Field(description="When paginating, limit the results to this number.")] = None, page_token : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] GetIntegrationLogResults: Get integration log results  # noqa: E501

        Get integration log results  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_integration_log_results_with_http_info(filter, sort_by, limit, page_token, async_req=True)
        >>> result = thread.get()

        :param filter: Expression to filter the result set.
        :type filter: str
        :param sort_by: A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\".
        :type sort_by: List[str]
        :param limit: When paginating, limit the results to this number.
        :type limit: int
        :param page_token: The pagination token to use to continue listing integration logs; this value is returned from              the previous call. If a pagination token is provided, the <i>sortBy</i> and <i>filter</i> fields must not have changed since the original request.              For more information, see https://support.lusid.com/knowledgebase/article/KA-01915.
        :type page_token: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PagedResourceListOfIIntegrationLogResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter',
            'sort_by',
            'limit',
            'page_token'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_integration_log_results" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('sort_by') is not None:  # noqa: E501
            _query_params.append(('sortBy', _params['sort_by']))
            _collection_formats['sortBy'] = 'multi'

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('page_token') is not None:  # noqa: E501
            _query_params.append(('pageToken', _params['page_token']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "PagedResourceListOfIIntegrationLogResponse",
            '404': None,
        }

        return self.api_client.call_api(
            '/api/logs', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
