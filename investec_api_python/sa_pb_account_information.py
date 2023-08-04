from .http_api_client import HttpApiClient

"""
https://developer.investec.com/za/api-products/documentation/SA_PB_Account_Information
"""
class SAPBAccountInformation(HttpApiClient):

    def get_accounts(self)-> dict:
        url = f'{self._url}/za/pb/v1/accounts'
        return self._query_api_get(url)['accounts']

    def get_account_balance(self, account_id) -> dict:
        url = f'{self._url}/za/pb/v1/accounts/{account_id}/balance'
        return self._query_api_get(url)

    def get_account_transactions(self, account_id, from_date=None, to_date=None, transaction_type=None) -> dict:
        params = {}
        if from_date:
            params.update({'fromDate': from_date})
        if to_date:
            params.update({'toDate': to_date})
        if transaction_type:
            params.update({'transactionType': transaction_type})
        if len(params) == 0:
            params = None
        url = f'{self._url}/za/pb/v1/accounts/{account_id}/transactions'
        return self._query_api_get(url=url, params=params)['transactions']

    def transfer(self, account_id, beneficiary_account_id, amount, my_reference, their_reference) -> dict:
        data = {
             'transferList': [{
                'beneficiaryAccountId': f'{beneficiary_account_id}',
                'amount': f'{amount}',
                'myReference': f'{my_reference}',
                'theirReference': f'{their_reference}'
             }]
        }
        url = f'{self._url}/za/pb/v1/accounts/{account_id}/transfermultiple'
        return self._query_api_post(url=url, data=data)

    def pay(self, account_id, beneficiary_id, amount, my_reference, their_reference) -> dict:
        data = {
             'paymentList': [{
                'beneficiaryId': f'{beneficiary_id}',
                'amount': f'{amount}',
                'myReference': f'{my_reference}',
                'theirReference': f'{their_reference}'
             }]
        }
        url = f'{self._url}/za/pb/v1/accounts/{account_id}/paymultiple'
        return self._query_api_post(url=url, data=data)

    def get_beneficiaries(self) -> dict:
        url = f'{self._url}/za/pb/v1/accounts/beneficiaries'
        return self._query_api_get(url)

    def get_beneficiary_categories(self) -> dict:
        url = f'{self._url}/za/pb/v1/accounts/beneficiarycategories'
        return self._query_api_get(url)
