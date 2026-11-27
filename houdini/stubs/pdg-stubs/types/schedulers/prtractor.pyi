import _pdg
import threading
import tractor.api.author as author
import xmlrpc.client
from collections import deque
from collections.abc import Mapping, Sequence, Set as AbstractSet
from getpass import getuser as getuser
from pdg.job.callbackserver import CallbackServer as CallbackServer
from pdg.job.eventdispatch import EventDispatchMixin as EventDispatchMixin, _Event
from pdg.job.mqrelay import MQRelay as MQRelay
from pdg.scheduler import PyScheduler as PyScheduler
from pdg.utils import parseEnvironmentFile as parseEnvironmentFile, print_headless as print_headless
from pdg.utils.mq import MQInfo as MQInfo, MQSchedulerMixin as MQSchedulerMixin, MQState as MQState, MQUsage as MQUsage, MQUtility as MQUtility
from typing import Any, NotRequired, TypedDict

class _TaskRow(TypedDict):
    title: str
    state: str
    tid: int
    item_name: str
    service_key: NotRequired[str]

theTickVerboseLogPeriod: int
theNeutralizeServiceKey: str
theRetryDoneTasks: bool
user_input_special_chars: dict[str, list[str]]
theServiceJobTitleFormatStr: str

def displayError(msg: str, exception: BaseException | None = None) -> None:
    """Pop up a message dialog to display the given error message.

    If houdini or its ui are unavailable, then it writes the message to the console.
    """

class RunItem:
    work_item: _pdg.WorkItem | None
    scheduled_stamp: float
    keepalive_stamp: float
    theKeepaliveTickPeriod: int
    theKeepaliveTimeout: int
    theStartTaskTimeout: int
    failed: bool
    long_running: bool
    def __init__(self, work_item: _pdg.WorkItem | None, scheduled_stamp: float) -> None: ...
    def name(self) -> str | None: ...
    def keepalive(self) -> None: ...
    def started(self) -> None: ...
    def hasStarted(self) -> bool: ...
    def resetScheduled(self) -> None: ...
    def setFailed(self, failed: bool) -> None: ...
    def elapsedTime(self, now: float) -> float: ...
    def isExpired(self, now: float) -> bool: ...

class TaskSpooler:
    """
    Helper class for spooling Tractor Tasks.
    """
    def __init__(self, in_job: bool, scheduler: TractorScheduler) -> None:
        """
        in_job: When False we expect to be passed a Server Proxy object to call
                spool_tractor_task.
        scheduler: TractorScheduler instance
        """
    def spool_task(self, task: author.Task, rpcserverproxy: xmlrpc.client.ServerProxy | None = None) -> Any:
        """
        Spools the given task, which may be asynchronous.
        task: author.Task
        rpcserverproxy: MQ RPC Proxy, None when in_job is True
        """

class TractorScheduler(EventDispatchMixin, MQSchedulerMixin, PyScheduler):
    """
    Scheduler implementation that interfaces with a Tractor farm instance.
    scheduler : typename
    name: name of scheduler
    """
    callbackLock: threading.Lock
    rootjob_jid: int | None
    mqrelay: MQRelay | None
    activeTaskTitles: set[str]
    retries: dict[str, int]
    runningItems: dict[str, RunItem]
    taskTitleByItemId: dict[int, str]
    tasksToRetry: dict[int, _TaskRow]
    useKeepalive: int
    stateChanges: deque[tuple[str, int | str | None, str]]
    mq_hostname: str | None
    mq_xmlport: int | None
    mq_relayport: int | None
    running_services: list[_pdg.Service]
    file_env: dict[str, str]
    parmprefix: str
    cook_tid: int
    mq_tid: int
    mqTaskTitle: str
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onStop(self) -> bool:
        """
        onStop(self) -> boolean

        [virtual] Called before the underlying scheduler PDG node is destroyed.
        """
    def execEvent(self, event: _Event) -> str | None:
        """
        Override of EventDispatchMixin
        """
    def applicationBin(self, name: str, work_item: _pdg.WorkItem | None) -> str | None:
        """
        [virtual] Returns the path to the given application
        """
    def createTaskSpooler(self, in_job: bool) -> TaskSpooler:
        """
        Returns an object that is used to spool tractor jobs.  This is called
        once when the scheduler is created.
        in_job: True when we are part of the job, and so can expand tasks locally.
        """
    def onStartCook(self, static: bool, cook_set: AbstractSet[_pdg.Node]) -> bool:
        """
        onStartCook(self, static, cook_set) -> boolean

        [virtual] Cook start callback
        """
    def startService(self, service: _pdg.Service) -> bool | None:
        """
        start a service.
        """
    def stopService(self, service: _pdg.Service, cancel: bool) -> bool: ...
    def stopServiceClient(self, service: _pdg.Service, client: _pdg.ServiceClientInfo) -> bool: ...
    def shouldRetryTask(self, task: _TaskRow) -> bool: ...
    def neutralize_task(self, task: _TaskRow) -> str: ...
    def workItemStartCook(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        [virtual] Called by EventDispatch when a workitem signals started.
        """
    def workItemSucceeded(self, workitem_id: int, index: int, cook_duration: float, jobid: str = '') -> None:
        """
        [virtual] Called by EventDispatch when a workitem signals success.
        """
    def workItemFailed(self, workitem_id: int, index: int, jobid: str = '') -> None:
        """
        [virtual] Called by EventDispatch when a workitem signals failure.
        """
    def workItemKeepalive(self, workitem_id: int, jobid: str = '') -> None:
        """
        [virtual] Called by EventDispatchMixin when a workitem keepalive RPC is received.
        """
    def tickKeepalive(self) -> None: ...
    def onTick(self) -> _pdg.tickResult:
        """
        [virtual] Called during a cook. Checks on jobs in flight to see if any have
        finished.
        """
    def onStopCook(self, cancel: bool) -> bool:
        """
        [virtual] Callback invoked by PDG when graph cook ends.  Can be called
                  multiple times.
        """
    def submitAsJob(self, graph_file: str, node_name: str) -> tuple[None, None] | tuple[str, int]:
        """
        [virtual]
        Called by pressing the 'Submit as Job' button on the scheduler node
        UI.  Creates a job which cooks that TOP graph using hython.
        """
    def endSharedServer(self, sharedserver_name: str) -> bool:
        """
        [virtual] Called by a job or on cook end to terminate the sharedserver
        """
    def onPreSubmitItem(self, work_item: _pdg.WorkItem | None, job_env: Mapping[str | bytes, str | bytes], item_command: str) -> str:
        """
        Modifies the item command before it gets submitted to be run.
        Intended to be used in a user subclass of this scheduler.
        """
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult:
        """
        onSchedule(self, pdg.PyWorkItem) -> pdg.SchedulerResult

        Schedules the work item, e.g. submits a Task to Tractor to perform
        work described in the work item. Returns pdg.scheduleResult.Succeeded.
        """
    def onScheduleStatic(self, dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], ready_items: Sequence[_pdg.WorkItem]) -> None: ...
    def onCancelWorkItems(self, work_items: Sequence[_pdg.WorkItem], node: _pdg.Node | None) -> None: ...
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str: ...
    def getLogURI(self, work_item: _pdg.WorkItem) -> str:
        """
        [virtual]
        Returns the log URL for the Task corresponding to the given work item.
        """
    def getStatusURI(self, work_item: _pdg.WorkItem) -> str:
        """
        [virtual]
        Return the status URL for the Task corresponding to the given work item.
        """
