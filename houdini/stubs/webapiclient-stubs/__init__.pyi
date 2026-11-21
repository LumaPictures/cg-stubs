import requests
import typing
from collections.abc import Generator, MutableMapping, Sequence
from houtypes import JSONLike, JSONValue
from types import TracebackType
from typing import Literal
from typing_extensions import Self

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_KwargValue: TypeAlias = 'JSONLike | bytearray | File'
_V = TypeVar('_V', bound=_KwargValue)
_Result: TypeAlias = 'JSONValue | ResponseFile | bytes'
class APIError(Exception):
    """Raised from the client if the server generated an error while calling
    into the API.
    """
    status_code: int
    def __init__(self, message: object, status_code: int) -> None: ...

class File:
    """Pass parameters of this type to API functions as a way of uploading
    large files.  Note that these File parameters must be specified by keyword
    arguments when calling the functions.
    """
    filename: str
    def __init__(self, filename: str) -> None: ...

class ResponseFile:
    """This object is returned from API functions that stream binary content.
    Call the API function from a `with` statement, and call the read method
    on the object to read the data in chunks.
    """
    response: requests.Response
    def __init__(self, response: requests.Response) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    @typing.overload
    def read(self, chunk_size: Literal[-1] = ...) -> bytes: ...
    @typing.overload
    def read(self, chunk_size: int = ...) -> bytes | Generator[bytes, None, None]: ...

def call(endpoint_url: str, function_name: str, args: Sequence[JSONLike], kwargs: MutableMapping[str, _V], session: requests.Session | None = None, compress_request: bool = False, compress_response: bool = False) -> _Result:
    """This function implements the core code to call an API function, handling
    incoming file parameters, streamed binary responses, and errors.

    You probably want to use the Service object instead of calling this
    function directly.
    """
def enable_debugging() -> None:
    """Print out the headers sent in requests."""

class Service:
    """This convenience object makes it more natural to call API functions
    and supports namespaced functions.
    """
    def __init__(self, url: str, compress_request: bool = False, compress_response: bool = False) -> None: ...
    def __getattr__(self, attr_name: str) -> APIFunction: ...

class APIFunction:
    def __init__(self, function_name: str, service: Service) -> None: ...
    def __getattr__(self, attr_name: str) -> APIFunction: ...
    def __call__(self, *args: JSONLike, **kwargs: _KwargValue) -> _Result: ...
