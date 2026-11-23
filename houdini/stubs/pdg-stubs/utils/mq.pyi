from _pdg import BaseType as BaseType, Service as Service, _DictValue
from _pdgutils import PDGNPollingClient as PDGNPollingClient
from collections.abc import Callable as Callable
from pdg.job.callbackserver import CallbackServerAPI as CallbackServerAPI
from pdg.scheduler import PyScheduler as PyScheduler
from pdgutils import PDGNetMQRelay, PDGNetTLSConfig

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class MQState:
    NONE: int
    LAUNCHED: int
    CONNECTED: int
    ERRORED: int

class MQUsage:
    FARM: int
    LOCAL: int
    CONNECT: int

class MQServerLogLevel:
    LogNone: int
    LogErrors: int
    LogWarnings: int
    LogAll: int

class MQInfo:
    """
    MQ state container for a scheduler node.
    """
    mq_service_name: str | None
    mqstate: int
    mqusage: int
    connfile_maxtime: int
    connfile_starttime: float
    client_id: str
    mq_host: str | None
    mq_rpcport: int | None
    mq_relayport: int | None
    mq_httpport: int | None
    mq_jobid: int | str | None
    def __init__(self) -> None: ...
    def resetState(self) -> None:
        """
        Resets transient state, doesn't clear persistent config
        """
    def startMQConnectTime(self) -> None:
        """
        Marks the time when starting to wait for MQ connection file.
        """
    def hasMQConnectTimeExpired(self) -> bool:
        """
        Returns True if time since started waiting for MQ connection file
        has passed the maximum wait time.
        """

class MQError(Exception):
    """
    Error class for MQ
    """
    code: int | None
    message: str
    def __init__(self, code: int | None, msg: str) -> None: ...

class MQUtility:
    """
    Contains utlity functions and constants for managing MQ.
    """
    MQServiceNameLocal: str
    MQServiceNameConnect: str
    MQCommandData: str
    NetTimeout: int
    RelayPollingTime: int
    RelayMaxReceiveMessageBuffer: int
    ConnectionFileName: str
    ConnectionFileMaxTime: int
    MaxConnections: int
    MaxHTTPConnections: int
    HTTPResult: str
    @staticmethod
    def getService(mq_service_name: str | None, scheduler_type: BaseType, log: Callable[[str], object] | None = None) -> Service | None: ...
    @staticmethod
    def isLocalMQ(mqservice: Service) -> bool: ...
    @staticmethod
    def isConnectMQ(mqservice: Service) -> bool: ...
    @staticmethod
    def startService(scheduler: PyScheduler, mqservice: Service, log: Callable[[str], object] | None = None) -> bool: ...
    @staticmethod
    def stopService(scheduler: PyScheduler, mqservice: Service, log: Callable[[str], object] | None = None) -> bool: ...
    @staticmethod
    def clearMQData(mqservice: Service) -> None: ...
    @staticmethod
    def getMQUse(mqservice: Service) -> int: ...
    @staticmethod
    def incrementMQUse(mqservice: Service) -> int: ...
    @staticmethod
    def decrementMQUse(mqservice: Service) -> int: ...
    @staticmethod
    def setMQServerAddress(mqservice: Service, addr: str, rpc_port: int, relay_port: int, http_port: int) -> None: ...
    @staticmethod
    def updateInfo(mqservice: Service, mqinfo: MQInfo) -> None: ...
    @staticmethod
    def getMQServerAddress(mqservice: Service) -> str | None: ...
    @staticmethod
    def getMQServerRPCPort(mqservice: Service) -> int | None: ...
    @staticmethod
    def getMQServerRelayPort(mqservice: Service) -> int | None: ...
    @staticmethod
    def getMQServerHTTPPort(mqservice: Service) -> int | None: ...
    @staticmethod
    def getConnectionFileLocalPath(mqservice: Service) -> str | None: ...
    @staticmethod
    def getConnectionFileRemotePath(mqservice: Service) -> str | None: ...
    @staticmethod
    def setConnectionFilePaths(mqservice: Service, local_path: str, remote_path: str) -> None: ...
    @staticmethod
    def getServiceData(mqservice: Service, name: str, default_value: _T) -> _DictValue | _T: ...
    @staticmethod
    def setServiceData(mqservice: Service, name: str, value: int | float | str) -> None: ...
    @staticmethod
    def getMQError(mqservice: Service) -> str | None: ...
    @staticmethod
    def setMQError(mqservice: Service, error: str) -> None: ...
    @staticmethod
    def getMQJobID(mqservice: Service) -> int | str | None: ...
    @staticmethod
    def setMQJobID(mqservice: Service, jobid: int | str) -> None: ...
    @staticmethod
    def getMQParentJobID(mqservice: Service) -> int | None: ...
    @staticmethod
    def setMQParentJobID(mqservice: Service, jobid: int) -> None: ...
    @staticmethod
    def startLocalMQ(service: Service, log: Callable[[str], object] | None = None) -> int | None: ...
    @staticmethod
    def killLocalMQ(service: Service, log: Callable[[str], object] | None = None) -> bool: ...
    @staticmethod
    def stopMQRemotely(mq_addr: str | None, relay_port: int | None, rpc_port: int | None, log: Callable[[str], object] | None = None, tls_cfg: PDGNetTLSConfig = ...) -> bool:
        """
        Stop the MQ server via a remote network call.
        """
    @staticmethod
    def isWindows() -> bool:
        """
        Return true if this platform is Windows-based.
        """
    @staticmethod
    def createLocalMQCommand(connection_file: str, relayport: int = 0, callbackport: int = 0, ip: str = '*', loglvl: int = ..., logfile: str | None = None, quiet: bool = False) -> str:
        """
        Create a command that can be used to start a local 
        (but seperate process) MQ.
        """

class MQSchedulerMixin:
    """
    Intended to be mixed in to PyScheduler subclasses, for MQ usage.
    Assumes a standard naming of member variables:
    self.mqinfo  (MQInfo)
    self.mqrelay (PDGNetMQRelay)
    self._verboseLog() (for logging)
    """
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    @staticmethod
    def getMQServiceName(mqusage: int) -> str | None:
        """
        Returns the service name based on mqusage (farm or local)
        """
    def getPollingClient(self) -> PDGNPollingClient | None: ...
    def getMQService(self) -> Service | None:
        """
        Returns the MQ service used by this scheduler.
        """
