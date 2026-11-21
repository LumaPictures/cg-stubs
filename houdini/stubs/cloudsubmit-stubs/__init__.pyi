# Houdini stubs generated from Houdini 22.0.466

import cloud
import hjsonrpc
import hutil.enum
import queue
import threading
import xmlrpc.client
from houtypes import JSONValue
from typing import Any, NotRequired, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_XmlRpcValue: TypeAlias = bool | int | float | str | xmlrpc.client.Binary | xmlrpc.client.DateTime | list['_XmlRpcValue'] | dict[str, '_XmlRpcValue'] | None
class _Project(TypedDict):
    state: str
    fraction_complete: float
    size_description: str
    estimated_remaining_time: str
    frames_remaining: int
    frames: dict[int, str]
    id: NotRequired[int]

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
def start(project_parms_path: str, temp_file_with_key: str, debug: bool, verbose: bool) -> None:
    """Start an RPC server in one thread, launch the local render monitor and
    open a browser window to it from another thread, and submit the job to the
    cloud and download the output from this thread.
    """

class RobustConnection:
    conn: hjsonrpc.ServiceProxy | xmlrpc.client.ServerProxy | None
    conn_desc: str
    method_name: str | None
    NUM_WAIT_SECONDS: int
    def __init__(self, conn: hjsonrpc.ServiceProxy | xmlrpc.client.ServerProxy | None, conn_desc: str, method_name: str | None = None) -> None: ...
    def __getattr__(self, name: str) -> RobustConnection: ...
    def __call__(self, *args: Any) -> JSONValue | _XmlRpcValue: ...

def getConnection() -> hjsonrpc.ServiceProxy | None:
    """Return a connection to the local cloud submission process's RPC
    server.

    Return None if the cloudsubmit process isn't running.
    """
def openBrowser() -> None:
    """Open a web browser pointing to this cloud submission process."""

class ExitThread(Exception): ...

CloudSubmitState: hutil.enum.Enumeration
CloudServerState: hutil.enum.Enumeration

class RPCService:
    shutdown_after_rpc: bool
    cloud_region: str | None
    server_instance: EC2Instance | None
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
    def setState(self, project_name: str, state: hutil.enum._EnumeratedValue, size_description: str = '', fraction_complete: float = 0.0, estimated_remaining_time: str = '', frames_remaining: int = 0) -> None: ...
    def addDownloadedFrame(self, project_name: str, frame_number: int, local_frame_path: str) -> None: ...
    def setLaunching(self, is_launching: bool) -> None: ...
    def setStalled(self, is_stalled: bool) -> None: ...
    def isStalled(self) -> bool: ...
    @hjsonrpc.rpcMethod
    def isRunning(self) -> bool: ...
    @hjsonrpc.rpcMethod
    def cloudServerTerminated(self, error: bool) -> None: ...
    @hjsonrpc.rpcMethod
    def quit(self) -> None: ...
    @hjsonrpc.rpcMethod
    def cloudRegion(self) -> str | None: ...
    @hjsonrpc.rpcMethod
    def getCloudServerMachine(self) -> str | None: ...
    @hjsonrpc.rpcMethod
    def queueProject(self, project_parms_path: str) -> None: ...
    @hjsonrpc.rpcMethod
    def getStatus(self) -> _Status: ...
    @hjsonrpc.rpcMethod
    def playFilesForProject(self, job_id: int | str) -> str | None: ...
    @hjsonrpc.rpcMethod
    def terminateCloudInstances(self) -> None: ...
    @hjsonrpc.rpcMethod
    def timeToAutoShutdown(self) -> JSONValue: ...
    @hjsonrpc.rpcMethod
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
    def startInstanceAndWaitUntilRunning(cls, aws_connection: cloud.AWSConnection, machine_description: str, instance_type: str, license_category: str, houdini_version: str, server_machine: str = ...) -> EC2Instance: ...
    @classmethod
    def beginStartingInstance(cls, aws_connection: cloud.AWSConnection, instance_type: str, license_category: str, houdini_version: str, server_machine: str = ...) -> EC2Instance: ...
    @classmethod
    def beginStartingMultipleInstances(cls, aws_connection: cloud.AWSConnection, num_machines: int, instance_type: str, license_category: str, houdini_version: str, server_machine: str) -> None: ...
    @classmethod
    def getAllInstances(cls, aws_connection: cloud.AWSConnection) -> list[EC2Instance]: ...
    @classmethod
    def findRunningInstanceWithMachineName(cls, aws_connection: cloud.AWSConnection, machine_name: str) -> EC2Instance | None: ...
    def __init__(self, **kwargs: str) -> None: ...
    def refresh(self) -> None: ...
    def isRunning(self) -> bool: ...
    def status(self) -> str | None:
        '''Return the instance status ("running", "starting", etc.), or None
        if nothing is known about the instance.  Note that if the instance
        status is "terminated", this method returns None.
        '''
    def terminate(self) -> None: ...
    def userData(self) -> JSONValue: ...
