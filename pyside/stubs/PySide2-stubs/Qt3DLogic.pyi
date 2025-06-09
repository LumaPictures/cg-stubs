import PySide2.Qt3DCore
import PySide2.QtCore
import _typeshed
import collections
import shiboken2
import typing
T = typing.TypeVar('T')
import typing_extensions

class Qt3DLogic(shiboken2.Object):
    class QFrameAction(PySide2.Qt3DCore.Qt3DCore.QComponent):
        staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
        triggered: typing.ClassVar[PySide2.QtCore.Signal] = ...
        def __init__(self, parent: PySide2.Qt3DCore.Qt3DCore.QNode | None = ..., addedToEntity: typing.Callable = ..., defaultPropertyTrackingMode: Qt3DLogic.QFrameAction.PropertyTrackingMode = ..., defaultPropertyTrackingModeChanged: typing.Callable = ..., destroyed: typing.Callable = ..., enabled: bool = ..., enabledChanged: typing.Callable = ..., isShareable: bool = ..., nodeDestroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ..., parentChanged: typing.Callable = ..., removedFromEntity: typing.Callable = ..., shareableChanged: typing.Callable = ..., triggered: typing.Callable = ...) -> None: ...

    class QLogicAspect(PySide2.Qt3DCore.Qt3DCore.QAbstractAspect):
        staticMetaObject: typing.ClassVar[PySide2.QtCore.QMetaObject] = ...
        def __init__(self, parent: PySide2.QtCore.QObject | None = ..., destroyed: typing.Callable = ..., objectName: str = ..., objectNameChanged: typing.Callable = ...) -> None: ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
