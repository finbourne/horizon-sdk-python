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

from pydantic.v1 import StrictStr

from typing import List, Optional

from finbourne_horizon.models.audit_complete_request import AuditCompleteRequest
from finbourne_horizon.models.audit_complete_response import AuditCompleteResponse
from finbourne_horizon.models.audit_update_request import AuditUpdateRequest
from finbourne_horizon.models.audit_update_response import AuditUpdateResponse
from finbourne_horizon.models.paged_resource_list_of_process_information import PagedResourceListOfProcessInformation
from finbourne_horizon.models.paged_resource_list_of_process_update_result import PagedResourceListOfProcessUpdateResult
from finbourne_horizon.models.process_information import ProcessInformation
from finbourne_horizon.models.query_request import QueryRequest

from finbourne_horizon.api_client import ApiClient
from finbourne_horizon.api_response import ApiResponse
from finbourne_horizon.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_horizon.extensions.configuration_options import ConfigurationOptions


class ProcessHistoryApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def create_complete_event(self, audit_complete_request : AuditCompleteRequest, **kwargs) -> AuditCompleteResponse:  # noqa: E501
        ...

    @overload
    def create_complete_event(self, audit_complete_request : AuditCompleteRequest, async_req: Optional[bool]=True, **kwargs) -> AuditCompleteResponse:  # noqa: E501
        ...

    @validate_arguments
    def create_complete_event(self, audit_complete_request : AuditCompleteRequest, async_req: Optional[bool]=None, **kwargs) -> Union[AuditCompleteResponse, Awaitable[AuditCompleteResponse]]:  # noqa: E501
        """[EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_complete_event(audit_complete_request, async_req=True)
        >>> result = thread.get()

        :param audit_complete_request: (required)
        :type audit_complete_request: AuditCompleteRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuditCompleteResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_complete_event_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_complete_event_with_http_info(audit_complete_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_complete_event_with_http_info(self, audit_complete_request : AuditCompleteRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] CreateCompleteEvent: Write a completed event to the Horizon Dashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_complete_event_with_http_info(audit_complete_request, async_req=True)
        >>> result = thread.get()

        :param audit_complete_request: (required)
        :type audit_complete_request: AuditCompleteRequest
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
        :rtype: tuple(AuditCompleteResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'audit_complete_request'
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
                    " to method create_complete_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['audit_complete_request'] is not None:
            _body_params = _params['audit_complete_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '201': "AuditCompleteResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/process-history/event/complete', 'POST',
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

    @overload
    async def create_update_event(self, audit_update_request : AuditUpdateRequest, **kwargs) -> AuditUpdateResponse:  # noqa: E501
        ...

    @overload
    def create_update_event(self, audit_update_request : AuditUpdateRequest, async_req: Optional[bool]=True, **kwargs) -> AuditUpdateResponse:  # noqa: E501
        ...

    @validate_arguments
    def create_update_event(self, audit_update_request : AuditUpdateRequest, async_req: Optional[bool]=None, **kwargs) -> Union[AuditUpdateResponse, Awaitable[AuditUpdateResponse]]:  # noqa: E501
        """[EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_update_event(audit_update_request, async_req=True)
        >>> result = thread.get()

        :param audit_update_request: (required)
        :type audit_update_request: AuditUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuditUpdateResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_update_event_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_update_event_with_http_info(audit_update_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_update_event_with_http_info(self, audit_update_request : AuditUpdateRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] CreateUpdateEvent: Write an update event to the Horizon Dashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_update_event_with_http_info(audit_update_request, async_req=True)
        >>> result = thread.get()

        :param audit_update_request: (required)
        :type audit_update_request: AuditUpdateRequest
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
        :rtype: tuple(AuditUpdateResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'audit_update_request'
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
                    " to method create_update_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['audit_update_request'] is not None:
            _body_params = _params['audit_update_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '201': "AuditUpdateResponse",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/process-history/event/update', 'POST',
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

    @overload
    async def get_latest_runs(self, **kwargs) -> List[ProcessInformation]:  # noqa: E501
        ...

    @overload
    def get_latest_runs(self, async_req: Optional[bool]=True, **kwargs) -> List[ProcessInformation]:  # noqa: E501
        ...

    @validate_arguments
    def get_latest_runs(self, async_req: Optional[bool]=None, **kwargs) -> Union[List[ProcessInformation], Awaitable[List[ProcessInformation]]]:  # noqa: E501
        """[EARLY ACCESS] GetLatestRuns: Get latest run for each process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_runs(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ProcessInformation]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_latest_runs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_latest_runs_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_latest_runs_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] GetLatestRuns: Get latest run for each process  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_runs_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(List[ProcessInformation], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method get_latest_runs" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
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
            '200': "List[ProcessInformation]",
        }

        return self.api_client.call_api(
            '/api/process-history/$latestRuns', 'GET',
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

    @overload
    async def process_entry_updates(self, run_id : StrictStr, query_request : QueryRequest, **kwargs) -> PagedResourceListOfProcessUpdateResult:  # noqa: E501
        ...

    @overload
    def process_entry_updates(self, run_id : StrictStr, query_request : QueryRequest, async_req: Optional[bool]=True, **kwargs) -> PagedResourceListOfProcessUpdateResult:  # noqa: E501
        ...

    @validate_arguments
    def process_entry_updates(self, run_id : StrictStr, query_request : QueryRequest, async_req: Optional[bool]=None, **kwargs) -> Union[PagedResourceListOfProcessUpdateResult, Awaitable[PagedResourceListOfProcessUpdateResult]]:  # noqa: E501
        """[EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.process_entry_updates(run_id, query_request, async_req=True)
        >>> result = thread.get()

        :param run_id: (required)
        :type run_id: str
        :param query_request: (required)
        :type query_request: QueryRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PagedResourceListOfProcessUpdateResult
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the process_entry_updates_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.process_entry_updates_with_http_info(run_id, query_request, **kwargs)  # noqa: E501

    @validate_arguments
    def process_entry_updates_with_http_info(self, run_id : StrictStr, query_request : QueryRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] ProcessEntryUpdates: Get process entry updates for a query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.process_entry_updates_with_http_info(run_id, query_request, async_req=True)
        >>> result = thread.get()

        :param run_id: (required)
        :type run_id: str
        :param query_request: (required)
        :type query_request: QueryRequest
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
        :rtype: tuple(PagedResourceListOfProcessUpdateResult, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'run_id',
            'query_request'
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
                    " to method process_entry_updates" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('run_id') is not None:  # noqa: E501
            _query_params.append(('runId', _params['run_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['query_request'] is not None:
            _body_params = _params['query_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "PagedResourceListOfProcessUpdateResult",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/process-history/entries/$query', 'POST',
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

    @overload
    async def process_history_entries(self, query_request : QueryRequest, process_name : Optional[StrictStr] = None, **kwargs) -> PagedResourceListOfProcessInformation:  # noqa: E501
        ...

    @overload
    def process_history_entries(self, query_request : QueryRequest, process_name : Optional[StrictStr] = None, async_req: Optional[bool]=True, **kwargs) -> PagedResourceListOfProcessInformation:  # noqa: E501
        ...

    @validate_arguments
    def process_history_entries(self, query_request : QueryRequest, process_name : Optional[StrictStr] = None, async_req: Optional[bool]=None, **kwargs) -> Union[PagedResourceListOfProcessInformation, Awaitable[PagedResourceListOfProcessInformation]]:  # noqa: E501
        """[EARLY ACCESS] ProcessHistoryEntries: Get process history entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.process_history_entries(query_request, process_name, async_req=True)
        >>> result = thread.get()

        :param query_request: (required)
        :type query_request: QueryRequest
        :param process_name:
        :type process_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PagedResourceListOfProcessInformation
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the process_history_entries_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.process_history_entries_with_http_info(query_request, process_name, **kwargs)  # noqa: E501

    @validate_arguments
    def process_history_entries_with_http_info(self, query_request : QueryRequest, process_name : Optional[StrictStr] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] ProcessHistoryEntries: Get process history entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.process_history_entries_with_http_info(query_request, process_name, async_req=True)
        >>> result = thread.get()

        :param query_request: (required)
        :type query_request: QueryRequest
        :param process_name:
        :type process_name: str
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
        :rtype: tuple(PagedResourceListOfProcessInformation, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'query_request',
            'process_name'
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
                    " to method process_history_entries" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('process_name') is not None:  # noqa: E501
            _query_params.append(('processName', _params['process_name']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['query_request'] is not None:
            _body_params = _params['query_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "PagedResourceListOfProcessInformation",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/process-history/$query', 'POST',
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
