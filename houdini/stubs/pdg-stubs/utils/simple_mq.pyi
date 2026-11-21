# Houdini stubs generated from Houdini 22.0.466

from _pdgutils import PDGNPollingClient as PDGNPollingClient
from collections.abc import Callable as Callable
from pdg.job.callbackserver import CallbackServerAPI as CallbackServerAPI
from pdgutils import PDGNetMQRelay, PDGNetTLSConfig

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
    use_count: int
    local_pid: int | None
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
    def isRunning(self) -> bool: ...

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
    NetTimeout: int
    RelayPollingTime: int
    RelayMaxReceiveMessageBuffer: int
    ConnectionFileName: str
    ConnectionFileMaxTime: int
    MaxConnections: int
    MaxHTTPConnections: int
    HTTPResult: str
    @staticmethod
    def setMQServerAddress(mqinfo: MQInfo, addr: str, rpc_port: int, relay_port: int, http_port: int) -> None: ...
    @staticmethod
    def startLocalMQ(cmd: str, log: Callable[[str], object] | None = None) -> int: ...
    @staticmethod
    def killLocalMQ(pid: int, log: Callable[[str], object] | None = None) -> None: ...
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
    def createLocalMQCommand(connection_file: str, relayport: int = 0, callbackport: int = 0, ip: str = '*', loglvl: int = ..., logfile: str | None = None) -> str:
        """
        Create a command that can be used to start a local 
        (but seperate process) MQ.
        """

class SimpleMQSchedulerMixin:
    """
    Intended to be mixed in to PyScheduler subclasses, for MQ usage.
    Assumes a standard naming of member variables/functions:
    self._startFarmMQ
    self._killFarmMQ
    """
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    starting_mq: bool
    def __init__(self) -> None: ...
    def getPollingClient(self) -> PDGNPollingClient | None: ...
    def startPollingClient(self) -> None: ...
    def stopPollingClient(self) -> None: ...
    def checkPollingClient(self) -> bool: ...
