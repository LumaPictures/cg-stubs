from .common import IncludedPurposes as IncludedPurposes, Timer as Timer
from .qt import QtCore as QtCore
from _typeshed import Incomplete
from pxr import Usd as Usd, UsdGeom as UsdGeom, UsdShade as UsdShade
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup

class ChangeNotice(ConstantsGroup):
    NONE: int
    RESYNC: int
    INFOCHANGES: int

class RootDataModel(QtCore.QObject):
    """Data model providing centralized, moderated access to fundamental
    information used throughout Usdview controllers, data models, and plugins.
    """
    signalStageReplaced: Incomplete
    signalPrimsChanged: Incomplete
    _stage: Incomplete
    _makeTimer: Incomplete
    _currentFrame: Incomplete
    _playing: bool
    _bboxCache: Incomplete
    _xformCache: Incomplete
    _pcListener: Incomplete
    def __init__(self, makeTimer: Incomplete | None = None) -> None: ...
    @property
    def stage(self):
        """Get the current Usd.Stage object."""
    @stage.setter
    def stage(self, value) -> None:
        """Sets the current Usd.Stage object, and emits a signal if it is
        different from the previous stage.
        """
    def _emitPrimsChanged(self, primChange, propertyChange) -> None: ...
    def __OnPrimsChanged(self, notice, sender) -> None: ...
    @property
    def currentFrame(self):
        """Get a Usd.TimeCode object which represents the current frame being
        considered in Usdview."""
    @currentFrame.setter
    def currentFrame(self, value) -> None:
        """Set the current frame to a new Usd.TimeCode object."""
    @property
    def playing(self): ...
    @playing.setter
    def playing(self, value) -> None: ...
    def _clearCaches(self) -> None:
        """Clears internal caches of bounding box and transform data. Should be
        called when the current stage is changed in a way which affects this
        data."""
    @property
    def useExtentsHint(self):
        """Return True if bounding box calculations use extents hints from
        prims.
        """
    @useExtentsHint.setter
    def useExtentsHint(self, value) -> None:
        """Set whether whether bounding box calculations should use extents
        from prims.
        """
    @property
    def includedPurposes(self):
        """Get the set of included purposes used for bounding box calculations.
        """
    @includedPurposes.setter
    def includedPurposes(self, value) -> None:
        """Set a new set of included purposes for bounding box calculations."""
    def computeWorldBound(self, prim):
        """Compute the world-space bounds of a prim."""
    def getLocalToWorldTransform(self, prim):
        """Compute the transformation matrix of a prim."""
    def computeBoundMaterial(self, prim, purpose):
        """Compute the material that the prim is bound to, for the given value
           of material purpose. 
        """
