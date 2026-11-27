import re
import threading
import xmlrpc.client
from collections import deque
from collections.abc import Mapping, MutableMapping, Sequence
from collections.abc import Set as AbstractSet
from typing import TypedDict

import _pdg
from pdg.job.callbackserver import CallbackServerAPI
from pdg.job.eventdispatch import _Event
from pdg.utils.mq import MQInfo
from pdgutils import PDGNetMQRelay

# A job's command for each platform HQueue runs it on.
class _PlatformCommands(TypedDict):
    linux: str
    macosx: str
    windows: str

# A client condition of an HQueue job spec.
class _Condition(TypedDict):
    type: str
    name: str
    op: str
    value: str

# The HQueue job spec that the scheduler submits to the server's newjob().
class _JobSpec(TypedDict, total=False):
    name: str
    command: str | _PlatformCommands
    onCancel: _PlatformCommands
    onError: _PlatformCommands
    cpus: int
    priority: int
    parentIds: list[int]
    children: list["_JobSpec"]
    submittedBy: str
    description: str
    tags: list[str]
    conditions: list[_Condition]
    inheritConditions: bool
    host: str
    maxTime: int
    triesLeft: int
    environment: dict[str, str]
    resources: dict[str, int]
    combineOutput: bool

def displayError(msg: str, exception: BaseException | None = ...) -> None: ...
def displayMessage(msg: str) -> None: ...
def doesHQServerExists(hq_server: str) -> bool: ...
def _connectToHQServer(hq_server: str) -> xmlrpc.client.ServerProxy | None: ...
def getHQRoot(hq_server: str) -> str | None: ...

class HQueueScheduler:
    hqserver: xmlrpc.client.ServerProxy | None
    rpc_lock: threading.Lock
    # The root job's ID; -1 while it has not been created, 0 when creating it failed.
    root_id: int
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    # Node or service client name -> its container job's ID.
    node_id: dict[str, int]
    # Work item ID -> its job's ID.
    workitem_ids: dict[int, int]
    waiting_ids: set[int]
    running_ids: set[int]
    # Work item ID -> the retries its job has left.
    retries: dict[int, int]
    tickPeriod: None
    maxItems: None
    var_capture_re: re.Pattern[str]
    custom_port_range: None
    ready_deque: deque[tuple[_pdg.WorkItem, _JobSpec]]
    running_services: list[_pdg.Service]
    file_env: dict[str, str]
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def startService(self, service: _pdg.Service) -> bool: ...
    def stopService(self, service: _pdg.Service, cancel: bool) -> bool: ...
    def startServiceClient(
        self, service: _pdg.Service, client: _pdg.ServiceClientInfo
    ) -> bool: ...
    def stopServiceClient(
        self, service: _pdg.Service, client: _pdg.ServiceClientInfo
    ) -> bool: ...
    @staticmethod
    def getMQServiceName(mqusage: int) -> str | None: ...
    def _localsharedroot(self) -> str | None: ...
    def applicationBin(self, name: str, work_item: _pdg.WorkItem | None) -> str: ...
    def _updateWorkingDir(self, working_dir: str, lsr: str | None) -> bool: ...
    def onStart(self) -> bool: ...
    def onStop(self) -> bool: ...
    def onStartCook(self, static: bool, cook_set: AbstractSet[_pdg.Node]) -> bool: ...
    def onStopCook(self, cancel: bool) -> bool: ...
    def submitAsJob(
        self, graph_file: str, node_path: str
    ) -> tuple[str, int] | tuple[None, None]: ...
    def workItemSucceeded(
        self, workitem_id: int, index: int, cook_duration: float, jobid: str = ...
    ) -> None: ...
    def workItemFailed(self, workitem_id: int, index: int, jobid: str = ...) -> None: ...
    def workItemCanceled(self, workitem_id: int, index: int, jobid: str = ...) -> None: ...
    def workItemStartCook(self, workitem_id: int, index: int, jobid: str = ...) -> None: ...
    def endSharedServer(self, sharedserver_name: str) -> bool: ...
    def onTick(self) -> _pdg.tickResult: ...
    def execEvent(self, event: _Event) -> str | None: ...
    def onPreSubmitItem(
        self, work_item: _pdg.WorkItem, job_env: MutableMapping[str, str], item_json: _JobSpec
    ) -> _JobSpec: ...
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult: ...
    def onScheduleStatic(
        self,
        dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]],
        dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]],
        ready_items: Sequence[_pdg.WorkItem],
    ) -> None: ...
    def onCancelWorkItems(
        self, work_items: Sequence[_pdg.WorkItem], node: _pdg.Node | None
    ) -> None: ...
    def getLogURI(self, work_item: _pdg.WorkItem) -> str: ...
    def getStatusURI(self, work_item: _pdg.WorkItem) -> str: ...
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str: ...
