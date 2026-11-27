import _pdg
import datetime
from _typeshed import SupportsWrite
from collections import deque
from collections.abc import Mapping, Sequence, Set as AbstractSet
from pdg.job.callbackserver import CallbackServer as CallbackServer, CallbackServerAPI as CallbackServerAPI
from pdg.job.eventdispatch import EventDispatchMixin as EventDispatchMixin
from pdg.job.mqrelay import MQRelay as MQRelay
from pdg.scheduler import PyScheduler as PyScheduler
from pdg.types.schedulers.tbdeadline_utils import DeadlineCmdInteractive as DeadlineCmdInteractive
from pdg.utils import parseEnvironmentFile as parseEnvironmentFile
from pdg.utils.mq import MQInfo as MQInfo, MQSchedulerMixin as MQSchedulerMixin, MQState as MQState, MQUsage as MQUsage, MQUtility as MQUtility
from pdgutils import PDGNetMQRelay
from threading import Thread as Thread
from typing import NotRequired, TypedDict

class _TaskJSON(TypedDict):
    pdg_result_server: str
    pdg_http_port: int | None
    pdg_item_name: str
    pdg_item_id: str
    pdg_index: int
    dl_ignoreexit: int
    submit_as_job: str
    executable: str
    arguments: str
    executable_linux: NotRequired[str]
    arguments_linux: NotRequired[str]
    executable_macosx: NotRequired[str]
    arguments_macosx: NotRequired[str]
    executable_windows: NotRequired[str]
    arguments_windows: NotRequired[str]
    opencl_forcegpu: int
    gpus_per_task: int
    gpus_select_devices: str
    extra_infos: dict[str, str]
    pdg_item_env: NotRequired[dict[str, str | int | None]]

class DeadlineScheduler(EventDispatchMixin, MQSchedulerMixin, PyScheduler):
    """
    Scheduler implementation for Thinkbox's Deadline scheduler.
    """
    custom_port_range: tuple[int, int] | None
    rootjob_id: str | None
    local_job_dir: str | None
    remote_job_dir: str | None
    plugin_file_name: str | None
    active_queue: deque[tuple[int | str, int]]
    pending_queue: deque[tuple[int, _pdg.WorkItem] | tuple[_pdg.WorkItem, str]]
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    mqinfo: MQInfo
    repository_command_arg: list[str]
    dlcmd_intr: DeadlineCmdInteractive | None
    local_conn_file: str | None
    remote_conn_file: str | None
    start_time: datetime.datetime | None
    running_services: list[_pdg.Service]
    service_job_ids: list[str]
    file_env: dict[str, str]
    MQServiceNameFarm: str
    parmprefix: str
    launched_monitor: bool
    next_task_id: int
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def startService(self, service: _pdg.Service) -> bool:
        """
        Starts the MQ server if its not already running.
        This can run MQ locally or remotely on farm, based on the service name.
        The command used to start MQ should have been set in service.data.
        Returns True if service is running.
        """
    @staticmethod
    def startMQJobOnDeadline(cmd: str) -> str | None:
        """
        Starts MQ as a job on Deadline farm, and returns the job id.
        """
    def stopService(self, service: _pdg.Service, cancel: bool) -> bool:
        """
        Stops the MQ server.
        First tries to stop it via remote call, then if that fails, kills the 
        local process or farm job.
        """
    def stopMQ(self, service: _pdg.Service | None, mq_jobid: int | str | None, mq_addr: str | None, relay_port: int | None, rpc_port: int | None) -> bool:
        """
        Stops MQ by remote call first. If that fails, tries to kill the job if 
        on farm, or process if locally. Returns True if succeeds.
        """
    @staticmethod
    def getMQServiceName(mqusage: int) -> str | None:
        """
        Returns the service name based on mqusage (farm or local)
        """
    def onStart(self) -> bool:
        """
        onStart(self) -> boolean

        [virtual] Scheduler start callback.
        """
    def onStop(self) -> bool:
        """
        onStop(self) -> boolean

        [virtual] Scheduler stop callback.
        """
    def onStartCook(self, static: bool, cook_set: AbstractSet[_pdg.Node]) -> bool:
        """
        onStartCook(self, static, cook_set) -> boolean

        Sets up to start cooking. Initializes MQ, resolves Deadline repository,
        and starts the Deadline command interactive process.
        """
    def onStopCook(self, cancel: bool) -> bool:
        """
        Callback invoked by PDG when graph cook ends.
        Notify Deadline to stop (fail) current job.
        """
    def onPreSubmitItem(self, work_item: _pdg.WorkItem | None, job_env: Mapping[str, str | int | None], item_json: _TaskJSON) -> _TaskJSON:
        """
        Modifies the item json before it gets submitted to be run.
        Intended to be used in a user subclass of this scheduler.
        """
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult:
        """
        onSchedule(self, pdg.PyWorkItem) -> pdg.SchedulerResult

        Starts MQ if it hasn't started. Uses ServiceManager to share MQ use
        if using new MQ.

        Starts root job with first work item as first task.

        For subsequent work items (i.e. already running job), they are
        scheduled as tasks, appended as frames to the root job.

        Returns pdg.scheduleResult
        """
    def onScheduleStatic(self, dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]], ready_items: Sequence[_pdg.WorkItem]) -> None: ...
    def applicationBin(self, name: str, work_item: _pdg.WorkItem | None) -> str | None:
        """
        [virtual] Returns the path to the given application
        """
    def submitAsJob(self, graph_file: str, node_name: str) -> tuple[None, None] | tuple[str, str]:
        """
        Creates a job which cooks that TOP graph using hython.
        """
    def onTick(self) -> _pdg.tickResult:
        """
        Called during a cook to process the state of things in flight.
        Checks status of running servers.
        Tries to acquire MQ server address if needed.
        Connects relay to MQ if hasn't.
        Checks on active tasks to see if any have finished.
        Submits next batch of new tasks.
        """
    def getLogURI(self, work_item: _pdg.WorkItem) -> str:
        """
        Returns the URI to the log file for the given work_item.
        Note that Deadline archives its log files in bz2 format, so 
        'file:///path/to/log.bz2' will be returned
        """
    def writeStringDataFromWorkItem(self, work_item: _pdg.WorkItem | None, fileobj: SupportsWrite[str], work_item_var_name: str, deadline_var_name: str) -> None:
        """
        Write out the string data in work_item with name work_item_var_name to 
        fileobj using key deadline_var_name.
        After writing, fileobj will contain the following key-value pair: 
        deadline_var_name=work_item['work_item_var_name']
        """
    def writeIntDataFromWorkItem(self, work_item: _pdg.WorkItem | None, fileobj: SupportsWrite[str], work_item_var_name: str, deadline_var_name: str) -> None:
        """
        Write out the integer data in work_item with name work_item_var_name 
        to fileobj using key deadline_var_name.
        After writing, fileobj will contain the following key-value pair: 
        deadline_var_name=work_item['work_item_var_name']
        """
    @staticmethod
    def writeJobEnv(job_file: SupportsWrite[str], env_idx: int, key: str, value: str | int | None) -> int:
        """
        Write out the environment key-value pair to the given job_file, at 
        the given index.
        """
    @staticmethod
    def writeFileKeyValues(out_file: SupportsWrite[str], kvpairs: Mapping[str, str]) -> None: ...
    def writeJobTaskExtraInfoNames(self, job_file: SupportsWrite[str], work_item: _pdg.WorkItem | None) -> None:
        """
        Writes out jobfile task extra info names.
        """
    def writeJobFileKeyValues(self, job_file: SupportsWrite[str], work_item: _pdg.WorkItem | None, work_dir: str) -> None:
        """
        Writes out jobfile key-value pairs.
        Also writes out OutputDirectory0 if not specified in key-value pairs.
        """
    def writeJobFileEnvKeyValues(self, job_file: SupportsWrite[str], work_item: _pdg.WorkItem | None, env_idx: int) -> int:
        """
        Writes out jobfile environment key-value pairs.
        """
    def writePluginFileKeyValues(self, plugin_file: SupportsWrite[str], work_item: _pdg.WorkItem | None) -> None:
        """
        Writes out pluginfile environment key-value pairs.
        """
    def getUserRepositoryCommandArgument(self, cmd_args: list[str]) -> list[str]:
        """
        Returns deadline command argument formulated from user-specified 
        deadline repository, connection, and command-specific arguments.
        If user left the repository field empty, just returns the cmd_args, 
        which implies using default repository.
        """
    def endSharedServer(self, sharedserver_name: str) -> bool:
        """
        Called by a job or on cook end to terminate the sharedserver
        """
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str: ...
