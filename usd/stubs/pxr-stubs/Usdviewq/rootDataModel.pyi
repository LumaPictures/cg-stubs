# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import pxr.Usd as Usd
import pxr.UsdGeom as UsdGeom
import pxr.UsdShade as UsdShade
import pxr.UsdUtils.constantsGroup
from _typeshed import Incomplete
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq.common import IncludedPurposes as IncludedPurposes, Timer as Timer
from typing import ClassVar

class ChangeNotice(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    INFOCHANGES: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    RESYNC: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class RootDataModel(PySide6.QtCore.QObject):
    signalPrimsChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalStageReplaced: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    currentFrame: Incomplete
    includedPurposes: Incomplete
    playing: Incomplete
    stage: Incomplete
    useExtentsHint: Incomplete
    def __init__(self, makeTimer: Incomplete | None = ...) -> None: ...
    def _RootDataModel__OnPrimsChanged(self, notice, sender): ...
    def _clearCaches(self):
        """Clears internal caches of bounding box and transform data. Should be
                called when the current stage is changed in a way which affects this
                data."""
    def _emitPrimsChanged(self, primChange, propertyChange): ...
    def computeBoundMaterial(self, prim, purpose):
        """Compute the material that the prim is bound to, for the given value
                   of material purpose. 
        """
    def computeWorldBound(self, prim):
        """Compute the world-space bounds of a prim."""
    def getLocalToWorldTransform(self, prim):
        """Compute the transformation matrix of a prim."""
