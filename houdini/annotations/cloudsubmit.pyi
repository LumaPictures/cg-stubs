import queue
import threading
import xmlrpc.client
from typing import NotRequired, TypeAlias, TypedDict

import cloud
import hjsonrpc
import hutil.enum
from houtypes import JSONLike, JSONValue

# What an XML-RPC ServerProxy (default flags) unmarshals a reply into.
_XmlRpcValue: TypeAlias = (
    bool
    | int
    | float
    | str
    | xmlrpc.client.Binary
    | xmlrpc.client.DateTime
    | list["_XmlRpcValue"]
    | dict[str, "_XmlRpcValue"]
    | None
)

class _Project(TypedDict):
    state: str
    fraction_complete: float
    size_description: str
    estimated_remaining_time: str
    frames_remaining: int
    frames: dict[int, str]
    id: NotRequired[int]

# A project in getStatus's result: _Project without its frames, plus these.
class _ProjectStatus(TypedDict):
    state: str
    fraction_complete: float
    size_description: str
    estimated_remaining_time: str
    id: NotRequired[int]
    project_name: str
    is_done: bool

class _Status(TypedDict):
    cloud_server_state: str
    is_launching: bool
    running_jobs: list[_ProjectStatus]
    starting_jobs: list[_ProjectStatus]
    base_job_url: NotRequired[str]

CLOUD_HQUEUE_PORT: int
PORT: int
CLOUD_MONITOR_PORT: int
REMOTE_USER_NAME: str
REMOTE_MACHINE_PROJECT_PATH: str
SECURITY_GROUP_NAME: str
SECURITY_GROUP_DESCRIPTION: str
LOCAL_SERVER_ADDRESS: str

def startWithSysArgs() -> None: ...
def start(project_parms_path: str, temp_file_with_key: str, debug: bool, verbose: bool) -> None: ...

class RobustConnection:
    conn: hjsonrpc.ServiceProxy | xmlrpc.client.ServerProxy | None
    conn_desc: str
    method_name: str | None
    NUM_WAIT_SECONDS: int
    def __init__(
        self,
        conn: hjsonrpc.ServiceProxy | xmlrpc.client.ServerProxy | None,
        conn_desc: str,
        method_name: str | None = ...,
    ) -> None: ...
    def __getattr__(self, name: str) -> "RobustConnection": ...
    def __call__(self, *args: JSONLike | _XmlRpcValue) -> JSONValue | _XmlRpcValue: ...

def getConnection() -> hjsonrpc.ServiceProxy | None: ...
def openBrowser() -> None: ...

class ExitThread(Exception): ...

CloudSubmitState: hutil.enum.Enumeration
CloudServerState: hutil.enum.Enumeration

class RPCService:
    shutdown_after_rpc: bool
    cloud_region: str | None
    server_instance: "EC2Instance | None"
    queued_project_parms_paths: queue.Queue[str]
    is_launching: bool
    is_stalled: bool
    cloud_server_state: hutil.enum._EnumeratedValue
    projects: dict[str, _Project]
    project_lock: threading.RLock
    starting_job: bool
    def __init__(self) -> None: ...
    def addProject(self, project_name: str) -> None: ...
    def setIdForProject(self, project_name: str, job_id: int) -> None: ...
    def setState(
        self,
        project_name: str,
        state: hutil.enum._EnumeratedValue,
        size_description: str = ...,
        fraction_complete: float = ...,
        estimated_remaining_time: str = ...,
        frames_remaining: int = ...,
    ) -> None: ...
    def addDownloadedFrame(self, project_name: str, frame_number: int, local_frame_path: str) -> None: ...
    def setLaunching(self, is_launching: bool) -> None: ...
    def setStalled(self, is_stalled: bool) -> None: ...
    def isStalled(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def cloudServerTerminated(self, error: bool) -> None: ...
    def quit(self) -> None: ...
    def cloudRegion(self) -> str | None: ...
    def getCloudServerMachine(self) -> str | None: ...
    def queueProject(self, project_parms_path: str) -> None: ...
    def getStatus(self) -> _Status: ...
    def playFilesForProject(self, job_id: int | str) -> str | None: ...
    def terminateCloudInstances(self) -> None: ...
    def timeToAutoShutdown(self) -> JSONValue: ...
    def suggestProjectName(self, requested_project_name: str) -> str: ...

class HTTPRequestHandler(hjsonrpc.RPCRequestHandler):
    def do_GET(self) -> None: ...
    def redirectTo(self, url: str) -> None: ...

class EC2Instance:
    instance_id: str
    state: str
    machine_name: str
    private_machine_name: str
    start_time: str
    key_pair_name: str
    @classmethod
    def startInstanceAndWaitUntilRunning(
        cls,
        aws_connection: cloud.AWSConnection,
        machine_description: str,
        instance_type: str,
        license_category: str,
        houdini_version: str,
        server_machine: str = ...,
    ) -> "EC2Instance": ...
    @classmethod
    def beginStartingInstance(
        cls,
        aws_connection: cloud.AWSConnection,
        instance_type: str,
        license_category: str,
        houdini_version: str,
        server_machine: str = ...,
    ) -> "EC2Instance": ...
    @classmethod
    def beginStartingMultipleInstances(
        cls,
        aws_connection: cloud.AWSConnection,
        num_machines: int,
        instance_type: str,
        license_category: str,
        houdini_version: str,
        server_machine: str,
    ) -> None: ...
    @classmethod
    def getAllInstances(cls, aws_connection: cloud.AWSConnection) -> "list[EC2Instance]": ...
    @classmethod
    def findRunningInstanceWithMachineName(cls, aws_connection: cloud.AWSConnection, machine_name: str) -> "EC2Instance | None": ...
    def __init__(self, **kwargs: str) -> None: ...
    def refresh(self) -> None: ...
    def isRunning(self) -> bool: ...
    def status(self) -> str | None: ...
    def terminate(self) -> None: ...
    # The instance's user data as JSON; cloudsubmit's own instances have an object with
    # server_machine, start_client, license_category, ... (see _getUserData).
    def userData(self) -> JSONValue: ...
