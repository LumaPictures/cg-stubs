import os
import pdg
import typing
import xmlrpc.client
from collections.abc import Callable as Callable, Iterable, Sequence
from houtypes import JSONLike
from io import TextIOWrapper
from pdgjob import pdgjson as pdgjson
from pdgutils import PDGNetMQRelay
from types import ModuleType, TracebackType
from typing import Any, IO, Literal, Never, Protocol, Self, TextIO, TypeIs

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_XmlRpcValue: TypeAlias = bool | int | float | str | xmlrpc.client.Binary | xmlrpc.client.DateTime | list['_XmlRpcValue'] | dict[str, '_XmlRpcValue'] | None
_ServerAddr: TypeAlias = str | _RpcProxy
_WorkItemId: TypeAlias = int | str | None
_FileTuple: TypeAlias = tuple[str, str, int, bool]
_T = TypeVar('_T')
_W = TypeVar('_W', bound=pdg.WorkItem | pdgjson.WorkItem | pdgjson.NativeWorkItem)
class _RpcProxy(Protocol):
    def call(self, fn_name: str, /, *args: JSONLike | xmlrpc.client.Binary) -> Any: ...
    def commitMulti(self, name: str, /) -> object: ...

class _RpcDelegate(Protocol):
    def createRpcProxy(self, host: str, port: int, client_id: str, get_reply: bool, multi: bool, raise_exc: bool = ..., /) -> _RpcProxy: ...

LogDefault: int
LogVerbose: int
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

class BaseService:
    client_name: str
    listener_name: str | None
    address: str
    port: int
    timeout: int
    log_file: str | None
    should_stop: bool
    client: PDGNetMQRelay[Self]
    def __init__(self, client_name: str, listener_name: str | None, address: str, port: int, timeout: int, log_file: str | None) -> None: ...
    def reset_service(self) -> None: ...
    def receive_job(self, job_info: pdgjson._ServiceJobInfo) -> pdgjson._ServiceResponse | pdgjson._ServiceStatus | dict[str, Never] | None: ...
    def stop_service(self) -> None: ...
    def is_alive(self) -> bool: ...
    def start(self) -> bool: ...
    def run(self) -> int: ...

class RedirectBuffer:
    def __init__(self, source: TextIO, tee: bool = True) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def write(self, text: str) -> None: ...
    def flush(self) -> None: ...
    def buffer(self) -> str: ...

class StdOutReporter(TextIOWrapper):
    term: TextIO | None
    last: int
    format: str
    def __init__(self, log_format: str = '') -> None: ...
    def discardAndClose(self) -> None: ...
    def reportAndClose(self, work_item: pdg.WorkItem | pdgjson.WorkItem | pdgjson.NativeWorkItem | None = None) -> None: ...
    @typing.overload
    def collectFiles(self, include_tags: Literal[False]) -> list[str]: ...
    @typing.overload
    def collectFiles(self, include_tags: Literal[True]) -> list[tuple[str, str]]: ...
    @typing.overload
    def collectFiles(self, include_tags: bool) -> list[str] | list[tuple[str, str]]: ...
    def write(self, s: str) -> int: ...

class FileLock:
    file_name: str
    flags: int
    fd: int | None
    is_windows: bool
    def __init__(self, file_name: str, is_windows: bool) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...

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
def setVerbosity(level: int) -> None:
    """
    Sets the global verbosity level
    """
def printlog(msg: str | bytes, verbosity: int = ..., timestamp: bool = True, prefix: str = '', end: str = '\n') -> None:
    """
    Print a log message, verbosity > 0 means only print when PDG_VERBOSE
    is set to a higher value
    """
def setResultServerAddr(force_server_addr: _ServerAddr | None) -> None:
    """
    Set server address for result callback.
    """
def getResultServerAddr() -> _ServerAddr | None:
    """
    Return the result server address (or proxy object).
    """
def getSplitServerHostPort(server_addr: str) -> tuple[str, int]:
    """
    Returns 'url', 'port' from given 'url:port' format.
    """

result_client_id: str | None

def setResultClientId(client_id: str | None) -> None:
    """
    Set the client ID for sending RPCs.
    """
def getResultClientId() -> str:
    """
    Get the client ID for sending RPCs.
    """
def setRpcDelegate(delegate_obj: str | _RpcDelegate | None) -> None:
    """
    Set the RPc Delegate object, which is a factory for RpcProxy objects
    Passing None will re-query the environment, Passing a string will 
    try to import a module of the given name
    """

class RpcError(Exception):
    """
    Exception thrown when an RPC communication error occurs
    """

class XMLRpcProxy:
    """
    Implementation of an RPC Proxy Object that uses XMLRPC.
    Implementations must define the following methods:

    call(self, fn_name, *args, **kwargs) -> None
    commitMulti(self, name): -> object
    """
    def __init__(self, server_proxy: xmlrpc.client.ServerProxy | xmlrpc.client.MultiCall, raise_exc: bool) -> None: ...
    def call(self, fn_name: str, *args: object, **kwargs: object) -> _XmlRpcValue: ...
    def commitMulti(self, name: str) -> None: ...

class XMLRpcDelegate:
    """
    RPC Delegate for XMLRPC-based callbacks
    """
    def createRpcProxy(self, host: str, port: int, client_id: str, get_reply: bool, multi: bool, raise_exc: bool = True) -> XMLRpcProxy: ...

@typing.overload
def delocalizePath(local_path: str) -> str: ...
@typing.overload
def delocalizePath(local_path: _T) -> _T: ...
def makeDirSafe(local_path: str) -> None: ...
def localizePath(deloc_path: str) -> str:
    """
    Localize the given path.  This means replace any __PDG* tokens and
    expand env vars with the values in the current environment.  Also
    applies path mapping if PDG_PATHMAP is present.
    """
def getHostname(allow_localhost: bool = True) -> tuple[str, str]: ...
def getIPAddress() -> str: ...
def verboseAnnounce() -> None: ...
def getItemIdFromEnv() -> int | str | None:
    """
    Retrieve work_item.id from the job environment or None.
    """
def waitUntilReady(workitem_id: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Blocks until a batch sub item can begin cooking.

    subindex: the index of the batch item within it's batch.
    server_addr: the result server address, defaulting to
                 the value of $PDG_RESULT_SERVER
    raise_exc: whether or not RPC exceptions should be re-raised after logging
    """
def checkReady(workitem_id: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> bool:
    """
    Returns True if the work item is ready, False if it is not, and throws
    an exception if the work item is in an error state
    """
def appendSubItem(workitem_id: _WorkItemId, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> int:
    """
    Adds a sub item to the end of a running batch
    """
def execBatchPoll(item_name: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = None) -> None: ...
def getWorkItemJSON(workitem_id: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> str | None:
    """
    Returns a string containing the serialized json for the given
    work item.
    subindex: the index of the batch item within it's batch.
    server_addr: the result server address, defaulting to
                 the value of $PDG_RESULT_SERVER
    raise_exc: whether or not RPC exceptions should be re-raised after logging
    """
def workItemSuccess(workitem_id: _WorkItemId, subindex: int = -1, server_addr: _ServerAddr | None = None, to_stdout: bool = True, raise_exc: bool = True) -> None:
    """
    Reports that the given item has succeeded.

    subindex:    the index of the batch item within it's batch.
    server_addr: the result server address, defaulting to
                 the value of $PDG_RESULT_SERVER
    to_stdout:   also emit a status message to stdout
    raise_exc:   whether or not RPC exceptions should be re-raised after logging
    """
def execBatchSuccess(item_name: _WorkItemId, subindex: int, server_addr: _ServerAddr | None = None, to_stdout: bool = True) -> None: ...
def workItemFailed(workitem_id: _WorkItemId, server_addr: _ServerAddr | None = None, to_stdout: bool = True, raise_exc: bool = True) -> None:
    """
    Report when an item has failed.

    workitem_id: id of the associated work item
    server_addr: callback server in format 'IP:PORT', or emptry string to ignore
    to_stdout: also emit status messages to stdout
    raise_exc: whether or not RPC exceptions should be re-raised after logging
    
    Note: Batch subitems not supported.  Failure of a batch subitem will 
    automatically result in the failure of the batch item.
    """
def execItemFailed(item_name: _WorkItemId, server_addr: _ServerAddr | None = None, to_stdout: bool = True) -> None: ...
def workItemStartCook(workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, to_stdout: bool = True, raise_exc: bool = True) -> None:
    """
    Reports than a work item has started cooking.
    """
def execStartCook(item_name: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, to_stdout: bool = True) -> None: ...
def workItemSetCustomState(custom_state: str, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, to_stdout: bool = True, raise_exc: bool = True) -> None:
    """
    Sets a custom state string on the work item
    """
def workItemSetCookPercent(cook_percent: float, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, to_stdout: bool = True, raise_exc: bool = True) -> None:
    """
    Sets a cook percentage indicator on the work item
    """
def workItemAppendLog(log_data: str, log_type: int = 3, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, to_stdout: bool = True, raise_exc: bool = True) -> None:
    """
    Report log data back to PDG for the work item
    """
def workItemCancelled(workitem_id: _WorkItemId, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Report when a work item has been explicitly cancelled.

    workitem_id: id of the associated workitem
    server_addr: callback server in format 'IP:PORT', or emptry string to ignore
    raise_exc: whether or not RPC exceptions should be re-raised after logging
    
    Note: Batch subitems can not be cancelled, cancel the batch itself instead.
    """
def reportResultData(result_data: str | bytes | Sequence[str | bytes], workitem_id: _WorkItemId | None = None, server_addr: _ServerAddr | None = None, result_data_tag: str = '', subindex: int = -1, and_success: bool = False, to_stdout: bool = True, raise_exc: bool = True, duration: float = 0.0, hash_code: int = 0, batch_size: int = 50) -> None:
    """
    Deprecated in favor of addOutputFile
    """
def addOutputFile(result_data: str | bytes | Sequence[str | bytes], workitem_id: _WorkItemId | None = None, server_addr: _ServerAddr | None = None, result_data_tag: str = '', subindex: int = -1, and_success: bool = False, to_stdout: bool = True, raise_exc: bool = True, duration: float = 0.0, hash_code: int = 0, batch_size: int = 50) -> None:
    """
    Reports an output file to PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    result_data:    output file path - treated as bytes if result_data_tag is passed
    result_data_tag: tag to categorize result.  Eg: 'file/geo'
                    Default is empty which means attempt to categorize using file extension.
    subindex:       The batch subindex if this is a batch item.
    and_success:    If True, report success in addition to result_data
    to_stdout:      also emit status messages to stdout
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    duration:       [Unused] cook time of the item in seconds, only report with and_success
    hash_code:      int that can be used to check if this file has changed, usually this is the modify-time of the file.
    batch_size:     Maximum number of results to send per multicall invoke
    """
def addOutputFiles(output_file_array: Sequence[str | bytes], workitem_id: _WorkItemId | None = None, server_addr: _ServerAddr | None = None, output_file_tag: str | Sequence[str] = '', subindex: int = -1, to_stdout: bool = True, raise_exc: bool = True, duration: float = 0.0, hash_codes: Sequence[int] = ...) -> None:
    """
    Reports an output file to PDG via the callback server.

    workitem_id:        id of the associated workitem (default $PDG_ITEM_ID)
    server_addr:        callback server in format 'IP:PORT'
                        (default $PDG_RESULT_SERVER)
                        if there is no env var it will default to stdout
                        reporting only.
    output_file_array:  output file paths
    output_file_tag:    array of tag(s) to categorize files,  Eg: 'file/geo'
                        Default is empty which means attempt to categorize using
                        file extension.
    subindex:           The batch subindex if this is a batch item.
    to_stdout:          also emit status messages to stdout
    raise_exc:          whether or not RPC exceptions should be re-raised after
                        logging
    hash_codes:         int array that correpsonds to the output files
                        used to check if this file has changed, usually this is
                        the modify-time of the file.
    """
def writeAttribute(attr_name: str, attr_value: str | float | Sequence[str | float], item_name: str | None = None, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    [Deprecated]
    Writes attribute data back into a work item in PDG via the callback server.

    item_name:      name of the associated workitem (default $PDG_ITEM_NAME)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     single value or array of string/float/int data
    """
def setStringAttribArray(attr_name: str, attr_value: Sequence[str], workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     array of strings
    """
def setIntAttribArray(attr_name: str, attr_value: Sequence[int], workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     array of integers
    """
def setFloatAttribArray(attr_name: str, attr_value: Sequence[float], workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     array of floats
    """
def setFileAttribArray(attr_name: str, attr_value: Sequence[_FileTuple], workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     array of pdgjson.File objects
    """
def setDictAttribArray(attr_name: str, attr_value: Sequence[str], workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     array of dictionary string representations
    """
def setPyObjectAttrib(attr_name: str, attr_value: str | bytes, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     string that is a valid repr() of a python object
    """
def setStringAttrib(attr_name: str, attr_value: str, attr_index: int, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     string value
    """
def setIntAttrib(attr_name: str, attr_value: int, attr_index: int, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     integer value
    """
def setFloatAttrib(attr_name: str, attr_value: float, attr_index: int, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     float value
    """
def setFileAttrib(attr_name: str, attr_value: _FileTuple, attr_index: int, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     pdg.File value
    """
def setDictAttrib(attr_name: str, attr_value: str, attr_index: int, workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Writes attribute data back into a work item in PDG via the callback server.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    attr_name:      name of the attribute
    attr_value:     dictionary string representation
    """
def invalidateCache(workitem_id: _WorkItemId | None = None, subindex: int = -1, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Requests that the cache of the work item be invalidated by PDG. This forces
    downstream tasks to cook. The same effect can be achieved by adding an
    output file to the work item, however this method can be used to invalidate
    caches without explicitly adding a file.

    workitem_id:    id of the associated work item (default $PDG_ITEM_ID)
    subindex:       batch subindex of item (-1 indicates a non-batch item)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
                    if there is no env var it will default to stdout reporting only.
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    """
def reportServerStarted(servername: str, pid: int, host: str, port: int, proto_type: str, log_fname: str, workitem_id: _WorkItemId | None = None, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Reports that a shared server has been started.

    workitem_id:    id of the associated workitem (default $PDG_ITEM_ID)
    server_addr:    callback server in format 'IP:PORT' (default $PDG_RESULT_SERVER)
    raise_exc:      whether or not RPC exceptions should be re-raised after logging
    """
def warning(message: str, workitem_id: _WorkItemId | None = None, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None: ...
def keepalive(workitem_id: _WorkItemId | None = None, server_addr: _ServerAddr | None = None, raise_exc: bool = True) -> None:
    """
    Called by the job wrapper script when the scheduler requires heartbeat signals.
    """
def sanitizeEnvironment(sanitize_list: Iterable[str]) -> os._Environ[str] | dict[str, str]: ...
def sanitizeFullEnvironment() -> os._Environ[str] | dict[str, str]: ...
def execCommand(work_item: _W, command: str, toolName: str | None = None, sanitizeVars: Iterable[str] = ..., proc_input: bytes | None = None, proc_output: int | IO[str] | IO[bytes] | None = ..., log_line_callback: Callable[[_W, str], object] | None = None) -> str | None:
    """
    Executes a command.
    log_line_callback: Callable[[WorkItem, str], None] Function that runs on
        each line of stdout produced by the command.
    """

class PDGPingHelper:
    """
    Checks if PDG Result Server is reachable at a fixed period.
    """
    result_server: tuple[str, int]
    min_check_period: float
    next_check_time: float
    def __init__(self, host: str, port: int, min_check_period: float) -> None: ...
    def isReachable(self, raise_on_failure: bool = False) -> bool:
        """
        Returns True if PDG is reachable or if the minimum check period has not
        elapsed.
        """
    def ensureReachable(self) -> bool: ...

def main() -> None: ...
