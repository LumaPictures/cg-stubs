import _pdg
import re
import threading
import xmlrpc.client
from collections import deque
from collections.abc import Mapping, MutableMapping, Sequence, Set as AbstractSet
from pdg.job.callbackserver import CallbackServerAPI as CallbackServerAPI
from pdg.job.eventdispatch import EventDispatchMixin as EventDispatchMixin, _Event
from pdg.scheduler import PyScheduler as PyScheduler, convertEnvMapToUTF8 as convertEnvMapToUTF8
from pdg.utils import parseEnvironmentFile as parseEnvironmentFile
from pdg.utils.mq import MQInfo as MQInfo, MQSchedulerMixin as MQSchedulerMixin, MQState as MQState, MQUsage as MQUsage, MQUtility as MQUtility
from pdgutils import PDGNetMQRelay
from typing import TypedDict

class _PlatformCommands(TypedDict):
    linux: str
    macosx: str
    windows: str

class _Condition(TypedDict):
    type: str
    name: str
    op: str
    value: str

class _JobSpec(TypedDict, total=False):
    name: str
    command: str | _PlatformCommands
    onCancel: _PlatformCommands
    onError: _PlatformCommands
    cpus: int
    priority: int
    parentIds: list[int]
    children: list['_JobSpec']
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

def displayError(msg: str, exception: BaseException | None = None) -> None:
    """Pop up a message dialog to display the given error message.

    If houdini or the ui are unavailable, then it writes the message to the console.
    """
def displayMessage(msg: str) -> None:
    """Pop up a message dialog to display the given message.

    If houdini or the ui are unavailable, then it writes the message to the console.
    """
def doesHQServerExists(hq_server: str) -> bool:
    """Check that the given HQ server can be connected to.

    Returns True if the server exists and False if it does not. Furthermore,
    it will display an error message if it does not exists."""
def _connectToHQServer(hq_server: str) -> xmlrpc.client.ServerProxy | None:
    """Connect to the HQueue server and return the proxy connection."""
def getHQRoot(hq_server: str) -> str | None:
    """Query the HQueue server and return the mount point path
    to the HQueue shared folder root.

    Return None if the path cannot be retrieved from the server.
    """

theTickVerboseLogPeriod: int

class HQueueScheduler(EventDispatchMixin, MQSchedulerMixin, PyScheduler):
    """
    Scheduler implementation for SideFX HQueue scheduler.
    """
    hqserver: xmlrpc.client.ServerProxy | None
    rpc_lock: threading.Lock
    root_id: int
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    node_id: dict[str, int]
    workitem_ids: dict[int, int]
    waiting_ids: set[int]
    running_ids: set[int]
    retries: dict[int, int]
    tickPeriod: None
    maxItems: None
    var_capture_re: re.Pattern[str]
    custom_port_range: None
    ready_deque: deque[tuple[_pdg.WorkItem, _JobSpec]]
    running_services: list[_pdg.Service]
    file_env: dict[str, str]
    MQServiceNameFarm: str
    hq_caps_inherit_conditions: bool
    hq_throttle_flag: bool
    parmprefix: str
    schedulecount: int
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None:
        """
        __init__(self, pdg.Scheduler, str)
        """
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def startService(self, service: _pdg.Service) -> bool:
        """
        [virtual] Starts the MQ server if its not already running.
        This can run MQ locally or remotely on farm, based on the service name.
        The command used to start MQ should have been set in service.data.
        Returns True if service is running.
        """
    def stopService(self, service: _pdg.Service, cancel: bool) -> bool:
        """
        Stops the given service.
        First tries to stop it via remote call, then if that fails, kills the 
        local process or farm job.
        """
    def startServiceClient(self, service: _pdg.Service, client: _pdg.ServiceClientInfo) -> bool: ...
    def stopServiceClient(self, service: _pdg.Service, client: _pdg.ServiceClientInfo) -> bool: ...
    @staticmethod
    def getMQServiceName(mqusage: int) -> str | None:
        """
        Returns the service name based on mqusage (farm or local)
        """
    def _localsharedroot(self) -> str | None:
        """
        returns the local path to HQROOT, possibly by contacting the
        server.  Returns None on failure.
        """
    def applicationBin(self, name: str, work_item: _pdg.WorkItem | None) -> str:
        """
        [virtual] Returns the path to the given application
        """
    def _updateWorkingDir(self, working_dir: str, lsr: str | None) -> bool:
        """
        working_dir - the local path to the working directory
        lsr - the local path to $HQROOT

        recache  _localWorkingDir and _remoteWorkingDir and call SetWorkingDir

        NOTE: This is called directly by the hqueuescheduler TOP node
        """
    def onStart(self) -> bool:
        """
        onStart(self) -> boolean

        [virtual] Scheduler start callback.
        """
    def onStop(self) -> bool:
        """
        onStart(self) -> boolean

        [virtual] Scheduler stop callback.
        """
    def onStartCook(self, static: bool, cook_set: AbstractSet[_pdg.Node]) -> bool:
        """
        onStartCook(self, static, cook_set) -> boolean

        [virtual] Cook start callback. Starts a root job for the cook session
        """
    def onStopCook(self, cancel: bool) -> bool:
        """
        onStopCook(self, cancel) -> boolean

        [virtual] Cook stop callback. Clears the root job for the cook session
        """
    def submitAsJob(self, graph_file: str, node_path: str) -> tuple[str, int] | tuple[None, None]:
        """
        Called by pressing the 'Submit as Job' button on the scheduler node
        UI.  Creates a job which cooks that TOP graph using hython.
        """
    def workItemSucceeded(self, workitem_id: int, index: int, cook_duration: float, jobid: str = '') -> None:
        """
        Called by EventDispatch when a workitem signals success.
        """
    def workItemFailed(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        Called by EventDispatch when a workitem signals failure.
        """
    def workItemCanceled(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        Called by EventDispatch when a workitem signals cancelation.
        This can happen when the job is ejected,canceled,abandoned,timed out
        """
    def workItemStartCook(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        Called by EventDispatch when a workitem signals start.
        """
    def endSharedServer(self, sharedserver_name: str) -> bool:
        """
        Called by a job or on cook end to terminate the sharedserver
        """
    def onTick(self) -> _pdg.tickResult:
        """ [virtual] Called during cook  """
    def execEvent(self, event: _Event) -> str | None: ...
    def onPreSubmitItem(self, work_item: _pdg.WorkItem, job_env: MutableMapping[str, str], item_json: _JobSpec) -> _JobSpec:
        """
        Modifies the item json before it gets submitted to be run.
        Intended to be used in a user subclass of this scheduler.
        """
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult:
        """
        [virtual] onSchedule(self, pdg.PyWorkItem) -> pdg.ScheduleResult

        Schedules the work item, e.g. submits a job to HQueue to perform the
        work described in the work item. Returns pdg.scheduleResult.Succeeded
        on success, and pdg.scheduleResult.Failed on failures. Never cooks
        the work item directly, and thus does not return
        pdg.scheduleResult.CookSucceeded unless command is empty
        """
    def onScheduleStatic(self, dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], ready_items: Sequence[_pdg.WorkItem]) -> None: ...
    def onCancelWorkItems(self, work_items: Sequence[_pdg.WorkItem], node: _pdg.Node | None) -> None: ...
    def getLogURI(self, work_item: _pdg.WorkItem) -> str: ...
    def getStatusURI(self, work_item: _pdg.WorkItem) -> str: ...
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str: ...
