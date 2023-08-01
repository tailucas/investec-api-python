ENDPOINT_SANDBOX = 'openapisandbox.investec.com'
ENDPOINT_PRODUCTION = 'openapi.investec.com'
URL_SANDBOX = f'https://{ENDPOINT_SANDBOX}'
URL_PRODUCTION = f'https://{ENDPOINT_PRODUCTION}'
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'application/json'
}
from .sa_pb_account_information import SAPBAccountInformation
