from collections.abc import Callable, Mapping
from typing import Any, TypeVar, TypedDict

import hutil.json
import hutil.web
from houtypes import JSONLike, JSONValue


_F = TypeVar("_F", bound=Callable[..., Any])

class _ReadUrlKwargs(TypedDict):
    url: str
    post_data: bytes
    extra_headers: list[tuple[str, str]]

class API:
    class Error(Exception): ...
    api_functions: dict[str, dict[float, Callable[..., Any]]]
    @classmethod
    def register_api_function(cls, api_version: float) -> Callable[[_F], _F]: ...
    def find_api_function_and_validate_args(
        self, function_name: str, kwargs: Mapping[str, object], api_version: float
    ) -> Callable[..., Any]: ...
    def find_api_function(self, function_name: str, desired_api_version: float) -> Callable[..., Any] | None: ...

class ClientSessionData:
    session_key: str
    def __init__(self, session_key: str) -> None: ...

class ClientAPIConnection:
    FileArg: type[hutil.web.FileArg]
    server_url: str
    session_data: ClientSessionData | None
    def __init__(self, server_url: str, session_data: ClientSessionData | None) -> None: ...
    def __getattr__(self, name: str) -> "_ClientAPIConnectionFunction": ...

class APICallFailed(Exception): ...
class APIUnavailable(Exception): ...

class _ClientAPIConnectionFunction:
    server_url: str
    session_data: ClientSessionData | None
    name: str
    def __init__(self, server_url: str, session_data: ClientSessionData | None, name: str) -> None: ...
    # The arguments are sent as JSON, except FileArg keyword arguments, sent as files.
    def __call__(
        self, *args: JSONLike, **kwargs: JSONLike | hutil.web.FileArg
    ) -> hutil.json.DictAsObject | list[JSONValue] | str | int | float | bool | None: ...
    def kwargs_for_read_url(
        self, *args: JSONLike, **kwargs: JSONLike | hutil.web.FileArg
    ) -> _ReadUrlKwargs: ...
