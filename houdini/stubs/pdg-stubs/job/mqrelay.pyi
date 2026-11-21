# Houdini stubs generated from Houdini 22.0.466

from pdgjob.pdgmq import *
import queue
import re
from collections.abc import Callable as Callable
from pdg.job.eventdispatch import _Event
from types import TracebackType

ready_reg: re.Pattern[str]
theConnectionAttempts: int
theConnectionAttemptWait: int
theConnectTimeout: float
theRelaySocketTimeout: int

class MQRelay:
    execEvent: Callable[[_Event], str | None]
    relay_error_queue: queue.Queue[tuple[type[BaseException], BaseException, TracebackType | None]]
    @staticmethod
    def parseMQStdout(txt: str) -> tuple[str, int, int] | None: ...
    def __init__(self, execEventFn: Callable[[_Event], str | None]) -> None:
        """
        execEventFn - function to do blocking calls of received
                     events.
        """
    def startRelayServer(self, tracker_host: str, relay_port: int) -> None:
        """
        Start relay thread, the tracker server must be already running
        Raises an exception if we fail to connect before the timeout
        """
    def stopRelayServer(self) -> bool: ...
