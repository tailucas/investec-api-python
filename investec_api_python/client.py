import logging

from datetime import datetime
from typing import Dict, Tuple, Optional

log = logging.getLogger()

from .http_api_client import HttpApiClient
from .sa_card_code import SACardCode
from .sa_pb_account_information import SAPBAccountInformation


class InvestecOpenApiClient(SACardCode, SAPBAccountInformation):

    def __init__(self, client_id: str, secret: str, api_key: str, use_sandbox: bool=False, additional_headers: Optional[Dict[str, str]]=None, access_token: Optional[Tuple[str, datetime]]=None):
        HttpApiClient.__init__(
            self=self,
            client_id=client_id,
            secret=secret,
            api_key=api_key,
            use_sandbox=use_sandbox,
            additional_headers=additional_headers,
            access_token=access_token)
