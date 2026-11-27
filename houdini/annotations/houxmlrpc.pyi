import http.client
import ssl
import threading
import xmlrpc.client
from _typeshed import SizedBuffer
from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Any, Generic, TypeAlias, TypeVar, overload

from typing_extensions import Required, TypedDict, Unpack

_T = TypeVar("_T")
_K = TypeVar("_K", bound=Hashable)
_V = TypeVar("_V")
_RemoteRef: TypeAlias = tuple[str, int]
# What XML-RPC unmarshals (with allow_none and without use_builtin_types).
_XMLRPCValue: TypeAlias = (
    None
    | bool
    | int
    | float
    | str
    | xmlrpc.client.Binary
    | xmlrpc.client.DateTime
    | list["_XMLRPCValue"]
    | tuple["_XMLRPCValue", ...]
    | dict[str, "_XMLRPCValue"]
)
# An XML-RPC value with its remote object references replaced by what the unwrapper gives.
_Unwrapped: TypeAlias = (
    _T
    | None
    | bool
    | int
    | float
    | str
    | list["_Unwrapped[_T]"]
    | tuple["_Unwrapped[_T]", ...]
    | dict[str, "_Unwrapped[_T]"]
)
_Wrapped: TypeAlias = str | int | float | bool | list["_Wrapped"] | dict["_Wrapped", "_Wrapped"] | _RemoteRef | None
_HostType: TypeAlias = tuple[str, dict[str, str]] | str

def wrapObj(o: object, wrapperFunc: Callable[[object], _RemoteRef]) -> _Wrapped: ...
def unwrapObj(
    o: _XMLRPCValue, unwrapperFunc: Callable[[tuple[str, int] | list[str | int]], _T]
) -> _Unwrapped[_T]: ...
def getSessionId(params: Sequence[_XMLRPCValue]) -> Hashable | None: ...

class _LRUDict(Generic[_K, _V]):
    def __init__(self, maxObjs: int = ...) -> None: ...
    def __getitem__(self, key: _K) -> _V: ...
    @overload
    def get(self, key: _K) -> _V | None: ...
    @overload
    def get(self, key: _K, default: _T) -> _V | _T: ...
    def get(self, key: _K, default: _T | None = ...) -> _V | _T | None: ...
    def __setitem__(self, key: _K, value: _V) -> None: ...
    def __len__(self) -> int: ...
    def remove(self, key: _K) -> None: ...

class HouXMLRPCServer:
    allow_reuse_address: bool
    done: bool
    maxSessions: int
    maxSessionObjs: int
    # The objects each session hands out by reference: whatever hou returns that XML-RPC
    # cannot marshal.
    sessions: _LRUDict[Hashable | None, _LRUDict[int, Any]]
    def __init__(self, addr: tuple[str, int] = ..., logRequests: bool = ..., maxSessions: int = ..., maxSessionObjs: int = ...) -> None: ...
    def delObj(self, objId: int, sessId: Hashable | None) -> bool: ...
    def __del__(self) -> None: ...
    def stop(self) -> bool: ...
    def serve_forever(self) -> None: ...

class _ObjectProxy:
    def __init__(self, _srv: "ServerProxy", _type: str, _id: int) -> None: ...
    def __del__(self) -> None: ...

class _MethodWrapper:
    def __init__(self, obj: _ObjectProxy, meth: str) -> None: ...
    def __call__(self, *args: _XMLRPCValue) -> _Unwrapped[_ObjectProxy]: ...

class PersistantTransport:
    verbose: int
    def __init__(self) -> None: ...
    def make_connection(self, host: _HostType) -> http.client.HTTPConnection: ...
    def request(self, host: _HostType, handler: str, request_body: SizedBuffer, verbose: int = ...) -> tuple[_XMLRPCValue, ...]: ...

# What ServerProxy forwards to xmlrpc.client.ServerProxy; allow_none is always forced on.
class _ServerProxyKwargs(TypedDict, total=False):
    transport: xmlrpc.client.Transport | None
    encoding: str | None
    verbose: bool
    use_datetime: bool
    use_builtin_types: bool
    headers: Iterable[tuple[str, str]]
    context: ssl.SSLContext | None

class _ServerProxyUriKwargs(_ServerProxyKwargs, total=False):
    uri: Required[str]

class ServerProxy:
    @overload
    def __init__(self, *args: Unpack[tuple[str]], **kw: Unpack[_ServerProxyKwargs]) -> None: ...
    @overload
    def __init__(self, *args: Unpack[tuple[()]], **kw: Unpack[_ServerProxyUriKwargs]) -> None: ...

def run(port: int = ...) -> threading.Thread: ...
