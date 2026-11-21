import asyncio
from typing import Never, Protocol

class _ProcessWatcherOwner(Protocol):
    # Called on the loop's thread when the watched process exits (or the watch is cancelled).
    def _on_result(self, ec: ErrorCode, return_code: int, /) -> object: ...
__version__: str

class CancelError(Exception): ...

class CppErrorCode:
    def __init__(self) -> None:
        """__init__(self: _haio.CppErrorCode) -> None"""
    def assign(self, value: int, category: Never) -> None:
        """assign(self: _haio.CppErrorCode, value: int, category: std::_V2::error_category) -> None"""
    def clear(self) -> None:
        """clear(self: _haio.CppErrorCode) -> None"""
    def __bool__(self) -> bool:
        """__bool__(self: _haio.CppErrorCode) -> bool"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _haio.CppErrorCode, arg0: _haio.CppErrorCode) -> bool"""
    def __lt__(self, other: CppErrorCode) -> bool:
        """__lt__(self: _haio.CppErrorCode, arg0: _haio.CppErrorCode) -> bool"""
    @property
    def category(self) -> str: ...
    @property
    def failed(self) -> bool: ...
    @property
    def message(self) -> str: ...
    @property
    def value(self) -> int: ...

class ErrorCode:
    def __init__(self) -> None:
        """__init__(self: _haio.ErrorCode) -> None"""
    def assign(self, value: int, category: Never) -> None:
        """assign(self: _haio.ErrorCode, value: int, category: hboost::system::error_category) -> None"""
    def clear(self) -> None:
        """clear(self: _haio.ErrorCode) -> None"""
    def __bool__(self) -> bool:
        """__bool__(self: _haio.ErrorCode) -> bool"""
    def __eq__(self, other: object) -> bool:
        """__eq__(self: _haio.ErrorCode, arg0: _haio.ErrorCode) -> bool"""
    def __lt__(self, other: ErrorCode) -> bool:
        """__lt__(self: _haio.ErrorCode, arg0: _haio.ErrorCode) -> bool"""
    @property
    def category(self) -> str: ...
    @property
    def failed(self) -> bool: ...
    @property
    def message(self) -> str: ...
    @property
    def value(self) -> int: ...

class PyAsyncioHandle:
    def __init__(self) -> None:
        """__init__(self: _haio.PyAsyncioHandle) -> None"""
    def cancelled(self) -> bool:
        """cancelled(self: _haio.PyAsyncioHandle) -> bool"""

class PyAsyncioLoop:
    def __init__(self, arg0: asyncio.AbstractEventLoop) -> None:
        """__init__(self: _haio.PyAsyncioLoop, arg0: object) -> None"""

class PyAsyncioTimer:
    def __init__(self) -> None:
        """__init__(self: _haio.PyAsyncioTimer) -> None"""
    def cancel(self) -> None:
        """cancel(self: _haio.PyAsyncioTimer) -> None"""
    def when(self) -> float:
        """when(self: _haio.PyAsyncioTimer) -> float"""

class PyAsyncioTransport:
    def __init__(self) -> None:
        """__init__(self: _haio.PyAsyncioTransport) -> None"""

class PyPIDWatcher:
    def __init__(self, arg0: _ProcessWatcherOwner, arg1: int) -> None:
        """__init__(self: _haio.PyPIDWatcher, arg0: object, arg1: int) -> None"""

class PyReadPipe:
    def __init__(self, arg0: PyAsyncioLoop, arg1: int) -> None:
        """__init__(self: _haio.PyReadPipe, arg0: object, arg1: int) -> None"""

class PyTCPAcceptor:
    def __init__(self, arg0: PyAsyncioLoop) -> None:
        """__init__(self: _haio.PyTCPAcceptor, arg0: object) -> None"""
    @property
    def family(self) -> int: ...
    @property
    def socktype(self) -> int: ...

class PyTCPSocket:
    def __init__(self, arg0: PyAsyncioLoop) -> None:
        """__init__(self: _haio.PyTCPSocket, arg0: object) -> None"""
    @property
    def family(self) -> int: ...
    @property
    def socktype(self) -> int: ...

class PyUDPSocket:
    def __init__(self, arg0: PyAsyncioLoop) -> None:
        """__init__(self: _haio.PyUDPSocket, arg0: object) -> None"""
    @property
    def family(self) -> int: ...
    @property
    def socktype(self) -> int: ...

class PyWritePipe:
    def __init__(self, arg0: PyAsyncioLoop, arg1: int) -> None:
        """__init__(self: _haio.PyWritePipe, arg0: object, arg1: int) -> None"""

def is_boost_broken_pipe(error: ErrorCode) -> bool:
    """is_boost_broken_pipe(error: _haio.ErrorCode) -> bool"""
def is_boost_cancel_error(error: ErrorCode) -> bool:
    """is_boost_cancel_error(error: _haio.ErrorCode) -> bool"""
def is_boost_connection_reset_error(error: ErrorCode) -> bool:
    """is_boost_connection_reset_error(error: _haio.ErrorCode) -> bool"""
def is_boost_eof(error: ErrorCode) -> bool:
    """is_boost_eof(error: _haio.ErrorCode) -> bool"""
def version_info() -> str:
    """version_info() -> str"""
