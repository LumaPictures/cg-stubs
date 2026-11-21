import _pdgutils
import queue
import re
from collections.abc import Callable as Callable
from pdgjob.pdgnetjson import PDGNetRPCJsonWrapper
from types import TracebackType
from typing import Generic

from typing import TypeVar
from typing import TypeVar
_API = TypeVar('_API')
pdgnet_mqconn_reg: re.Pattern[str]

class PDGNetMQRelay(Generic[_API]):
    relay_error_queue: queue.Queue[tuple[type[BaseException], BaseException, TracebackType] | tuple[None, None, None]]
    callbackServerAPI: _API
    jsonwrapper: PDGNetRPCJsonWrapper
    @staticmethod
    def parseMQStdout(txt: str) -> tuple[str, int, int, int] | None: ...
    def __init__(self, callbackServerAPI: _API, jsonwrapper: Callable[[], PDGNetRPCJsonWrapper] = ...) -> None: ...
    def startLocalMQServer(self, port: int, max_connections: int, tls_cfg: _pdgutils.PDGNetTLSConfig = ...) -> int | _pdgutils.PDGNetError:
        """
        Start local MQ server (i.e. self-mq).
        """
    def startLocalMQHTTP(self, http_rel_path: str = 'result', http_port: int = 0, http_max_connections: int = 128) -> int | _pdgutils.PDGNetError:
        """
        Start the local MQ server's HTTP listener, to support HTTP requests.
        Note that startLocalMQServer() must have already been called to start
        MQ server.
        """
    def connectToMQServer(self, url: str, port: int, client_name: str, polling_time: int, net_timeout: int, max_recv_msgs: int, conn_timeout: float, tls_cfg: _pdgutils.PDGNetTLSConfig = ...) -> int | _pdgutils.PDGNetError:
        """
        Connect to server, with timeout.
        """
    def disconnectFromMQServer(self) -> None:
        """
        Disconnect from a server
        """
    def stopAll(self) -> bool: ...
    def isConnected(self) -> bool: ...
    def isLocalMQRunning(self) -> bool: ...
    def getMQPort(self) -> int: ...
    def getMQHTTPPort(self) -> int: ...
    def getClient(self) -> _pdgutils.PDGNPollingClient | None: ...
