import logging


log = logging.getLogger()

from .http_api_client import HttpApiClient
from .sa_card_code import SACardCode
from .sa_pb_account_information import SAPBAccountInformation


class InvestecOpenApiClient(SACardCode, SAPBAccountInformation):

    def __init__(self, client_id, secret, api_key, use_sandbox=False, additional_headers=None):
        HttpApiClient.__init__(
            self=self,
            client_id=client_id,
            secret=secret,
            api_key=api_key,
            use_sandbox=use_sandbox,
            additional_headers=additional_headers)
