import PySide6.QtCore
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
import pxr.UsdShade as UsdShade
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.common import IncludedPurposes as IncludedPurposes, Timer as Timer
from typing import Any, Callable, ClassVar

class ChangeNotice(ConstantsGroup):
    INFOCHANGES: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    RESYNC: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class RootDataModel(PySide6.QtCore.QObject):
    __init__: ClassVar[Callable] = ...
    _RootDataModel__OnPrimsChanged: ClassVar[Callable] = ...
    _clearCaches: ClassVar[Callable] = ...
    _emitPrimsChanged: ClassVar[Callable] = ...
    computeBoundMaterial: ClassVar[Callable] = ...
    computeWorldBound: ClassVar[Callable] = ...
    getLocalToWorldTransform: ClassVar[Callable] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    currentFrame: Any
    includedPurposes: Any
    playing: Any
    stage: Any
    useExtentsHint: Any
    def signalPrimsChanged(self, *args, **kwargs) -> Any: ...
    def signalStageReplaced(self, *args, **kwargs) -> Any: ...