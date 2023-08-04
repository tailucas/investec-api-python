from .http_api_client import HttpApiClient

"""
https://developer.investec.com/za/api-products/documentation/SA_Card_Code
"""
class SACardCode(HttpApiClient):

    def get_cards(self)-> dict:
        url = f'{self._url}/za/v1/cards'
        return self._query_api_get(url)['cards']
