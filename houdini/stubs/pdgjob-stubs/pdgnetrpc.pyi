# Houdini stubs generated from Houdini 22.0.466

import subprocess
from _pdgutils import PDGNMessage as PDGNMessage
from collections.abc import Callable as Callable, Mapping
from pdgjob.pdgcmd import RpcError as RpcError
from pdgjob.pdgnetjson import _RpcCall, _RpcJSON
from pdgnetjson import PDGNetRPCJsonWrapper as PDGNetRPCJsonWrapper
from queue import Queue
from typing import NoReturn, Protocol

from typing import TypeAlias
from typing import TypeAlias
_HTTPResponse: TypeAlias = bytes | str | BaseException
class _RecordCall(Protocol):
    def __call__(self, *args: object) -> None: ...

LogDefault: int
LogVerbose: int
is_py2: bool

def printlog(msg: str, verbosity: int = ...) -> None: ...
def rpcException() -> type[RpcError] | type[RuntimeError]: ...
def throwRpcException(msg: str) -> NoReturn: ...

use_http: bool
httpport: int | str
PDGNET_RPC_NOTIMEOUT: int
PDGNET_HTTP_SUCCESS: int
PDGNET_HTTP_GENERAL_ERROR: int
PICKLE_START_TOKEN: bytes

def doHTTPRequest(url: str, headers: Mapping[str, str | int], content: str, timeout_ms: float) -> tuple[int, _HTTPResponse]:
    """
    Send a HTTP request and return reply.
    Returns (status code, text) tuple.
    """

class PDGNetRPCHTTPMessage:
    response_queue: Queue[tuple[int, _HTTPResponse]] | None
    process: subprocess.Popen[bytes] | None
    complete: bool
    response_code: int
    response_msg: _HTTPResponse | None
    def __init__(self) -> None: ...
    def doRequest(self, url: str, port: int | str, get_reply: bool, reply_id: int, client_name: str, content: str, timeout_ms: float) -> None: ...
    def getError(self) -> int: ...
    def getErrorMessage(self, error_code: int) -> _HTTPResponse | None: ...
    def hasReplyAsyncReceived(self) -> bool: ...
    def completeReplyAsync(self) -> int: ...
    def readString(self) -> _HTTPResponse | None: ...

def sendMessageGetReplyAsync(url: str, port: int, client_name: str, json_str: str, timeout_ms: int) -> PDGNetRPCHTTPMessage | PDGNMessage: ...

class PDGNetRPCMessage:
    """ Single RPC call message handler for PDGnet """
    server_url: str
    server_port: int
    client_name: str
    get_reply: bool
    func_name: str | None
    timeout_ms: int
    jsonwrapper: PDGNetRPCJsonWrapper
    lasterror: int
    def __init__(self, server_url: str, server_port: int, client_name: str, get_reply: bool, func_name: str | None, timeout_ms: int, jsonwrapper: Callable[[], PDGNetRPCJsonWrapper] = ...) -> None: ...
    def __call__(self, *args: object) -> _RpcJSON: ...
    def doRPC(self, json_str: str) -> _RpcJSON: ...

max_retries: int
rpc_timeout: int
rpc_backoff: int
max_rpc_errors: int
rpc_num_errors: int

class PDGNetRPC:
    """ Single RPC message creator for PDGnet """
    server_url: str
    server_port: int
    client_name: str
    wait_reply: bool
    timeout_ms: float | None
    rpcmsgclass: type[PDGNetRPCMessage]
    def __init__(self, server_url: str, server_port: int, client_name: str, wait_reply: bool, timeout_ms: float | None = None, rpcmsgclass: type[PDGNetRPCMessage] = ...) -> None: ...
    def __getattr__(self, func_name: str) -> PDGNetRPCMessage:
        """
        Returns new rpcmsgclass object that should allow to invoke RPC over network.
        """

class PDGNetRPCMulti:
    """ Multi RPC message creator for PDGnet """
    server_url: str
    server_port: int
    client_name: str
    timeout_ms: float | None
    jsonwrapper: PDGNetRPCJsonWrapper
    jsonmethods: list[_RpcCall]
    rpcmsgclass: type[PDGNetRPCMessage]
    def __init__(self, server_url: str, server_port: int, client_name: str, timeout_ms: float | None = None, jsonwrapper: Callable[[], PDGNetRPCJsonWrapper] = ..., rpcmsgclass: type[PDGNetRPCMessage] = ...) -> None: ...
    def __call__(self) -> None: ...
    def __getattr__(self, func_name: str) -> _RecordCall:
        """
        Returns a function object that tracks RPC calls. When the object itself is
        called via (), the message is sent and the RPCs are invoked.
        """

class PDGNetRpcProxy:
    def __init__(self, host: str, port: int, client_id: str, get_reply: bool, multi: bool, raise_exc: bool = True) -> None: ...
    def call(self, fn_name: str, *args: object, **kwargs: object) -> _RpcJSON: ...
    def commitMulti(self, name: str) -> None: ...

def createRpcProxy(host: str, port: int, client_id: str, get_reply: bool, multi: bool, raise_exc: bool = True) -> PDGNetRpcProxy: ...
