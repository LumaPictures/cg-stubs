import threading
import typing
from rpyc.core.protocol import Connection as Connection
from typing import Any, Literal

def start_server(port: int = 18811, use_thread: bool = True, quiet: bool = True) -> threading.Thread | None: ...

class _RemoteHouAttrWrapper:
    """This class wraps a given HOM attribute.

    If the attribute is called (i.e. method call), then this class first
    ensures that the global time in the remote helper thread is synchronized
    with the global time in the remote main thread.  This guarantees that calls
    like `hou.frame()` and `hou.time()` return the expected time.

    Additionally, after the attribute is called, this class ensures that the
    global time in the remote helper thread is pushed back into the remote main
    thread.  This guarantees that changes from `hou.setFrame()` and
    `hou.setTime()` are propogated to the main global time.
    """
    def __init__(self, remote_hou: Any, attr: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getattribute__(self, name: str) -> Any: ...

@typing.overload
def import_remote_module(server: str = ..., port: int = ..., name: Literal['hou'] = ...) -> tuple[Connection, _RemoteHouAttrWrapper]: ...
@typing.overload
def import_remote_module(server: str = ..., port: int = ..., name: str = ...) -> tuple[Connection, Any]: ...
