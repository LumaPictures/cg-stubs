from collections.abc import Callable

from _pdgutils import PDGNetTLSConfig, PDGNPollingClient
from pdg.job.callbackserver import CallbackServerAPI
from pdgutils import PDGNetMQRelay

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
    def resetState(self) -> None: ...
    def __str__(self) -> str: ...
    def startMQConnectTime(self) -> None: ...
    def hasMQConnectTimeExpired(self) -> bool: ...
    def isRunning(self) -> bool: ...

class MQError(Exception):
    code: int | None
    message: str
    def __init__(self, code: int | None, msg: str) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class MQUtility:
    NetTimeout: int
    RelayPollingTime: int
    RelayMaxReceiveMessageBuffer: int
    ConnectionFileName: str
    ConnectionFileMaxTime: int
    MaxConnections: int
    MaxHTTPConnections: int
    HTTPResult: str
    @staticmethod
    def setMQServerAddress(
        mqinfo: MQInfo, addr: str, rpc_port: int, relay_port: int, http_port: int
    ) -> None: ...
    @staticmethod
    def startLocalMQ(cmd: str, log: Callable[[str], object] | None = ...) -> int: ...
    @staticmethod
    def killLocalMQ(pid: int, log: Callable[[str], object] | None = ...) -> None: ...
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
    ) -> str: ...

class SimpleMQSchedulerMixin:
    mqinfo: MQInfo
    mqrelay: PDGNetMQRelay[CallbackServerAPI] | None
    starting_mq: bool
    def __init__(self) -> None: ...
    def getPollingClient(self) -> PDGNPollingClient | None: ...
    def startPollingClient(self) -> None: ...
    def stopPollingClient(self) -> None: ...
    def checkPollingClient(self) -> bool: ...
