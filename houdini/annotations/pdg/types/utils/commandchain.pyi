from collections.abc import Sequence
from typing import TypedDict

import _pdg
from houtypes import JSONValue
from pdg import PyProcessor

# What pdgjob.genericrpc.RPCProxy records for each call a job script makes, after the JSON round
# trip through the shared server: xmlrpc Binary arguments are base64 strings, the others as given.
class _BinaryCallArg(TypedDict):
    b64: str

class _CallArg(TypedDict):
    arg: JSONValue

class _CallRecord(TypedDict):
    fn: str
    args: list[_BinaryCallArg | _CallArg]

XMLRPC: int
RAW: int

class SendCommandRpcApi:
    @staticmethod
    def process_rpc(callobj: _CallRecord, work_item: _pdg.WorkItem) -> None: ...
    # `data` is the job's xmlrpc Binary result, base64-decoded by process_rpc.
    @staticmethod
    def result(
        work_item: _pdg.WorkItem, data: bytes, datatag: str, hashcode: int, jobid: str
    ) -> None: ...
    @staticmethod
    def success_and_result(
        work_item: _pdg.WorkItem,
        data: bytes,
        datatag: str,
        hashcode: int,
        duration: float,
        jobid: str,
    ) -> None: ...
    @staticmethod
    def failed(work_item: _pdg.WorkItem, jobid: str) -> None: ...
    @staticmethod
    def cancelled(work_item: _pdg.WorkItem, jobid: str) -> None: ...
    @staticmethod
    def warning(work_item: _pdg.WorkItem, message: str, jobid: str) -> None: ...
    @staticmethod
    def set_string_attrib_array(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[str],
        jobid: str,
    ) -> None: ...
    @staticmethod
    def set_int_attrib_array(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[int],
        jobid: str = ...,
    ) -> None: ...
    @staticmethod
    def set_float_attrib_array(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[float],
        jobid: str = ...,
    ) -> None: ...
    # Each file is pdgcmd's (path, tag, hash, own).
    @staticmethod
    def set_file_attrib_array(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: Sequence[tuple[str, str, int, bool]],
        jobid: str = ...,
    ) -> None: ...
    # The repr() of the object, which is stored as is.
    @staticmethod
    def set_pyobject_attrib(
        work_item: _pdg.WorkItem, subindex: int, attr_name: str, attr_value: str, jobid: str = ...
    ) -> None: ...
    @staticmethod
    def set_string_attrib(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    @staticmethod
    def set_int_attrib(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: int,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    @staticmethod
    def set_float_attrib(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: float,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    @staticmethod
    def set_file_attrib(
        work_item: _pdg.WorkItem,
        subindex: int,
        attr_name: str,
        attr_value: tuple[str, str, int, bool],
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...

class SendCommand(PyProcessor):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> None: ...
    def getCommandString(self, work_item: _pdg.WorkItem) -> str: ...
    def onCookTask(self, work_item: _pdg.WorkItem) -> _pdg.result: ...

class GenerativeSendCommand(PyProcessor):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> None: ...
    # The JSON string the server's exec_script returns; None for the raw protocol, or on error.
    def get_data(self, work_item: _pdg.WorkItem | None, sharedservername: str) -> str | None: ...

class CommandServerFeedback(PyProcessor):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def evaluateStartupCommandline(self, upstream_item: _pdg.WorkItem) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> _pdg.result: ...
    def onAddInternalDependencies(
        self,
        dependency_holder: _pdg.DependencyHolder,
        internal_items: _pdg.WorkItemList,
        is_static: bool,
    ) -> _pdg.result: ...

class PythonServer(CommandServerFeedback):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...

class HoudiniServer(PythonServer):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...

class MayaServer(CommandServerFeedback):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...

class ShotgunServer(CommandServerFeedback):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def evaluateStartupCommandline(self, upstream_item: _pdg.WorkItem) -> str: ...

class NukeServer(CommandServerFeedback):
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
