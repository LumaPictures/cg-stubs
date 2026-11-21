import queue
import re
import threading
from collections.abc import Callable
from types import TracebackType
from typing import Generic, TypeVar

import _pdgutils
from pdgjob.pdgnetjson import PDGNetRPCJsonWrapper

# The object whose methods the relay calls by name, for the RPCs it receives.
_API = TypeVar("_API")

pdgnet_mqconn_reg: re.Pattern[str]

class PDGNetMQRelay(Generic[_API]):
    relay_error_queue: queue.Queue[
        tuple[type[BaseException], BaseException, TracebackType] | tuple[None, None, None]
    ]
    callbackServerAPI: _API
    jsonwrapper: PDGNetRPCJsonWrapper
    @staticmethod
    def parseMQStdout(txt: str) -> tuple[str, int, int, int] | None: ...
    def __init__(
        self, callbackServerAPI: _API, jsonwrapper: Callable[[], PDGNetRPCJsonWrapper] = ...
    ) -> None: ...
    def startLocalMQServer(
        self, port: int, max_connections: int, tls_cfg: _pdgutils.PDGNetTLSConfig = ...
    ) -> int | _pdgutils.PDGNetError: ...
    def startLocalMQHTTP(
        self, http_rel_path: str = ..., http_port: int = ..., http_max_connections: int = ...
    ) -> int | _pdgutils.PDGNetError: ...
    def connectToMQServer(
        self,
        url: str,
        port: int,
        client_name: str,
        polling_time: int,
        net_timeout: int,
        max_recv_msgs: int,
        conn_timeout: float,
        tls_cfg: _pdgutils.PDGNetTLSConfig = ...,
    ) -> int | _pdgutils.PDGNetError: ...
    def disconnectFromMQServer(self) -> None: ...
    def stopAll(self) -> bool: ...
    def isConnected(self) -> bool: ...
    def isLocalMQRunning(self) -> bool: ...
    def getMQPort(self) -> int: ...
    def getMQHTTPPort(self) -> int: ...
    def getClient(self) -> _pdgutils.PDGNPollingClient | None: ...
