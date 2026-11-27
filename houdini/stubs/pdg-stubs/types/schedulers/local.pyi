import _pdg
import subprocess
import threading
from collections.abc import Iterator, Mapping, MutableMapping, Sequence, Set as AbstractSet
from pdg.job.callbackserver import CallbackServerAPI as CallbackServerAPI, CallbackServerMixin as CallbackServerMixin
from pdg.job.eventdispatch import _Event
from pdg.scheduler import PyScheduler as PyScheduler, convertEnvMapToUTF8 as convertEnvMapToUTF8
from pdg.staticcook import StaticCookMixin as StaticCookMixin
from pdg.utils import expand_vars as expand_vars, parseEnvironmentFile as parseEnvironmentFile
from pdg.utils.mq import MQInfo as MQInfo, MQSchedulerMixin as MQSchedulerMixin, MQState as MQState, MQUsage as MQUsage, MQUtility as MQUtility
from pdgutils import PDGNetMQRelay
from typing import TextIO, TypedDict

class _ProcessOptions(TypedDict, total=False):
    requireswindow: bool
    shell: bool
    cwd: str

class RunItem:
    """
    Holds the data for one running processes
    """
    eExitCodeError: int
    eExitCodeWarn: int
    eExitCodeRetry: int
    eExitCodeIgnore: int
    eTimeoutFail: int
    eTimeoutSuccess: int
    work_item: _pdg.WorkItem | None
    id: int | None
    process: subprocess.Popen[bytes] | None
    output_file: TextIO
    single: bool
    cpu_slots: float
    released_cpu_slots: float
    exit_code_handling: int
    exit_code_custom: int
    retries_remaining: int
    retry_attr: str
    item_command: str
    job_env: Mapping[str, str]
    extra: _ProcessOptions
    start_time: float
    max_time: float
    on_timeout: int
    max_memory: float
    max_memory_mb: float
    on_memory_exceeded: int
    @staticmethod
    def spawn(work_item: _pdg.WorkItem | None, item_command: str, item_log_path: str, single: bool, cpu_slots: float, job_env: Mapping[str, str], extra: _ProcessOptions) -> RunItem | None: ...
    def __init__(self, work_item: _pdg.WorkItem | None, process: subprocess.Popen[bytes] | None, output_file: TextIO, single: bool, cpu_slots: float) -> None: ...
    def swapSlots(self) -> None: ...
    def checkExitCode(self, ec: int) -> int | None:
        """ Check the given exit code, returns scheduler action """
    def closeLog(self) -> None: ...
    def writeToLog(self, msg: str, flush: bool = False) -> None: ...
    def restart(self, ec: int) -> subprocess.Popen[bytes] | None:
        """ Restart this job, returns None on failure """

class RunList:
    """
    Holds all running processes, represented by RunItem objects
    """
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[RunItem]: ...
    def add(self, runitem: RunItem) -> None: ...
    def remove(self, runitem: RunItem) -> None: ...
    def find(self, workitem_id: int) -> RunItem | None: ...
    def acquireSlots(self, workitem_id: int) -> None: ...
    def releaseSlots(self, workitem_id: int) -> None: ...
    def slotsUsed(self) -> float: ...
    def clear(self) -> None: ...

class LocalScheduler(CallbackServerMixin, StaticCookMixin, MQSchedulerMixin, PyScheduler):
    schedule_lock: threading.RLock
    run_list: RunList
    max_cpu_slots: float
    file_env: dict[str, str]
    running_services: dict[str, dict[int, RunItem]]
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    running_single: bool
    static_cook: bool
    cook_id: str
    parmprefix: str
    mqlaunched: bool
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onStart(self) -> bool:
        """
        [virtual]  Called when scheduler is created.
        Can be used to do one-time intitialization
        """
    def onStop(self) -> bool:
        """
        [virtual] Called when scheduler is destroyed.
        """
    def startService(self, service: _pdg.Service) -> bool: ...
    def stopService(self, service: _pdg.Service, cancel: bool) -> bool: ...
    def startServiceClient(self, service: _pdg.Service, client: _pdg.ServiceClientInfo) -> bool: ...
    def stopServiceClient(self, service: _pdg.Service, client: _pdg.ServiceClientInfo) -> bool: ...
    def execEvent(self, event: _Event) -> str | None: ...
    def onStartCook(self, static: bool, cook_set: AbstractSet[_pdg.Node]) -> bool:
        """
        [virtual] Called when a graph cook starts.
        """
    def onStopCook(self, cancel: bool) -> bool:
        """
        [virtual] Called when a graph cook stops.
        """
    def submitAsJob(self, graph_file: str, node_path: str) -> tuple[None, None]:
        """
        [virtual] Called to cook the graph of the given node as a single job.
        """
    def killPools(self) -> None:
        """
        Helper.  Kills all remaining shared servers
        """
    def onTick(self) -> _pdg.tickResult:
        """
        [virtual] Called during a cook. Checks on jobs in flight to see if
        any have finished.  Also starts new jobs if any are available.
        Must return pdg.tickResult
        """
    def kill(self) -> None:
        """
        Helper.  Kills all remaining jobs and shared servers.
        """
    def workItemSucceeded(self, workitem_id: int, index: int, cook_duration: float, jobid: str = '') -> None:
        """
        [event dispatch] callback for work item finishing without error
        """
    def onSharedServerStarted(self, args: _pdg._SharedServerInfo) -> None:
        """
        [virtual] Called when a job has started a new sharedserver
        """
    def endSharedServer(self, sharedserver_name: str, kill: bool = False) -> bool:
        """
        [virtual] Called by a job or on cook end to terminate the sharedserver
        """
    def applicationBin(self, name: str, work_item: _pdg.WorkItem | None) -> str:
        """
        [virtual] Returns the path to the given application
        """
    def isWorkItemReady(self, workitem_id: int, index: int) -> bool | _pdg.workItemReadyResult:
        """
        [event dispatch] Called to check if a given batch item can start cooking.
        This is necessary when batches are set to cook when the dependencies of
        the first frame are ready.
        """
    def releaseJobSlots(self, workitem_id: int, jobid: str = '') -> None:
        """
        [event dispatch] when a work item wants to release
        the scheduler slots it currently occupies.
        """
    def acquireJobSlots(self, workitem_id: int, jobid: str = '') -> None:
        """
        [event dispatch] Called when a work item wants to (re)acquire
        the scheduler slots it previously released.
        """
    def onScheduleStatic(self, dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], ready_items: Sequence[_pdg.WorkItem]) -> None:
        """
        [virtual] Called to do a static cook of the graph.
        (pdg.cookType.StaticDepsFull or pdg.cookType.StaticDepsNode)
        The scheduler should manage the execution of the graph and report back
        all results.  Typically this would hand off execution to the farm scheduler
        using a static job spec.  The local scheduler provides a trivial
        implementation of this using staticcook.StaticCookMixin for testing
        purposes.
        """
    def onPreSubmitItem(self, work_item: _pdg.WorkItem, job_env: MutableMapping[str, str], item_command: str) -> str:
        """
        Modifies the item command before it gets submitted to be run.
        Intended to be used in a user subclass of this scheduler.
        """
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult:
        """
        [virtual] Called when the given work item is ready to be executed.
        Must return pdg.scheduleResult
        """
    def onCancelWorkItems(self, work_items: Sequence[_pdg.WorkItem], node: _pdg.Node | None) -> None: ...
    def getStatusURI(self, work_item: _pdg.WorkItem) -> str:
        """
        [virtual] Called to get a link to the details for the given work item.
        Typically this would be a URL to task details.
        """
    def getLogURI(self, work_item: _pdg.WorkItem) -> str:
        """
        [virtual] Called to get the link to the log file for the given work item.
        Typically this would be a URL to a log output page.
        """

def start_async(item_command: str, output_file: TextIO, job_env: Mapping[str, str], extra: _ProcessOptions = ...) -> subprocess.Popen[bytes] | None:
    """
    Helper. Executes the given cmd in a non-blocking subprocess
    item_command: the command script (shell)
    output_file: output stream redirection
    job_env: override environment
    return: Popen object
    """
