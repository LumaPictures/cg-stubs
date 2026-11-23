from collections.abc import Callable
from typing import TypeVar

from _pdg import BaseType, Service, _DictValue
from _pdgutils import PDGNetTLSConfig, PDGNPollingClient
from pdg.scheduler import PyScheduler
from pdg.job.callbackserver import CallbackServerAPI
from pdgutils import PDGNetMQRelay

_T = TypeVar("_T")

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
    # Local MQ pid or HQueue job id (int), or a Deadline job id (str).
    mq_jobid: int | str | None
    def __init__(self) -> None: ...
    def resetState(self) -> None: ...
    def __str__(self) -> str: ...
    def startMQConnectTime(self) -> None: ...
    def hasMQConnectTimeExpired(self) -> bool: ...

class MQError(Exception):
    code: int | None
    message: str
    def __init__(self, code: int | None, msg: str) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class MQUtility:
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
    def getService(
        mq_service_name: str | None,
        scheduler_type: BaseType,
        log: Callable[[str], object] | None = ...,
    ) -> Service | None: ...
    @staticmethod
    def isLocalMQ(mqservice: Service) -> bool: ...
    @staticmethod
    def isConnectMQ(mqservice: Service) -> bool: ...
    @staticmethod
    def startService(
        scheduler: PyScheduler, mqservice: Service, log: Callable[[str], object] | None = ...
    ) -> bool: ...
    @staticmethod
    def stopService(
        scheduler: PyScheduler, mqservice: Service, log: Callable[[str], object] | None = ...
    ) -> bool: ...
    @staticmethod
    def clearMQData(mqservice: Service) -> None: ...
    @staticmethod
    def getMQUse(mqservice: Service) -> int: ...
    @staticmethod
    def incrementMQUse(mqservice: Service) -> int: ...
    @staticmethod
    def decrementMQUse(mqservice: Service) -> int: ...
    @staticmethod
    def setMQServerAddress(
        mqservice: Service, addr: str, rpc_port: int, relay_port: int, http_port: int
    ) -> None: ...
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
    def startLocalMQ(service: Service, log: Callable[[str], object] | None = ...) -> int | None: ...
    @staticmethod
    def killLocalMQ(service: Service, log: Callable[[str], object] | None = ...) -> bool: ...
    @staticmethod
    def stopMQRemotely(
        mq_addr: str | None,
        relay_port: int | None,
        rpc_port: int | None,
        log: Callable[[str], object] | None = ...,
        tls_cfg: PDGNetTLSConfig = ...,
    ) -> bool: ...
    @staticmethod
    def isWindows() -> bool: ...
    @staticmethod
    def createLocalMQCommand(
        connection_file: str,
        relayport: int = ...,
        callbackport: int = ...,
        ip: str = ...,
        loglvl: int = ...,
        logfile: str | None = ...,
        quiet: bool = ...,
    ) -> str: ...

class MQSchedulerMixin:
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    @staticmethod
    def getMQServiceName(mqusage: int) -> str | None: ...
    def getPollingClient(self) -> PDGNPollingClient | None: ...
    def getMQService(self) -> Service | None: ...
