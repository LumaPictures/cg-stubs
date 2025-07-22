from .error import *
from _typeshed import Incomplete

downcaseTokens: Incomplete
UNQUOTE_PAIRS: Incomplete
unquote: Incomplete
tchar: Incomplete
token: Incomplete
token68: Incomplete
quoted_string: Incomplete
auth_param_name: Incomplete
auth_param: Incomplete
params: Incomplete
scheme: Incomplete
challenge: Incomplete
authentication_info: Incomplete
www_authenticate: Incomplete

def _parse_authentication_info(headers, headername: str = 'authentication-info'):
    """https://tools.ietf.org/html/rfc7615
    """
def _parse_www_authenticate(headers, headername: str = 'www-authenticate'):
    """Returns a dictionary of dictionaries, one dict per auth_scheme."""
