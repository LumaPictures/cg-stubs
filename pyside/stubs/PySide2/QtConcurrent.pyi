import PySide2.QtCore
import _typeshed
import collections
import shiboken2
import typing
T = typing.TypeVar('T')
import typing_extensions

class QFutureQString(shiboken2.Object):
    @typing.overload
    def __init__(self, QFutureQString: QFutureQString) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def cancel(self) -> None: ...
    def isCanceled(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isResultReadyAt(self, resultIndex: int) -> bool: ...
    def isRunning(self) -> bool: ...
    def isStarted(self) -> bool: ...
    def pause(self) -> None: ...
    def progressMaximum(self) -> int: ...
    def progressMinimum(self) -> int: ...
    def progressText(self) -> str: ...
    def progressValue(self) -> int: ...
    def result(self) -> str: ...
    def resultAt(self, index: int) -> str: ...
    def resultCount(self) -> int: ...
    def results(self) -> typing.List[str]: ...
    def resume(self) -> None: ...
    def setPaused(self, paused: bool) -> None: ...
    def togglePaused(self) -> None: ...
    def waitForFinished(self) -> None: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QFutureVoid(shiboken2.Object):
    @typing.overload
    def __init__(self, QFutureVoid: QFutureVoid) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
    def cancel(self) -> None: ...
    def isCanceled(self) -> bool: ...
    def isFinished(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isRunning(self) -> bool: ...
    def isStarted(self) -> bool: ...
    def pause(self) -> None: ...
    def progressMaximum(self) -> int: ...
    def progressMinimum(self) -> int: ...
    def progressText(self) -> str: ...
    def progressValue(self) -> int: ...
    def resultCount(self) -> int: ...
    def resume(self) -> None: ...
    def setPaused(self, paused: bool) -> None: ...
    def togglePaused(self) -> None: ...
    def waitForFinished(self) -> None: ...
    def __copy__(self) -> None: ...

class QFutureWatcherQString(PySide2.QtCore.QObject):
    canceled: typing.ClassVar[PySide2.QtCore.Signal] = ...
    finished: typing.ClassVar[PySide2.QtCore.Signal] = ...
    paused: typing.ClassVar[PySide2.QtCore.Signal] = ...
    progressRangeChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    progressTextChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    progressValueChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    resultReadyAt: typing.ClassVar[PySide2.QtCore.Signal] = ...
    resultsReadyAt: typing.ClassVar[PySide2.QtCore.Signal] = ...
    resumed: typing.ClassVar[PySide2.QtCore.Signal] = ...
    started: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, _parent: PySide2.QtCore.QObject | None = ..., canceled: typing.Callable = ..., destroyed: typing.Callable = ..., finished: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., paused: typing.Callable = ..., progressRangeChanged: typing.Callable = ..., progressTextChanged: typing.Callable = ..., progressValueChanged: typing.Callable = ..., resultReadyAt: typing.Callable = ..., resultsReadyAt: typing.Callable = ..., resumed: typing.Callable = ..., started: typing.Callable = ...) -> None: ...
    def future(self) -> QFutureQString: ...
    def result(self) -> str: ...
    def resultAt(self, index: int) -> str: ...
    def setFuture(self, future: QFutureQString) -> None: ...

class QFutureWatcherVoid(PySide2.QtCore.QObject):
    canceled: typing.ClassVar[PySide2.QtCore.Signal] = ...
    finished: typing.ClassVar[PySide2.QtCore.Signal] = ...
    paused: typing.ClassVar[PySide2.QtCore.Signal] = ...
    progressRangeChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    progressTextChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    progressValueChanged: typing.ClassVar[PySide2.QtCore.Signal] = ...
    resultReadyAt: typing.ClassVar[PySide2.QtCore.Signal] = ...
    resultsReadyAt: typing.ClassVar[PySide2.QtCore.Signal] = ...
    resumed: typing.ClassVar[PySide2.QtCore.Signal] = ...
    started: typing.ClassVar[PySide2.QtCore.Signal] = ...
    staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, _parent: PySide2.QtCore.QObject | None = ..., canceled: typing.Callable = ..., destroyed: typing.Callable = ..., finished: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., paused: typing.Callable = ..., progressRangeChanged: typing.Callable = ..., progressTextChanged: typing.Callable = ..., progressValueChanged: typing.Callable = ..., resultReadyAt: typing.Callable = ..., resultsReadyAt: typing.Callable = ..., resumed: typing.Callable = ..., started: typing.Callable = ...) -> None: ...

class QtConcurrent(shiboken2.Object):
    class ReduceOption:
        OrderedReduce: typing.ClassVar[QtConcurrent.ReduceOption] = ...
        SequentialReduce: typing.ClassVar[QtConcurrent.ReduceOption] = ...
        UnorderedReduce: typing.ClassVar[QtConcurrent.ReduceOption] = ...
        values: typing.ClassVar[dict] = ...
        name: _typeshed.Incomplete
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __and__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> QtConcurrent.ReduceOptions: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __rand__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __ror__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __rxor__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __xor__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...

    class ReduceOptions:
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __and__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __invert__(self) -> QtConcurrent.ReduceOptions: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __rand__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __ror__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __rxor__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...
        def __xor__(self, other: typing.SupportsInt) -> QtConcurrent.ReduceOptions: ...

    class ThreadFunctionResult:
        ThreadFinished: typing.ClassVar[QtConcurrent.ThreadFunctionResult] = ...
        ThrottleThread: typing.ClassVar[QtConcurrent.ThreadFunctionResult] = ...
        values: typing.ClassVar[dict] = ...
        name: _typeshed.Incomplete
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __and__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __pos__(self): ...
        def __radd__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __rand__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __rmul__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __ror__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __rsub__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __rxor__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __sub__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
        def __xor__(self, other: typing.SupportsInt) -> QtConcurrent.ThreadFunctionResult: ...
    OrderedReduce: typing.ClassVar[QtConcurrent.ReduceOption] = ...
    SequentialReduce: typing.ClassVar[QtConcurrent.ReduceOption] = ...
    ThreadFinished: typing.ClassVar[QtConcurrent.ThreadFunctionResult] = ...
    ThrottleThread: typing.ClassVar[QtConcurrent.ThreadFunctionResult] = ...
    UnorderedReduce: typing.ClassVar[QtConcurrent.ReduceOption] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
