import hutil.json
import hutil.web
from collections.abc import Callable, Mapping
from houtypes import JSONLike, JSONValue
from typing import Any, TypedDict

from typing import TypeVar
from typing import TypeVar
_F = TypeVar('_F', bound=Callable[..., Any])
class _ReadUrlKwargs(TypedDict):
    url: str
    post_data: bytes
    extra_headers: list[tuple[str, str]]

class API:
    """Methods of this class define the API that is invoked by URLs using
    the custom URL scheme.
    """
    class Error(Exception): ...
    api_functions: dict[str, dict[float, Callable[..., Any]]]
    @classmethod
    def register_api_function(cls, api_version: float) -> Callable[[_F], _F]:
        """Return a decorator that marks a method as being part of a particular
        version of the API.
        """
    def find_api_function_and_validate_args(self, function_name: str, kwargs: Mapping[str, object], api_version: float) -> Callable[..., Any]:
        """Make sure the given API function name is valid, and make sure exactly
        the right keyword arguments are being passed to it.
        """
    def find_api_function(self, function_name: str, desired_api_version: float) -> Callable[..., Any] | None:
        """Look up an API function with the given name, returning None if no
        such function exists.  If a function with the matching API version is
        found it is returned.  Otherwise, the function with the next lowest API
        version is returned.
        """

class ClientSessionData:
    session_key: str
    def __init__(self, session_key: str) -> None: ...

class ClientAPIConnection:
    server_url: str
    session_data: ClientSessionData | None
    FileArg: type[hutil.web.FileArg]
    def __init__(self, server_url: str, session_data: ClientSessionData | None) -> None: ...
    def __getattr__(self, name: str) -> _ClientAPIConnectionFunction: ...

class APICallFailed(Exception): ...
class APIUnavailable(Exception): ...

class _ClientAPIConnectionFunction:
    server_url: str
    session_data: ClientSessionData | None
    name: str
    def __init__(self, server_url: str, session_data: ClientSessionData | None, name: str) -> None: ...
    def __call__(self, *args: JSONLike, **kwargs: JSONLike | hutil.web.FileArg) -> hutil.json.DictAsObject | list[JSONValue] | str | int | float | bool | None: ...
    def kwargs_for_read_url(self, *args: JSONLike, **kwargs: JSONLike | hutil.web.FileArg) -> _ReadUrlKwargs: ...
