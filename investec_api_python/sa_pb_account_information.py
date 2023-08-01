from .client import InvestecOpenApiClient


"""
https://developer.investec.com/za/api-products/documentation/SA_PB_Account_Information
"""
class SAPBAccountInformation(InvestecOpenApiClient):

  def __init__(self, client_id, secret, api_key, use_sandbox=False, additional_headers=None):
    super().__init__(
        client_id=client_id,
        secret=secret,
        api_key=api_key,
        use_sandbox=use_sandbox,
        additional_headers=additional_headers)

  def get_accounts(self)-> dict:
      url = f'{self._url}/za/pb/v1/accounts'
      return self.query_api_get(url)['accounts']

  def get_account_balance(self, account_id) -> dict:
      url = f'{self._url}/za/pb/v1/accounts/{account_id}/balance'
      return self.query_api_get(url)

  def get_account_transactions(self, account_id) -> dict:
      url = f'{self._url}/za/pb/v1/accounts/{account_id}/transactions'
      return self.query_api_get(url)['transactions']

  def transfer(self, account_id, beneficiary, amount) -> dict:
      data = f'beneficiaryAccountId={beneficiary}&amount={amount}&myReference=API transfer&theirReference=API transfer'
      url = f'{self._url}/za/pb/v1/accounts/{account_id}/transactions'
      return self.query_api_post(url, data)

  def get_cards(self) -> dict:
      url = f'{self._url}/za/v1/cards'
      return self.query_api_get(url)['result']

  def get_countries(self) -> dict:
      url = f'{self._url}/za/v1/cards/countries'
      return self.query_api_get(url)['result']

  def get_currencies(self) -> dict:
      url = f'{self._url}/za/v1/cards/currencies'
      return self.query_api_get(url)['result']

  def get_merchants(self) -> dict:
      url = f'{self._url}/za/v1/cards/merchants'
      return self.query_api_get(url)['result']
