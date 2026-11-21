import logging
from collections.abc import Iterable, Mapping, MutableMapping, Sequence
from typing import Any, TypeAlias, TypeVar, overload, type_check_only

import _pdg
import hou
from houtypes import ParmCallbackKwargs

_T = TypeVar("_T")
_EnvT = TypeVar("_EnvT", bound=Mapping[str, str])
_ParmValue: TypeAlias = int | float | str | Iterable[int | float | str]
# A pdgjson.File sent by a job via File.asTuple(): (path, tag, hash, owned).
_FileTuple: TypeAlias = tuple[str, str, int, bool]

class PyScheduler:
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None: ...
    @type_check_only
    def __getitem__(self, key: str) -> _pdg.Port: ...
    def __setitem__(self, key: str, value: _ParmValue) -> None: ...
    def initLogger(self, logger: logging.Logger, log_level: int | str) -> None: ...
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult: ...
    def onScheduleStatic(
        self,
        dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]],
        dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]],
        ready_items: Sequence[_pdg.WorkItem],
    ) -> None: ...
    @staticmethod
    def hasServiceSupport() -> bool: ...
    def startService(self, service: _pdg.Service) -> bool: ...
    def stopService(self, service: _pdg.Service) -> bool: ...
    def workItemSucceeded(
        self, workitem_id: int, index: int, cook_duration: float, jobid: str = ...
    ) -> None: ...
    def workItemCancelled(self, workitem_id: int, index: int, jobid: str = ...) -> None: ...
    def workItemFailed(self, workitem_id: int, index: int, jobid: str = ...) -> None: ...
    def workItemKeepalive(self, workitem_id: int, jobid: str = ...) -> None: ...
    def workItemStartCook(self, workitem_id: int, index: int, jobid: str = ...) -> None: ...
    def workItemSetCustomState(
        self, workitem_id: int, index: int, custom_state: str, jobid: str = ...
    ) -> None: ...
    def workItemSetCookPercent(
        self, workitem_id: int, index: int, cook_percent: float = ..., jobid: str = ...
    ) -> None: ...
    def workItemAppendLog(
        self, workitem_id: int, index: int, log_data: str, log_type: int, jobid: str = ...
    ) -> None: ...
    def workItemAddOutput(
        self,
        workitem_id: int,
        subindex: int,
        result: str | bytes,
        tag: str,
        checksum: int,
        jobid: str = ...,
        active_only: bool = ...,
    ) -> None: ...
    def workItemAddOutputs(
        self,
        workitem_id: int,
        subindex: int,
        results: Sequence[str | bytes],
        tags: str | Sequence[str],
        checksums: Sequence[int],
        jobid: str = ...,
        active_only: bool = ...,
    ) -> None: ...
    def workItemInvalidateCache(self, workitem_id: int, subindex: int, jobid: str = ...) -> None: ...
    def releaseJobSlots(self, workitem_id: int, jobid: str = ...) -> None: ...
    def acquireJobSlots(self, workitem_id: int, jobid: str = ...) -> None: ...
    def workItemSetStringAttribArray(
        self, workitem_id: int, subindex: int, attr_name: str, data: Sequence[str], jobid: str = ...
    ) -> None: ...
    def workItemSetIntAttribArray(
        self, workitem_id: int, subindex: int, attr_name: str, data: Sequence[int], jobid: str = ...
    ) -> None: ...
    def workItemSetFloatAttribArray(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        data: Sequence[float],
        jobid: str = ...,
    ) -> None: ...
    def workItemSetFileAttribArray(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        data: Iterable[_FileTuple],
        jobid: str = ...,
    ) -> None: ...
    def workItemSetDictAttribArray(
        self, workitem_id: int, subindex: int, attr_name: str, data: Iterable[str], jobid: str = ...
    ) -> None: ...
    def workItemSetStringAttrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    def workItemSetIntAttrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: int,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    def workItemSetFloatAttrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: float,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    def workItemSetFileAttrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: _FileTuple,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    def workItemSetDictAttrib(
        self,
        workitem_id: int,
        subindex: int,
        attr_name: str,
        attr_value: str,
        attr_index: int,
        jobid: str = ...,
    ) -> None: ...
    def workItemSetPyObjectAttrib(
        self, workitem_id: int, subindex: int, attr_name: str, attr_value: str, jobid: str = ...
    ) -> None: ...
    def onSharedServerStarted(self, args: _pdg._SharedServerInfo) -> None: ...
    def workItemWarning(self, workitem_id: int, message: str, jobid: str = ...) -> None: ...
    def workItemResultServerAddr(self) -> str: ...
    def setWorkItemResultServerAddr(self, addr: str) -> None: ...
    def getStatusURI(self, work_item: _pdg.WorkItem) -> str: ...
    def getLogURI(self, work_item: _pdg.WorkItem) -> str: ...
    # The base returns "", but subclasses (and submitGraphAsJob, which unpacks the result)
    # use (status URI, scheduler-specific job id).
    def submitAsJob(self, graph_file: str, node_path: str) -> str | tuple[str | None, Any]: ...
    def endSharedServer(self, sharedserver_name: str) -> bool: ...
    def setParameter(self, name: str, value: _ParmValue, str_expr: bool = ...) -> None: ...
    def addParameter(
        self, name: str, label: str, tag: str | Sequence[str], param_type: _pdg.dataType, size: int = ...
    ) -> _pdg.Port: ...
    def setParameters(
        self, parameters: Mapping[str, _ParmValue] | None = ..., **kwargs: _ParmValue
    ) -> None: ...
    def setValue(self, param_name: str, value: _ParmValue, index: int = ...) -> None: ...
    def setValues(
        self, values: Mapping[str, _ParmValue] | None = ..., **kwargs: _ParmValue
    ) -> None: ...
    def resolveBaseEnvironment(
        self,
        parmprefix: str,
        node: _pdg.Node | None,
        work_item: _pdg.WorkItem | None,
        remove_list: Iterable[str] = ...,
        affix: str = ...,
    ) -> dict[str, str]: ...
    def resolveEnvParams(
        self,
        parmprefix: str,
        work_item: _pdg.WorkItem | None,
        escapeforshell: bool = ...,
        affix: str = ...,
    ) -> tuple[dict[str, str], list[str]]: ...
    def resolvePathMapping(
        self, job_env: MutableMapping[str, str], b64encode: bool = ...
    ) -> str | None: ...
    def addCommonJobEnvVars(
        self, job_env: MutableMapping[str, str], work_item: _pdg.WorkItem | None, verbosity: int = ...
    ) -> None: ...
    def createJobDirsAndSerializeWorkItems(self, work_item: _pdg.WorkItem | None) -> None: ...
    def getLocalLogDir(self) -> str: ...
    def getLocalDataDir(self) -> str: ...
    def initHoudiniMaxThreads(
        self, work_item: _pdg.WorkItem | None, parm_prefix: str, default_val: _T
    ) -> int | _T: ...
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str: ...

def convertEnvMapToUTF8(job_env: _EnvT) -> _EnvT: ...
@overload
def evaluateParamOr(
    scheduler: PyScheduler,
    node: _pdg.Node | None,
    prefix: str,
    key: str,
    work_item: _pdg.WorkItem | None,
    default_value: str,
    toggle_prefix: str | None = ...,
) -> str: ...
@overload
def evaluateParamOr(
    scheduler: PyScheduler,
    node: _pdg.Node | None,
    prefix: str,
    key: str,
    work_item: _pdg.WorkItem | None,
    default_value: bool,
    toggle_prefix: str | None = ...,
) -> bool: ...
@overload
def evaluateParamOr(
    scheduler: PyScheduler,
    node: _pdg.Node | None,
    prefix: str,
    key: str,
    work_item: _pdg.WorkItem | None,
    default_value: int,
    toggle_prefix: str | None = ...,
) -> int: ...
@overload
def evaluateParamOr(
    scheduler: PyScheduler,
    node: _pdg.Node | None,
    prefix: str,
    key: str,
    work_item: _pdg.WorkItem | None,
    default_value: float,
    toggle_prefix: str | None = ...,
) -> float: ...
def evaluateParamOr(
    scheduler: PyScheduler,
    node: _pdg.Node | None,
    prefix: str,
    key: str,
    work_item: _pdg.WorkItem | None,
    default_value: str | float,
    toggle_prefix: str | None = ...,
) -> str | float: ...
def submitGraphAsJob(
    kwargs: ParmCallbackKwargs, topnode: hou.TopNode, sched_name: str, quiet: bool = ...
) -> str | tuple[str | None, Any]: ...
def saveToPython(
    node: hou.OpNode,
    classname: str = ...,
    description: str = ...,
    file_path: str = ...,
    tab_submenu: str = ...,
) -> None: ...
