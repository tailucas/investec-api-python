import json
import logging
import requests


from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
from typing import Dict, Tuple, Optional

from . import (
   DEFAULT_REQUEST_HEADERS,
   ENDPOINT_SANDBOX,
   ENDPOINT_PRODUCTION,
   URL_SANDBOX,
   URL_PRODUCTION
)

log = logging.getLogger()


class HttpApiClient:

    @property
    def access_token(self) -> Optional[str]:
        return self._access_token

    @property
    def access_token_expiry(self) -> Optional[datetime]:
        return self._token_expiry

    def __init__(self, client_id: str, secret: str, api_key: str, use_sandbox: bool=False, additional_headers: Optional[Dict[str, str]]=None, access_token: Optional[Tuple[str, datetime]]=None):
        self._client_id: str = client_id
        self._secret: str = secret
        self._api_key: str = api_key
        self._host: str = ENDPOINT_PRODUCTION
        self._url: str = URL_PRODUCTION
        if use_sandbox:
            self._host = ENDPOINT_SANDBOX
            self._url = URL_SANDBOX
        self._additional_headers: Optional[Dict[str, str]] = additional_headers
        self._access_token: Optional[str] = None
        self._token_expiry: Optional[datetime] = None
        if access_token:
            self._access_token, self._token_expiry = access_token

    def _get_token(self) -> str:
        # treat access token as expired a minute ahead of actual expiry
        if self._access_token and self._token_expiry:
            if self._token_expiry + timedelta(seconds=60) >= datetime.now():
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

    def _get_base_headers(self, additional: Optional[Dict[str, str]]=None) -> Dict:
        headers = dict(DEFAULT_REQUEST_HEADERS)
        headers['Host'] = self._host
        if additional:
            headers.update(additional)
        if self._additional_headers:
            headers.update(self._additional_headers)
        return headers

    def _get_request_headers(self, additional: Optional[Dict[str, str]]=None):
        headers = {'Authorization': f'Bearer {self._get_token()}'}
        if additional:
            headers.update(additional)
        return self._get_base_headers(additional=headers)

    def _query_api_get(self, url: str, params: Optional[Dict[str, str]]=None) -> Dict:
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

    def _query_api_post(self, url: str, data: str) -> Dict:
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
