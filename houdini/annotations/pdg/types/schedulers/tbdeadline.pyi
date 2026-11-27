import datetime
from collections import deque
from collections.abc import Mapping, Sequence
from collections.abc import Set as AbstractSet
from typing import NotRequired, TypedDict

from _typeshed import SupportsWrite

import _pdg
from pdg.job.callbackserver import CallbackServerAPI
from pdg.types.schedulers.tbdeadline_utils import DeadlineCmdInteractive
from pdg.utils.mq import MQInfo
from pdgutils import PDGNetMQRelay

# The task file's JSON, which the PDGDeadline plugin reads to run a work item.
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

class DeadlineScheduler:
    MQServiceNameFarm: str
    custom_port_range: tuple[int, int] | None
    rootjob_id: str | None
    local_job_dir: str | None
    remote_job_dir: str | None
    plugin_file_name: str | None
    # (task id, work item id) when scheduling work items as tasks of the root job, or
    # (job id, work item id) when scheduling them as jobs.
    active_queue: deque[tuple[int | str, int]]
    # (task id, work item) or (work item, job file path), as active_queue.
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
    def __init__(self, scheduler: _pdg.Scheduler, name: str) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def startService(self, service: _pdg.Service) -> bool: ...
    @staticmethod
    def startMQJobOnDeadline(cmd: str) -> str | None: ...
    def stopService(self, service: _pdg.Service, cancel: bool) -> bool: ...
    def stopMQ(
        self,
        service: _pdg.Service | None,
        mq_jobid: int | str | None,
        mq_addr: str | None,
        relay_port: int | None,
        rpc_port: int | None,
    ) -> bool: ...
    @staticmethod
    def getMQServiceName(mqusage: int) -> str | None: ...
    def onStart(self) -> bool: ...
    def onStop(self) -> bool: ...
    def onStartCook(self, static: bool, cook_set: AbstractSet[_pdg.Node]) -> bool: ...
    def onStopCook(self, cancel: bool) -> bool: ...
    def onPreSubmitItem(
        self,
        work_item: _pdg.WorkItem | None,
        job_env: Mapping[str, str | int | None],
        item_json: _TaskJSON,
    ) -> _TaskJSON: ...
    def onSchedule(self, work_item: _pdg.WorkItem) -> _pdg.scheduleResult: ...
    def onScheduleStatic(
        self,
        dependencies: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]],
        dependents: Mapping[_pdg.WorkItem, Sequence[_pdg.WorkItem]],
        ready_items: Sequence[_pdg.WorkItem],
    ) -> None: ...
    # None for an application other than python and hython.
    def applicationBin(self, name: str, work_item: _pdg.WorkItem | None) -> str | None: ...
    # (None, None) if the working directory can't be set up, else ("", the job's id).
    def submitAsJob(
        self, graph_file: str, node_name: str
    ) -> tuple[None, None] | tuple[str, str]: ...
    def onTick(self) -> _pdg.tickResult: ...
    def getLogURI(self, work_item: _pdg.WorkItem) -> str: ...
    def writeStringDataFromWorkItem(
        self,
        work_item: _pdg.WorkItem | None,
        fileobj: SupportsWrite[str],
        work_item_var_name: str,
        deadline_var_name: str,
    ) -> None: ...
    def writeIntDataFromWorkItem(
        self,
        work_item: _pdg.WorkItem | None,
        fileobj: SupportsWrite[str],
        work_item_var_name: str,
        deadline_var_name: str,
    ) -> None: ...
    @staticmethod
    def writeJobEnv(
        job_file: SupportsWrite[str], env_idx: int, key: str, value: str | int | None
    ) -> int: ...
    @staticmethod
    def writeFileKeyValues(out_file: SupportsWrite[str], kvpairs: Mapping[str, str]) -> None: ...
    def writeJobTaskExtraInfoNames(
        self, job_file: SupportsWrite[str], work_item: _pdg.WorkItem | None
    ) -> None: ...
    def writeJobFileKeyValues(
        self, job_file: SupportsWrite[str], work_item: _pdg.WorkItem | None, work_dir: str
    ) -> None: ...
    def writeJobFileEnvKeyValues(
        self, job_file: SupportsWrite[str], work_item: _pdg.WorkItem | None, env_idx: int
    ) -> int: ...
    def writePluginFileKeyValues(
        self, plugin_file: SupportsWrite[str], work_item: _pdg.WorkItem | None
    ) -> None: ...
    def getUserRepositoryCommandArgument(self, cmd_args: list[str]) -> list[str]: ...
    def endSharedServer(self, sharedserver_name: str) -> bool: ...
    def expandCommandTokens(self, item_command: str, work_item: _pdg.WorkItem | None) -> str: ...
