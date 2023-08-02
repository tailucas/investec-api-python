import json
import logging
import requests

from . import (
   ENDPOINT_SANDBOX,
   ENDPOINT_PRODUCTION,
   DEFAULT_REQUEST_HEADERS,
   URL_SANDBOX,
   URL_PRODUCTION
)

from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth


log = logging.getLogger()


"""
https://developer.investec.com/za/api-products/documentation/SA_Open_API_-_Authorization
"""
class InvestecOpenApiClient:

    def __init__(self, client_id, secret, api_key, use_sandbox=False, additional_headers=None):
        self._client_id = client_id
        self._secret = secret
        self._api_key = api_key
        self._host = ENDPOINT_PRODUCTION
        self._url = URL_PRODUCTION
        if use_sandbox:
            self._host = ENDPOINT_SANDBOX
            self._url = URL_SANDBOX
        self._additional_headers = additional_headers
        self._access_token = None
        self._token_expiry = datetime.now()

    def _get_base_headers(self, additional=None) -> dict:
        headers = dict(DEFAULT_REQUEST_HEADERS)
        headers['Host'] = self._host
        if additional:
            headers.update(additional)
        if self._additional_headers:
            headers.update(self._additional_headers)
        return headers

    def _get_token(self) -> str:
        access_token_expiry = datetime.now() + timedelta(seconds=60)
        if self._access_token is not None or self._token_expiry >= access_token_expiry:
            return self._access_token

        url = f'{self._url}/identity/v2/oauth2/token'
        headers = self._get_base_headers(additional={'Content-Type': 'application/x-www-form-urlencoded', 'x-api-key': self._api_key})
        log.debug(f'Access token refresh. POST to {url} with headers {headers.keys()}')
        response = requests.post(
            url,
            auth=HTTPBasicAuth(self._client_id, self._secret),
            headers=headers,
            data='grant_type=client_credentials'
        )
        response = response.json()

        self._access_token = response['access_token']
        self._token_expiry = datetime.now() + timedelta(seconds=response['expires_in'])
        return self._access_token

    def _get_request_headers(self, additional=None):
        headers = {'Authorization': f'Bearer {self._get_token()}'}
        if additional:
            headers.update(additional)
        return self._get_base_headers(additional=headers)

    def query_api_get(self, url, params=None) -> dict:
        headers = self._get_request_headers()
        if params is None:
            log.debug(f'GET {url} with headers {headers.keys()}')
        else:
            log.debug(f'GET {url} with headers {headers.keys()} and parameters {params.keys()}')
        response = requests.get(
            url=url,
            headers=headers,
            params=params)
        response.raise_for_status()
        return response.json()['data']

    def query_api_post(self, url, data) -> dict:
        headers = self._get_request_headers(additional={'Content-Type': 'application/json'})
        req_data = json.dumps(data)
        log.debug(f'POST {url} ({len(req_data)} bytes) with headers {headers.keys()}. {req_data=}')
        response = requests.post(
            url=url,
            headers=headers,
            data=req_data)
        log.debug(f'{response.headers=}: {response.text=}')
        response.raise_for_status()
        return response.json()