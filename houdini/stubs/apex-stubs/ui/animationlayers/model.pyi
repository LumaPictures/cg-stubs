import hou
from _apexscene import AnimLayer as AnimLayer
from collections.abc import Iterable, Mapping, Sequence
from enum import Enum
from hutil.PySide import QtCore, QtGui
from hutil.qt.objecthandle import QtObjectHandle
from typing import ClassVar, Literal, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_WeightChangeType: TypeAlias = Literal['started', 'updated', 'finished']
class _LayerWeightData(TypedDict):
    weight: float
    animated: bool
    keyed: bool

MIME_TYPE: str
ROOT_ITEM_NAME: str
BASE_LAYER_NAME: str
DEFAULT_LAYER_COLOR: hou.Color
ADDITIVE_COLOR: QtGui.QColor
OVERRIDE_COLOR: QtGui.QColor
ADDITIVE_TYPE_TEXT: str
OVERRIDE_TYPE_TEXT: str

class WeightChangeType:
    STARTED: Literal['started']
    UPDATED: Literal['updated']
    FINISHED: Literal['finished']

class Column(Enum):
    NAME = 0
    TYPE = 1
    WEIGHT = 2
    LOCK = 3
    MUTE = 4
    SOLO = 5

class LayerType(Enum):
    OVERRIDE = 0
    ADDITIVE = 1

def toQtColor(color: hou.Color) -> QtGui.QColor: ...
def toHouColor(color: QtGui.QColor) -> hou.Color: ...

class AnimationLayerItem:
    """Item representing a single Animation Layer."""
    icon_size: int
    locked_icon: QtGui.QIcon
    lock_overridden_icon: QtGui.QIcon
    unlocked_icon: QtGui.QIcon
    muted_icon: QtGui.QIcon
    unmuted_icon: QtGui.QIcon
    mute_overridden_icon: QtGui.QIcon
    solo_on_icon: QtGui.QIcon
    solo_off_icon: QtGui.QIcon
    has_controls_icon: QtGui.QIcon
    has_active_controls_icon: QtGui.QIcon
    _parent: AnimationLayerItem | None
    def __init__(self, name: str, muted: bool = False, locked: bool = False, soloed: bool = False, additive: bool = False, color: QtGui.QColor = ..., inherited: bool = False) -> None: ...
    def flags(self, column: int) -> QtCore.Qt.ItemFlag: ...
    def isRoot(self) -> bool:
        """Whether this item is a root item."""
    def isBaseLayer(self) -> bool: ...
    def color(self) -> QtGui.QColor:
        """Return the color of this layer."""
    def setColor(self, color: QtGui.QColor) -> None: ...
    def setName(self, name: str) -> None:
        """Set the name of this layer."""
    def name(self) -> str:
        """Return the name of this layer."""
    def displayLabel(self) -> str:
        """Return the displayed label for this layer."""
    def setInherited(self, inherited: bool) -> None: ...
    def isInherited(self) -> bool: ...
    def descriptionLabel(self) -> str:
        """Return the description for this layer."""
    def enable(self, enabled: bool) -> None:
        """
        Enable or disable this layer. Used when soloing another layer.
        """
    def isEnabled(self) -> bool:
        """
        Return the enabled state of this layer.
        Disabled layers are generally disabled due to another layer being soloed.
        """
    def muted(self) -> bool:
        """Return the mute status of this layer."""
    def setMuted(self, muted: bool) -> None:
        """Set the mute status of this layer."""
    def locked(self) -> bool:
        """Return the lock status of this layer."""
    def setLocked(self, locked: bool) -> None:
        """Set the lock status of this layer."""
    def soloed(self) -> bool:
        """Return the solo status of this layer."""
    def setSoloed(self, soloed: bool) -> None:
        """Set the solo status of this layer."""
    def isAdditive(self) -> bool:
        """Return whether this layer is additive or override."""
    def setAdditive(self, additive: bool) -> None:
        """Set this layer as additive or override."""
    def weight(self) -> float:
        """Return the weight of this layer."""
    def setWeight(self, value: float) -> None:
        """Set the weight of this layer."""
    def setAnimated(self, animated: bool) -> None:
        """Set whether or not the weight of this layer is animated."""
    def animated(self) -> bool:
        """Return whether or not this layer's weight is animated."""
    def setKeyed(self, keyed: bool) -> None:
        """
        Set whether or not the weight of this layer has a key at the current
        frame.
        """
    def keyed(self) -> bool:
        """
        Return whether or not this layer's weight channel has a key at the
        current frame.
        """
    def setHasSelectedControls(self, has_selected_controls: bool) -> None:
        """
        Set whether or not this layer has controls that are selected in the
        scene.
        """
    def hasSelectedControls(self) -> bool:
        """
        Return whether or not this layer has controls that are selected in the
        scene.
        """
    def weightChannelBackgroundColor(self) -> QtGui.QColor:
        """Get the background color for the weight channel input box."""
    def buttonIcon(self, column: Column, disabled: bool) -> QtGui.QIcon | None:
        """Return a button icon for this layer."""
    def parent(self) -> AnimationLayerItem | None:
        """Get the parent item."""
    def setParent(self, parent: AnimationLayerItem | None) -> None:
        """Set the parent item of this item."""
    def childCount(self) -> int:
        """The number of children."""
    def child(self, row: int) -> AnimationLayerItem | None:
        """Get a specific child by its index."""
    def setRow(self, row: int) -> None:
        """Set the index in the parents children list."""
    def row(self) -> int: ...
    def addChild(self, child: AnimationLayerItem) -> None:
        """Add a child to this item."""
    def updateChildRows(self) -> None:
        """Update the stored child row indices."""
    def removeChildByIndex(self, index: int) -> None:
        """Remove a child item by index."""
    def clear(self, keep_persistant: bool = True) -> None:
        """Clear the child items from this item."""

class RootItem(AnimationLayerItem):
    """The hidden root level item."""
    def __init__(self, model: AnimationLayersModel) -> None: ...
    def isRoot(self) -> bool: ...

class AnimationLayersModel(QtCore.QAbstractItemModel):
    """The model used for the Animation Layers Manager."""
    activeLayerUpdated: ClassVar[QtCore.Signal]
    layerWeightUpdated: ClassVar[QtCore.Signal]
    clipsChanged: ClassVar[QtCore.Signal]
    COLOR_ROLE: int
    DESCRIPTION_ROLE: int
    ACTIVE_ROLE: int
    NAME_COLUMN_LABEL: str
    WEIGHT_COLUMN_LABEL: str
    def __init__(self, scene_viewer: hou.SceneViewer | None = None) -> None: ...
    def setClips(self, clips: list[str], active_clip: str) -> None: ...
    def getClips(self) -> list[str]: ...
    def getActiveClip(self) -> str: ...
    def isActive(self) -> bool:
        """
        Returns whether or not this model is active, ie tied to a scene viewer.
        Inactive models cannot be modified.
        """
    def supportedDropActions(self) -> QtCore.Qt.DropAction: ...
    def mimeTypes(self) -> list[str]: ...
    def mimeData(self, indexes: Sequence[QtCore.QModelIndex]) -> QtCore.QMimeData: ...
    def dropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def sceneViewer(self) -> hou.SceneViewer | None: ...
    def flattenLayerTree(self, layers: Mapping[str, AnimLayer], base_layer: str = ...) -> list[AnimLayer]: ...
    def setAllowEditingInheritedLayers(self, allow: bool) -> None: ...
    def isEditingInheritedLayersAllowed(self) -> bool: ...
    def setLayers(self, layers: Mapping[str, AnimLayer], active_layer: str = ...) -> None: ...
    def setLayerWeights(self, weight_data: Mapping[str, _LayerWeightData]) -> None: ...
    def setLayersInherited(self, inherited: Mapping[str, bool]) -> None: ...
    def setLayerControlsIndicators(self, controls_data: Mapping[str, bool]) -> None: ...
    def getHasControlsIcon(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtGui.QIcon | None: ...
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag:
        """Return the flags for an index"""
    def setDefaultLayerType(self, layer_type: LayerType) -> None: ...
    def createLayer(self, name: str | None = None, parent_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> tuple[Literal[True], str] | tuple[Literal[False], None]:
        """Create a new, empty layer."""
    def duplicateLayersByIndex(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None:
        """Duplicate a layer."""
    def bakeLayers(self, replace: bool = True, keys_only: bool = True) -> None:
        """Send a command to the animstate to bake all layers."""
    def mergeLayersByIndices(self, first: QtCore.QModelIndex | QtCore.QPersistentModelIndex, last: QtCore.QModelIndex | QtCore.QPersistentModelIndex, keys_only: bool = True) -> None:
        """Send a command to the animstate to merge the given range of layers."""
    def activeLayerIndex(self) -> QtCore.QModelIndex: ...
    def setActiveLayer(self, layer: str, notify_state: bool = True) -> None:
        """Set the active layer."""
    def isLayerDisabled(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool:
        """
        Returns whether the layer associated with the index is disabled,
        due to being inherited from the input.
        """
    def isLayerActive(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool:
        """
        Return whether or not the item at the given index is the active layer.
        """
    def addSelectedControlsToLayer(self, layer: str) -> None:
        """Tell the animstate to add selected controls to the given layer."""
    def addSelectedControlsToLayers(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None:
        """Tell the animstate to add selected controls to the given layers."""
    def removeSelectedControlsFromLayers(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None:
        """
        Tell the animstate to remove selected controls from the given layers.
        """
    def selectLayerControls(self, layer: str) -> None:
        """
        Tell the animstate to select controls in the given layer.
        """
    def setLayersAdditive(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], additive: bool) -> None: ...
    def forkInheritedLayers(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def setLayersColor(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], color: QtGui.QColor) -> None: ...
    def removeSelectedControlsFromLayerByIndex(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def deleteLayers(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def lockLayers(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], lock: bool) -> None:
        """Toggle the lock state of a list of layers."""
    def muteLayers(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], mute: bool) -> None:
        """Toggle the muted state of a list of layers."""
    def soloLayers(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], solo: bool) -> None:
        """Toggle the muted state of a layer."""
    def setWeight(self, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], value: float, change_type: _WeightChangeType) -> None: ...
    def setWeightKeyframe(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def removeWeightKeyframe(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def addWeightToChannelList(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def resetWeights(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def setWeightFromPlaybarSelection(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def deleteWeightChannels(self, indexes: Iterable[QtCore.QModelIndex | QtCore.QPersistentModelIndex]) -> None: ...
    def columnCount(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> int:
        """Returns the number of columns in the model."""
    def rowCount(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None = ...) -> int:
        """The number of rows in the model rooted under index."""
    def itemFromIndex(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None) -> AnimationLayerItem | None:
        """Get the item from the index."""
    def indexFromLayerName(self, layer: str | None) -> QtCore.QModelIndex: ...
    def parent(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex:
        """Get the parent index from an index."""
    def index(self, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> QtCore.QModelIndex:
        """ Get the index from the row and column and given parent. """
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> str | QtGui.QIcon | QtCore.Qt.AlignmentFlag | None:
        """ Get the header data for the given section. """
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int = ...) -> str | bool | float | QtGui.QColor | QtGui.QIcon | QtCore.Qt.AlignmentFlag | None:
        """Get the data from an index and role."""
    def setData(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, data: str | bool | float | QtGui.QColor, role: int = ...) -> bool:
        """ Set the data at an index. """
    def addChild(self, item: AnimationLayerItem, parent_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> None:
        """ Add a child to the model. """
    def addChildren(self, items: Sequence[AnimationLayerItem], parent_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> None:
        """Add children to the model."""

class AnimationLayersModelHandle(QtObjectHandle[AnimationLayersModel]):
    """ A wrapper class used to hold and manage the life cycle
        of an AnimationLayerModel 
    """
    def __init__(self, *args: hou.SceneViewer | None, **kwargs: hou.SceneViewer | None) -> None: ...
