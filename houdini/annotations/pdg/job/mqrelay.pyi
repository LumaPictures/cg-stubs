import queue
import re
from collections.abc import Callable
from types import TracebackType

from pdg.job.eventdispatch import _Event

ready_reg: re.Pattern[str]
theConnectionAttempts: int
theConnectionAttemptWait: int
theConnectTimeout: float
theRelaySocketTimeout: int

class MQRelay:
    execEvent: Callable[[_Event], str | None]
    relay_error_queue: queue.Queue[
        tuple[type[BaseException], BaseException, TracebackType | None]
    ]
    @staticmethod
    def parseMQStdout(txt: str) -> tuple[str, int, int] | None: ...
    def __init__(self, execEventFn: Callable[[_Event], str | None]) -> None: ...
    def startRelayServer(self, tracker_host: str, relay_port: int) -> None: ...
    def stopRelayServer(self) -> bool: ...
