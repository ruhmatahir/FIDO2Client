# coding: utf-8

"""
    Simple FIDO API

    This is the FIDO API  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: ruhma@metrarc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RegistrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def finish_registration(self, body, **kwargs):  # noqa: E501
        """Complete the registration by submitting a signed challenge to the server  # noqa: E501

        Once the client has generated a authenticatorAttestationResponse to the server's registration request, this API must be called for the registration worrkflow to be completed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finish_registration(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticatorAttestationResponse body: Registration response (required)
        :return: ServerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.finish_registration_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.finish_registration_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def finish_registration_with_http_info(self, body, **kwargs):  # noqa: E501
        """Complete the registration by submitting a signed challenge to the server  # noqa: E501

        Once the client has generated a authenticatorAttestationResponse to the server's registration request, this API must be called for the registration worrkflow to be completed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.finish_registration_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthenticatorAttestationResponse body: Registration response (required)
        :return: ServerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method finish_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `finish_registration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/RegnResponse', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_registration(self, body, **kwargs):  # noqa: E501
        """Generate a registration FIDO challenge for the client  # noqa: E501

        During the registration ceremony, when users or the VCHolder wants to initiate the registration of a new FIDO key, they will call this API. The users can send thier username or displayName as an optional request, but the server does not have to use those values when creating the response. The servcer response will be a JSON formatted PublicKeyCredentialCreationOptions dictionary, which will be used by the client in order  to create a PublicKeyCredential.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_registration(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegistrationRequest body: Values needed from the client to create a FIDO registration challenge (required)
        :return: PublicKeyCredentialCreationOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start_registration_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.start_registration_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def start_registration_with_http_info(self, body, **kwargs):  # noqa: E501
        """Generate a registration FIDO challenge for the client  # noqa: E501

        During the registration ceremony, when users or the VCHolder wants to initiate the registration of a new FIDO key, they will call this API. The users can send thier username or displayName as an optional request, but the server does not have to use those values when creating the response. The servcer response will be a JSON formatted PublicKeyCredentialCreationOptions dictionary, which will be used by the client in order  to create a PublicKeyCredential.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_registration_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegistrationRequest body: Values needed from the client to create a FIDO registration challenge (required)
        :return: PublicKeyCredentialCreationOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `start_registration`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/Register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicKeyCredentialCreationOptions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)