import os
import xmlrpc.client
from collections.abc import Callable, Iterable, Sequence
from io import TextIOWrapper
from types import ModuleType, TracebackType
from typing import IO, Any, Literal, Never, Protocol, Self, TextIO, TypeAlias, TypeIs, TypeVar, overload

import pdg
from pdgjob import pdgjson
from pdgutils import PDGNetMQRelay

# What an XML-RPC ServerProxy (default flags) unmarshals a reply into.
_XmlRpcValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | xmlrpc.client.Binary
    | xmlrpc.client.DateTime
    | list["_XmlRpcValue"]
    | dict[str, "_XmlRpcValue"]
    | None
)

class _RpcProxy(Protocol):
    def call(self, fn_name: str, /, *args: object) -> Any: ...
    def commitMulti(self, name: str, /) -> object: ...

class _RpcDelegate(Protocol):
    def createRpcProxy(
        self, host: str, port: int, client_id: str, get_reply: bool, multi: bool, raise_exc: bool = ..., /
    ) -> _RpcProxy: ...

_ServerAddr: TypeAlias = str | _RpcProxy
_WorkItemId: TypeAlias = int | str | None
_FileTuple: TypeAlias = tuple[str, str, int, bool]
_T = TypeVar("_T")
_W = TypeVar("_W", bound=pdg.WorkItem | pdgjson.WorkItem | pdgjson.NativeWorkItem)

max_retries: int
rpc_timeout: int
rpc_backoff: int
rpc_delegate_from_env: str | None
batch_poll_delay: float
release_job_slots_on_poll: int
ignore_rpc_errors: int
max_rpc_errors: int
max_rpc_array_size: int
verbose: int
LogDefault: int
LogVerbose: int

class BaseService:
    client_name: str
    listener_name: str | None
    address: str
    port: int
    timeout: int
    log_file: str | None
    should_stop: bool
    client: PDGNetMQRelay[Self]
    def __init__(
        self,
        client_name: str,
        listener_name: str | None,
        address: str,
        port: int,
        timeout: int,
        log_file: str | None,
    ) -> None: ...
    def reset_service(self) -> None: ...
    def receive_job(self, job_info: pdgjson._ServiceJobInfo) -> pdgjson._ServiceResponse | pdgjson._ServiceStatus | dict[str, Never] | None: ...
    def stop_service(self) -> None: ...
    def is_alive(self) -> bool: ...
    def start(self) -> bool: ...
    def run(self) -> int: ...

class RedirectBuffer:
    def __init__(self, source: TextIO, tee: bool = ...) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def write(self, text: str) -> None: ...
    def flush(self) -> None: ...
    def buffer(self) -> str: ...

class StdOutReporter(TextIOWrapper):
    term: TextIO | None
    last: int
    format: str
    def __init__(self, log_format: str = ...) -> None: ...
    def discardAndClose(self) -> None: ...
    def reportAndClose(
        self, work_item: pdg.WorkItem | pdgjson.WorkItem | pdgjson.NativeWorkItem | None = ...
    ) -> None: ...
    @overload
    def collectFiles(self, include_tags: Literal[False]) -> list[str]: ...
    @overload
    def collectFiles(self, include_tags: Literal[True]) -> list[tuple[str, str]]: ...
    @overload
    def collectFiles(self, include_tags: bool) -> list[str] | list[tuple[str, str]]: ...
    def write(self, s: str) -> int: ...

class FileLock:
    file_name: str
    flags: int
    fd: int | None
    is_windows: bool
    def __init__(self, file_name: str, is_windows: bool) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None = ...,
        exc_value: BaseException | None = ...,
        traceback: TracebackType | None = ...,
    ) -> None: ...

disable_timestamps: int
disable_rpc: bool
result_server_addr: _ServerAddr | None
rpc_delegate: _RpcDelegate | ModuleType | None
rpc_num_errors: int
theJobid: str
thePathMaps: list[list[tuple[str, str, bool, int]]] | None
theSHFSPaths: list[str] | None
theDelocalizePaths: bool

def decode_str(s: str) -> str: ...
def is_str(s: object) -> TypeIs[str | bytes | bytearray]: ...
def setVerbosity(level: int) -> None: ...
def printlog(
    msg: str | bytes, verbosity: int = ..., timestamp: bool = ..., prefix: str = ..., end: str = ...
) -> None: ...
def setResultServerAddr(force_server_addr: _ServerAddr | None) -> None: ...
def getResultServerAddr() -> _ServerAddr | None: ...
def getSplitServerHostPort(server_addr: str) -> tuple[str, int]: ...

result_client_id: str | None

def setResultClientId(client_id: str | None) -> None: ...
def getResultClientId() -> str: ...
def setRpcDelegate(delegate_obj: str | _RpcDelegate | None) -> None: ...

class RpcError(Exception): ...

class XMLRpcProxy:
    def __init__(
        self, server_proxy: xmlrpc.client.ServerProxy | xmlrpc.client.MultiCall, raise_exc: bool
    ) -> None: ...
    def call(self, fn_name: str, *args: object, **kwargs: object) -> _XmlRpcValue: ...
    def commitMulti(self, name: str) -> None: ...

class XMLRpcDelegate:
    def createRpcProxy(
        self, host: str, port: int, client_id: str, get_reply: bool, multi: bool, raise_exc: bool = ...
    ) -> XMLRpcProxy: ...

@overload
def delocalizePath(local_path: str) -> str: ...
@overload
def delocalizePath(local_path: _T) -> _T: ...
def makeDirSafe(local_path: str) -> None: ...
def localizePath(deloc_path: str) -> str: ...
def getHostname(allow_localhost: bool = ...) -> tuple[str, str]: ...
def getIPAddress() -> str: ...
def verboseAnnounce() -> None: ...
def getItemIdFromEnv() -> int | str | None: ...
def waitUntilReady(
    workitem_id: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = ..., raise_exc: bool = ...
) -> None: ...
def checkReady(
    workitem_id: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = ..., raise_exc: bool = ...
) -> bool: ...
def appendSubItem(workitem_id: _WorkItemId, server_addr: _ServerAddr | None = ..., raise_exc: bool = ...) -> int: ...
def execBatchPoll(item_name: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = ...) -> None: ...
def getWorkItemJSON(
    workitem_id: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = ..., raise_exc: bool = ...
) -> str | None: ...
def workItemSuccess(
    workitem_id: _WorkItemId,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
) -> None: ...
def execBatchSuccess(
    item_name: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = ..., to_stdout: bool = ...
) -> None: ...
def workItemFailed(
    workitem_id: _WorkItemId, server_addr: _ServerAddr | None = ..., to_stdout: bool = ..., raise_exc: bool = ...
) -> None: ...
def execItemFailed(item_name: _WorkItemId, server_addr: _ServerAddr | None = ..., to_stdout: bool = ...) -> None: ...
def workItemStartCook(
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
) -> None: ...
def execStartCook(
    item_name: _WorkItemId = ..., subindex: int = ..., server_addr: _ServerAddr | None = ..., to_stdout: bool = ...
) -> None: ...
def workItemSetCustomState(
    custom_state: str,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
) -> None: ...
def workItemSetCookPercent(
    cook_percent: float,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
) -> None: ...
def workItemAppendLog(
    log_data: str,
    log_type: int = ...,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
) -> None: ...
def workItemCancelled(workitem_id: _WorkItemId, server_addr: _ServerAddr | None = ..., raise_exc: bool = ...) -> None: ...
def reportResultData(
    result_data: str | bytes | Sequence[str | bytes],
    workitem_id: _WorkItemId = ...,
    server_addr: _ServerAddr | None = ...,
    result_data_tag: str = ...,
    subindex: int = ...,
    and_success: bool = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
    duration: float = ...,
    hash_code: int = ...,
    batch_size: int = ...,
) -> None: ...
def addOutputFile(
    result_data: str | bytes | Sequence[str | bytes],
    workitem_id: _WorkItemId = ...,
    server_addr: _ServerAddr | None = ...,
    result_data_tag: str = ...,
    subindex: int = ...,
    and_success: bool = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
    duration: float = ...,
    hash_code: int = ...,
    batch_size: int = ...,
) -> None: ...
def addOutputFiles(
    output_file_array: Sequence[str | bytes],
    workitem_id: _WorkItemId = ...,
    server_addr: _ServerAddr | None = ...,
    output_file_tag: str | Sequence[str] = ...,
    subindex: int = ...,
    to_stdout: bool = ...,
    raise_exc: bool = ...,
    duration: float = ...,
    hash_codes: Sequence[int] = ...,
) -> None: ...
def writeAttribute(
    attr_name: str,
    attr_value: str | float | Sequence[str | float],
    item_name: str | None = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setStringAttribArray(
    attr_name: str,
    attr_value: Sequence[str],
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setIntAttribArray(
    attr_name: str,
    attr_value: Sequence[int],
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setFloatAttribArray(
    attr_name: str,
    attr_value: Sequence[float],
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setFileAttribArray(
    attr_name: str,
    attr_value: Sequence[_FileTuple],
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setDictAttribArray(
    attr_name: str,
    attr_value: Sequence[str],
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setPyObjectAttrib(
    attr_name: str,
    attr_value: str | bytes,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setStringAttrib(
    attr_name: str,
    attr_value: str,
    attr_index: int,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setIntAttrib(
    attr_name: str,
    attr_value: int,
    attr_index: int,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setFloatAttrib(
    attr_name: str,
    attr_value: float,
    attr_index: int,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setFileAttrib(
    attr_name: str,
    attr_value: _FileTuple,
    attr_index: int,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def setDictAttrib(
    attr_name: str,
    attr_value: str,
    attr_index: int,
    workitem_id: _WorkItemId = ...,
    subindex: int = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def invalidateCache(
    workitem_id: _WorkItemId = ..., subindex: int = ..., server_addr: _ServerAddr | None = ..., raise_exc: bool = ...
) -> None: ...
def reportServerStarted(
    servername: str,
    pid: int,
    host: str,
    port: int,
    proto_type: str,
    log_fname: str,
    workitem_id: _WorkItemId = ...,
    server_addr: _ServerAddr | None = ...,
    raise_exc: bool = ...,
) -> None: ...
def warning(
    message: str, workitem_id: _WorkItemId = ..., server_addr: _ServerAddr | None = ..., raise_exc: bool = ...
) -> None: ...
def keepalive(workitem_id: _WorkItemId = ..., server_addr: _ServerAddr | None = ..., raise_exc: bool = ...) -> None: ...
def sanitizeEnvironment(sanitize_list: Iterable[str]) -> os._Environ[str] | dict[str, str]: ...
def sanitizeFullEnvironment() -> os._Environ[str] | dict[str, str]: ...
def execCommand(
    work_item: _W,
    command: str,
    toolName: str | None = ...,
    sanitizeVars: Iterable[str] = ...,
    proc_input: bytes | None = ...,
    proc_output: int | IO[str] | IO[bytes] | None = ...,
    log_line_callback: Callable[[_W, str], object] | None = ...,
) -> str | None: ...

class PDGPingHelper:
    result_server: tuple[str, int]
    min_check_period: float
    next_check_time: float
    def __init__(self, host: str, port: int, min_check_period: float) -> None: ...
    def isReachable(self, raise_on_failure: bool = ...) -> bool: ...
    def ensureReachable(self) -> bool: ...

def main() -> None: ...
