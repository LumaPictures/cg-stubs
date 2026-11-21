import itertools
import queue
import socket
import socketserver
import xmlrpc.client
from collections.abc import Iterable, Mapping, Sequence
from typing import NamedTuple, Protocol, TypeAlias
from xmlrpc.server import SimpleXMLRPCServer

from houtypes import JSONLike

class _Event(Protocol):
    def _asdict(self) -> dict[str, JSONLike | bytes | Sequence[bytes] | xmlrpc.client.Binary]: ...

class _Spooler(Protocol):
    def spool_tractor_task(self, task_tcl: str, /) -> object: ...
    def shutdown(self) -> object: ...

_WorkItemId: TypeAlias = int | str
_FileData: TypeAlias = Sequence[str | int | bool]

class SuccessEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    cook_duration: float
    jobid: str

class CanceledEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    jobid: str

class FailedEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    jobid: str

class KeepaliveEvent(NamedTuple):
    workitem_id: _WorkItemId
    jobid: str

class StartCookEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    jobid: str

class SharedServerStartedEvent(NamedTuple):
    info: Mapping[str, str | int]
    jobid: str

class IsWorkItemReadyEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int

class AddSubItemBatchEvent(NamedTuple):
    workitem_id: _WorkItemId

class ReleaseJobSlotsEvent(NamedTuple):
    workitem_id: _WorkItemId
    jobid: str

class AcquireJobSlotsEvent(NamedTuple):
    workitem_id: _WorkItemId
    jobid: str

class GetWorkItemJSONEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int

class ResultDataEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    result_data: bytes
    result_data_tag: str
    hash_code: int
    jobid: str

class ResultDataArrayEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    result_data_array: list[bytes]
    result_data_tag: Sequence[str]
    hash_code_array: Sequence[int]
    jobid: str

class WriteAttrEvent(NamedTuple):
    workitem_id: _WorkItemId
    attr_name: str
    value: Sequence[str] | Sequence[int] | Sequence[float]
    jobid: str

class SetStringAttribArrayEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    value: Sequence[str]
    jobid: str

class SetIntAttribArrayEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    value: Sequence[int]
    jobid: str

class SetFloatAttribArrayEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    value: Sequence[float]
    jobid: str

class SetFileAttribArrayEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    value: Sequence[_FileData]
    jobid: str

class SetDictAttribArrayEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    value: Sequence[str]
    jobid: str

# CallbackServerAPI passes the attribute value and index in the opposite order to the fields,
# so `attr_index` holds the value and `value` the index.
class SetStringAttribEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    attr_index: str
    value: int
    jobid: str

class SetIntAttribEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    attr_index: int
    value: int
    jobid: str

class SetFloatAttribEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    attr_index: float
    value: int
    jobid: str

class SetFileAttribEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    attr_index: _FileData
    value: int
    jobid: str

class SetDictAttribEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    attr_index: str
    value: int
    jobid: str

class SetPyObjectAttribEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    attr_name: str
    value: str | xmlrpc.client.Binary
    jobid: str

class SetCustomStateEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    custom_state: str
    jobid: str

class SetCookPercentEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    cook_percent: float
    jobid: str

class AppendLogEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    log_data: str
    log_type: int
    jobid: str

class InvalidateCacheEvent(NamedTuple):
    workitem_id: _WorkItemId
    index: int
    jobid: str

class WarningEvent(NamedTuple):
    workitem_id: _WorkItemId
    message: str
    jobid: str

blocking_events: set[
    type[
        IsWorkItemReadyEvent
        | AddSubItemBatchEvent
        | ResultDataEvent
        | ResultDataArrayEvent
        | SuccessEvent
        | ReleaseJobSlotsEvent
        | WriteAttrEvent
        | GetWorkItemJSONEvent
        | SetStringAttribArrayEvent
        | SetIntAttribArrayEvent
        | SetFloatAttribArrayEvent
        | SetFileAttribArrayEvent
        | SetDictAttribArrayEvent
        | SetStringAttribEvent
        | SetIntAttribEvent
        | SetFloatAttribEvent
        | SetFileAttribEvent
        | SetDictAttribEvent
        | SetPyObjectAttribEvent
        | StartCookEvent
    ]
]

theFirstConnectionTimeout: float
theFailOnLostConnection: int
theVerbosity: int

def dumpEvent(eventtuple: _Event) -> str: ...

class _Stats:
    inst: "_Stats | None"
    start: float
    latencies: queue.Queue[float]
    message_count: int
    def __init__(self, report_period: float = ...) -> None: ...

class TractorSpooler:
    def __init__(self) -> None: ...
    def shutdown(self) -> None: ...
    def spool_tractor_task(self, task_tcl: str | bytes) -> None: ...

def createTractorSpooler() -> _Spooler: ...
def printflushed(s: object, no_ts: bool = ...) -> None: ...

class CallbackServerAPI:
    callback_server: "XMLRPCServer"
    def __init__(self, callback_server: "XMLRPCServer") -> None: ...
    def shutdown(self) -> str: ...
    def success(self, workitem_id: _WorkItemId, duration: float = ..., jobid: str = ...) -> str: ...
    def success_batch(
        self, workitem_id: _WorkItemId, subindex: int, duration: float = ..., jobid: str = ...
    ) -> str: ...
    def result(
        self,
        workitem_id: _WorkItemId,
        resultdata_binary: xmlrpc.client.Binary,
        datatag: str,
        hashcode: int = ...,
        jobid: str = ...,
    ) -> str: ...
    def result_array(
        self,
        workitem_id: _WorkItemId,
        resultdata_binary: Iterable[xmlrpc.client.Binary],
        datatag: Sequence[str],
        hashcodes: Sequence[int] = ...,
        jobid: str = ...,
    ) -> str: ...
    def result_batch(
        self,
        workitem_id: _WorkItemId,
        resultdata_binary: xmlrpc.client.Binary,
        datatag: str,
        subindex: int,
        hashcode: int = ...,
        jobid: str = ...,
    ) -> None: ...
    def result_array_batch(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        resultdata_binary: Iterable[xmlrpc.client.Binary],
        datatag: Sequence[str],
        hashcodes: Sequence[int] = ...,
        jobid: str = ...,
    ) -> None: ...
    def success_and_result(
        self,
        workitem_id: _WorkItemId,
        resultdata_binary: xmlrpc.client.Binary,
        datatag: str,
        hashcode: int = ...,
        duration: float = ...,
        jobid: str = ...,
    ) -> str: ...
    def success_and_result_batch(
        self,
        workitem_id: _WorkItemId,
        resultdata_binary: xmlrpc.client.Binary,
        datatag: str,
        subindex: int,
        hashcode: int = ...,
        duration: float = ...,
        jobid: str = ...,
    ) -> str: ...
    def write_attr(
        self,
        workitem_id: _WorkItemId,
        attr_name: str,
        attr_value: Sequence[str] | Sequence[int] | Sequence[float],
        jobid: str = ...,
    ) -> str: ...
    def set_string_attrib_array(
        self, workitem_id: _WorkItemId, subindex: int, attr_name: str, attr_value: Sequence[str], jobid: str = ...
    ) -> str: ...
    def set_int_attrib_array(
        self, workitem_id: _WorkItemId, subindex: int, attr_name: str, attr_value: Sequence[int], jobid: str = ...
    ) -> str: ...
    def set_float_attrib_array(
        self, workitem_id: _WorkItemId, subindex: int, attr_name: str, attr_value: Sequence[float], jobid: str = ...
    ) -> str: ...
    def set_file_attrib_array(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[_FileData],
        jobid: str = ...,
    ) -> str: ...
    def set_dict_attrib_array(
        self, workitem_id: _WorkItemId, subindex: int, attr_name: str, attr_value: Sequence[str], jobid: str = ...
    ) -> str: ...
    def set_pyobject_attrib(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: str | xmlrpc.client.Binary,
        jobid: str = ...,
    ) -> str: ...
    def set_string_attrib(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> str: ...
    def set_int_attrib(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: int,
        attr_index: int,
        jobid: str = ...,
    ) -> str: ...
    def set_float_attrib(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: float,
        attr_index: int,
        jobid: str = ...,
    ) -> str: ...
    def set_file_attrib(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: _FileData,
        attr_index: int,
        jobid: str = ...,
    ) -> str: ...
    def set_dict_attrib(
        self,
        workitem_id: _WorkItemId,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> str: ...
    def invalidate_cache(self, workitem_id: _WorkItemId, subindex: int, jobid: str = ...) -> None: ...
    def failed(self, workitem_id: _WorkItemId, jobid: str = ...) -> None: ...
    def cancelled(self, workitem_id: _WorkItemId, jobid: str = ...) -> None: ...
    def keepalive(self, workitem_id: _WorkItemId, jobid: str = ...) -> None: ...
    def check_ready_batch(self, workitem_id: _WorkItemId, subindex: int, jobid: str = ...) -> str: ...
    def add_sub_item_batch(self, workitem_id: _WorkItemId, jobid: str = ...) -> str: ...
    def release_job_slots(self, workitem_id: _WorkItemId, jobid: str = ...) -> None: ...
    def acquire_job_slots(self, workitem_id: _WorkItemId, jobid: str = ...) -> None: ...
    def get_workitem_json(self, workitem_id: _WorkItemId, subindex: int, jobid: str = ...) -> str: ...
    def start_cook(self, workitem_id: _WorkItemId, jobid: str = ...) -> str: ...
    def start_cook_batch(self, workitem_id: _WorkItemId, subindex: int, jobid: str = ...) -> str: ...
    def set_custom_state(self, workitem_id: _WorkItemId, subindex: int, custom_state: str, jobid: str = ...) -> None: ...
    def set_cook_percent(
        self, workitem_id: _WorkItemId, subindex: int, cook_percent: float, jobid: str = ...
    ) -> None: ...
    def append_log(
        self, workitem_id: _WorkItemId, subindex: int, logdata: str, logtype: int, jobid: str = ...
    ) -> None: ...
    def sharedserver_started(self, server_info: Mapping[str, str | int], jobid: str = ...) -> None: ...
    def warning(self, workitem_id: _WorkItemId, message: str, jobid: str = ...) -> None: ...
    def spool_tractor_task(self, task_tcl: str) -> str: ...

class RelayProtocol:
    @staticmethod
    def send_message(s: socket.socket, msg: str) -> None: ...
    @staticmethod
    def recv_message(s: socket.socket) -> str: ...
    @staticmethod
    def sendACK(s: socket.socket) -> None: ...
    @staticmethod
    def recvACK(s: socket.socket) -> None: ...

class XMLRPCServer(SimpleXMLRPCServer):
    request_queue_size: int
    allow_reuse_address: bool
    finished: bool
    id_counter: itertools.count[int]
    task_statements: queue.Queue[_Event]
    task_questions: queue.Queue[tuple[int, _Event]]
    host_answers: queue.Queue[tuple[int, str]]
    relay_server: "RelayTCPServer"
    def serve_forever(self) -> None: ...
    def shutdown(self) -> int: ...
    def putTaskStatement(self, event: _Event) -> None: ...
    def askQuestion(self, event: _Event) -> str: ...

class RelayHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None: ...

def get_hostname() -> str: ...
def get_ip_experimental() -> str: ...

class RelayTCPServer(socketserver.TCPServer):
    allow_reuse_address: bool
    timedout: bool
    finished: bool
    exit_code: int
    task_statements: queue.Queue[_Event]
    task_questions: queue.Queue[tuple[int, _Event]]
    host_answers: queue.Queue[tuple[int, str]]
    def handle_timeout(self) -> None: ...

def test_port(endpoint: tuple[str, int]) -> bool: ...
def main() -> None: ...
