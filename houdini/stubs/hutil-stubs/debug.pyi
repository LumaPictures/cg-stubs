# Houdini stubs generated from Houdini 22.0.466

from io import TextIOWrapper

def enableUserSignalHandling(as_daemon: bool = False) -> None:
    """All this program to respond to a SIGUSR1 signal by printing a stack trace
    and launching an interactive Python session.
    
    Note that SIGUSR1 is not available on Windows.
    """

class _BidirectionalNamedPipe:
    in_name: str
    out_name: str
    in_pipe: TextIOWrapper
    out_pipe: TextIOWrapper
    def __init__(self, pid: int, is_process_being_debugged: bool, mode: int = 438) -> None: ...
    def isOpen(self) -> bool: ...
    def write(self, obj: object) -> None: ...
    def read(self) -> str | None: ...
    def close(self) -> None: ...
