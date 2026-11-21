from collections.abc import Generator, MutableMapping, Sequence
from types import TracebackType
from typing import Literal, TypeAlias, TypeVar, overload

import requests
from houtypes import JSONLike, JSONValue
from typing_extensions import Self

# Keyword arguments that are File or bytearray are uploaded as files; the rest are sent as JSON.
_KwargValue: TypeAlias = "JSONLike | bytearray | File"
_V = TypeVar("_V", bound=_KwargValue)
# The JSON-decoded result, a streamed binary result, or the raw body if it is not JSON.
_Result: TypeAlias = "JSONValue | ResponseFile | bytes"

class APIError(Exception):
    status_code: int
    def __init__(self, message: object, status_code: int) -> None: ...

class File:
    filename: str
    def __init__(self, filename: str) -> None: ...

class ResponseFile:
    response: requests.Response
    def __init__(self, response: requests.Response) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    @overload
    def read(self, chunk_size: Literal[-1] = ...) -> bytes: ...
    @overload
    def read(self, chunk_size: int = ...) -> bytes | Generator[bytes, None, None]: ...

def call(
    endpoint_url: str,
    function_name: str,
    args: Sequence[JSONLike],
    kwargs: MutableMapping[str, _V],
    session: requests.Session | None = ...,
    compress_request: bool = ...,
    compress_response: bool = ...,
) -> _Result: ...
def enable_debugging() -> None: ...

class Service:
    def __init__(self, url: str, compress_request: bool = ..., compress_response: bool = ...) -> None: ...
    def __getattr__(self, attr_name: str) -> "APIFunction": ...

class APIFunction:
    def __init__(self, function_name: str, service: Service) -> None: ...
    def __getattr__(self, attr_name: str) -> "APIFunction": ...
    def __call__(self, *args: JSONLike, **kwargs: _KwargValue) -> _Result: ...
