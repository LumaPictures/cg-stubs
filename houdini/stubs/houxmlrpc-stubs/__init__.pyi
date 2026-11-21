# Houdini stubs generated from Houdini 22.0.466

from xmlrpc.server import *
import http.client
import threading
import typing
import xmlrpc.client
from _typeshed import SizedBuffer
from collections.abc import Callable, Hashable, Sequence
from typing import Any, Generic

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_K = TypeVar('_K', bound=Hashable)
_V = TypeVar('_V')
_RemoteRef: TypeAlias = tuple[str, int]
_XMLRPCValue: TypeAlias = None | bool | int | float | str | xmlrpc.client.Binary | xmlrpc.client.DateTime | list['_XMLRPCValue'] | tuple['_XMLRPCValue', ...] | dict[str, '_XMLRPCValue']
_Unwrapped: TypeAlias = _T | None | bool | int | float | str | list['_Unwrapped[_T]'] | tuple['_Unwrapped[_T]', ...] | dict[str, '_Unwrapped[_T]']
_Wrapped: TypeAlias = str | int | float | bool | list['_Wrapped'] | dict['_Wrapped', '_Wrapped'] | _RemoteRef | None
_HostType: TypeAlias = tuple[str, dict[str, str]] | str
__all__ = ['HouXMLRPCServer', 'ServerProxy']

def wrapObj(o: object, wrapperFunc: Callable[[object], _RemoteRef]) -> _Wrapped:
    """Wraps an object o in preparation for XMLRPC marshalling.
    This will leave primitive types alone, and will replace all non-
    primitive types with remote object references.

    Primitive types are: strings, integers, floats, bools, lists/tuples,
                         and dictionaries.  Key and elements of lists,
                         tuples and dictionaries will be wrapped as well
                         as required.
    wrapperFunc is a function that will be called when a non-primitive
    type is encountered.  It is expected to return a remote object
    reference (a tuple of the form ('types.XXXXXX', object_id)).

    Returns o with non-primitive objects replaced by remote object
    references.
    """
def unwrapObj(o: _XMLRPCValue, unwrapperFunc: Callable[[tuple[str, int] | list[str | int]], _T]) -> _Unwrapped[_T]:
    '''Unwraps object o by replacing remote object references with
    "real" objects created by calling unwrapperFunc on remote object
    references.

    Returns o with remote object references replaced by objects.
    '''
def getSessionId(params: Sequence[_XMLRPCValue]) -> Hashable | None:
    """Checks if the first item of params is a session identifier, and
    returns it if it is.  Otherwise returns None.

    A session identifier is a 2-tuple: ('sessionid', sessionId)"""

class _LRUDict(Generic[_K, _V]):
    """A dictionary-like object that has LRU semantics (removes the
    least recently used object if more than maxObjs are in the
    dictionary)"""
    def __init__(self, maxObjs: int = 10) -> None: ...
    def __getitem__(self, key: _K) -> _V: ...
    @typing.overload
    def get(self, key: _K) -> _V | None: ...
    @typing.overload
    def get(self, key: _K, default: _T) -> _V | _T: ...
    def __setitem__(self, key: _K, value: _V) -> None: ...
    def __len__(self) -> int: ...
    def remove(self, key: _K) -> None: ...

class HouXMLRPCServer(SimpleXMLRPCServer):
    done: bool
    maxSessions: int
    maxSessionObjs: int
    sessions: _LRUDict[Hashable | None, _LRUDict[int, Any]]
    allow_reuse_address: bool
    def __init__(self, addr: tuple[str, int] = ('localhost', 8888), logRequests: bool = False, maxSessions: int = 10, maxSessionObjs: int = 1000) -> None: ...
    def delObj(self, objId: int, sessId: Hashable | None) -> bool: ...
    def __del__(self) -> None: ...
    def stop(self) -> bool:
        """Stops the XMLRPC Server"""
    def serve_forever(self) -> None: ...

class _ObjectProxy:
    def __init__(self, _srv: ServerProxy, _type: str, _id: int) -> None: ...
    def __del__(self) -> None: ...

class _MethodWrapper:
    def __init__(self, obj: _ObjectProxy, meth: str) -> None: ...
    def __call__(self, *args: _XMLRPCValue) -> _Unwrapped[_ObjectProxy]: ...

class PersistantTransport(xmlrpc.client.Transport):
    verbose: int
    def __init__(self) -> None: ...
    def make_connection(self, host: _HostType) -> http.client.HTTPConnection: ...
    def request(self, host: _HostType, handler: str, request_body: SizedBuffer, verbose: int = 0) -> tuple[_XMLRPCValue, ...]: ...

class ServerProxy(xmlrpc.client.ServerProxy):
    def __init__(self, *args: Any, **kw: Any) -> None: ...

def run(port: int = 8888) -> threading.Thread: ...
