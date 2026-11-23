import threading
from collections.abc import Mapping, Sequence
from typing import Protocol, TypeAlias, TypedDict, Unpack
from xmlrpc.client import Binary
from xmlrpc.server import SimpleXMLRPCRequestHandler

from pdg.job.eventdispatch import _Event

class _EventDispatcher(Protocol):
    def execEvent(self, event: _Event) -> str | None: ...

class _XMLRPCServerOptions(TypedDict, total=False):
    requestHandler: type[SimpleXMLRPCRequestHandler]
    logRequests: bool
    allow_none: bool
    encoding: str | None
    bind_and_activate: bool
    use_builtin_types: bool

# A pdgjson.File sent over XML-RPC by File.asTuple(): (path, tag, hash, owned).
_FileTuple: TypeAlias = tuple[str, str, int, bool]

class CallbackServerAPI:
    callback_server: _EventDispatcher
    def __init__(self, callback_server: _EventDispatcher) -> None: ...
    def success(self, workitem_id: int, duration: float = ..., jobid: str = ...) -> str: ...
    def success_batch(
        self, workitem_id: int, subindex: int, duration: float = ..., jobid: str = ...
    ) -> str: ...
    def result(
        self,
        workitem_id: int,
        resultdata_binary: Binary,
        datatag: str,
        hashcode: int = ...,
        jobid: str = ...,
    ) -> None: ...
    def result_array(
        self,
        workitem_id: int,
        resultdata_binary: Sequence[Binary],
        datatag: str | Sequence[str],
        hashcodes: Sequence[int] = ...,
        jobid: str = ...,
    ) -> None: ...
    def result_batch(
        self,
        workitem_id: int,
        resultdata_binary: Binary,
        datatag: str,
        subindex: int,
        hashcode: int = ...,
        jobid: str = ...,
    ) -> None: ...
    def result_array_batch(
        self,
        workitem_id: int,
        subindex: int,
        resultdata_binary: Sequence[Binary],
        datatag: str | Sequence[str],
        hashcodes: Sequence[int] = ...,
        jobid: str = ...,
    ) -> None: ...
    def success_and_result(
        self,
        workitem_id: int,
        resultdata_binary: Binary,
        datatag: str,
        hashcode: int = ...,
        duration: float = ...,
        jobid: str = ...,
    ) -> str: ...
    def success_and_result_batch(
        self,
        workitem_id: int,
        resultdata_binary: Binary,
        datatag: str,
        subindex: int,
        hashcode: int = ...,
        duration: float = ...,
        jobid: str = ...,
    ) -> str: ...
    # pdgcmd.writeAttr sends the work item's name, not its id.
    def write_attr(
        self, workitem_id: str, attr_name: str, attr_value: Sequence[str | int | float], jobid: str = ...
    ) -> None: ...
    def set_string_attrib_array(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[str],
        jobid: str = ...,
    ) -> str | None: ...
    def set_int_attrib_array(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[int],
        jobid: str = ...,
    ) -> str | None: ...
    def set_float_attrib_array(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[float],
        jobid: str = ...,
    ) -> str | None: ...
    def set_file_attrib_array(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[_FileTuple],
        jobid: str = ...,
    ) -> str | None: ...
    def set_dict_attrib_array(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[str],
        jobid: str = ...,
    ) -> str | None: ...
    def set_pyobject_attrib(
        self, workitem_id: int, subindex: int, attr_name: str, attr_value: str, jobid: str = ...
    ) -> str | None: ...
    def set_string_attrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> str | None: ...
    def set_int_attrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: int,
        attr_index: int,
        jobid: str = ...,
    ) -> str | None: ...
    def set_float_attrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: float,
        attr_index: int,
        jobid: str = ...,
    ) -> str | None: ...
    def set_file_attrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: _FileTuple,
        attr_index: int,
        jobid: str = ...,
    ) -> str | None: ...
    def set_dict_attrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> str | None: ...
    def invalidate_cache(self, workitem_id: int, subindex: int, jobid: str = ...) -> None: ...
    def failed(self, workitem_id: int, jobid: str = ...) -> None: ...
    def cancelled(self, workitem_id: int, jobid: str = ...) -> None: ...
    def keepalive(self, workitem_id: int, jobid: str = ...) -> None: ...
    def check_ready_batch(self, workitem_id: int, subindex: int, jobid: str = ...) -> str | None: ...
    def add_sub_item_batch(self, workitem_id: int) -> str | None: ...
    def release_job_slots(self, workitem_id: int, jobid: str = ...) -> None: ...
    def acquire_job_slots(self, workitem_id: int, jobid: str = ...) -> None: ...
    def get_workitem_json(self, workitem_id: int, subindex: int, jobid: str = ...) -> str | None: ...
    def start_cook(self, workitem_id: int, jobid: str = ...) -> None: ...
    def start_cook_batch(self, workitem_id: int, subindex: int, jobid: str = ...) -> None: ...
    def set_custom_state(
        self, workitem_id: int, subindex: int, custom_state: str, jobid: str = ...
    ) -> None: ...
    def set_cook_percent(
        self, workitem_id: int, subindex: int, cook_percent: float, jobid: str = ...
    ) -> None: ...
    def append_log(
        self, workitem_id: int, subindex: int, log_data: str, log_type: int, jobid: str = ...
    ) -> None: ...
    def sharedserver_started(self, server_info: Mapping[str, str | int], jobid: str = ...) -> None: ...
    def warning(self, workitem_id: int, message: str, jobid: str = ...) -> None: ...

def getHostname() -> str: ...

class XMLRPCServer:
    request_queue_size: int
    allow_reuse_address: bool
    def __init__(self, addr: tuple[str, int], **kwargs: Unpack[_XMLRPCServerOptions]) -> None: ...

class CallbackServer:
    server_endpoint: tuple[str, int]
    custom_port_range: tuple[int, int] | None
    xmlserver: XMLRPCServer | None
    server_thread: threading.Thread | None
    eventdispatcher: _EventDispatcher
    def __init__(self, local_only: bool) -> None: ...
    def setEventDispatcher(self, dispatcherobj: _EventDispatcher) -> None: ...
    def isCallbackServerRunning(self) -> bool: ...
    def startCallbackServer(self) -> str: ...
    def stopCallbackServer(self) -> None: ...

class CallbackServerMixin:
    def __init__(self, local_only: bool) -> None: ...
    def startCallbackServer(self) -> str: ...
