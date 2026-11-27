from collections.abc import Callable, Sequence
from typing import Literal, Protocol, TypeAlias

import _houqt
import apex
import hou
from kinefx.mixer import Mixer, _MixerNode
from kinefx.mixerfx import _FXDict
from kinefx.ui.mixerbake import BakeDialog
from kinefx.ui.mixercreatenested import BakeToOverrideDialog, CreateNestedDialog, ExtractNestedDialog
from kinefx.ui.mixermatchjoints import MatchJointDialog
from PySide6 import QtCore, QtGui, QtWidgets

# The Animate viewer state (apexanimate) the pane refreshes after parameter changes.
class _AnimateState(Protocol):
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def control_manager(self) -> apex.ControlManager: ...
    def runSceneCallbacks(self, update_handle: bool = ..., force: bool = ...) -> None: ...

# MixerPane.myCallbacks entries: what removeAllCallbacks() removes.
_NodeCallbackEntry: TypeAlias = tuple[
    Literal["node"], hou.OpNode, Sequence[hou.EnumValue[hou.nodeEventType]], hou._NodeEventCallback
]
_PlaybarCallbackEntry: TypeAlias = tuple[Literal["playbar"], Callable[[hou.EnumValue[hou.playbarEvent], float], object]]
# A postDelayChange() change: (change type, its data).
_DelayedChange: TypeAlias = tuple[Literal["delayedRebuildScene"], None]

class MixerPane:
    mixerSelectionUpdated: QtCore.Signal
    myCallbacks: list[_NodeCallbackEntry | _PlaybarCallbackEntry]
    myLastDelayedTime: float
    myDelayedChanges: list[_DelayedChange]
    myPaneTab: hou.PythonPanel
    myMatchDialog: MatchJointDialog | None
    myCreateNestedDialog: CreateNestedDialog | None
    myBakeToOverrideDialog: BakeToOverrideDialog | None
    myExtractNestedDialog: ExtractNestedDialog | None
    myBakeDialog: BakeDialog | None
    myCurrentAnimateState: _AnimateState | None
    myEffectIcons: dict[str, hou.qt.Icon]
    myNodes: list[_MixerNode | None]
    myRegisterEffects: list[dict[str, _FXDict]]
    # None only until __init__ calls createMenus().
    myMenuWidget: QtWidgets.QWidget | None
    myDelayedRebuildNodes: list[_MixerNode | None] | None
    myDelayedRebuildCaller: Callable[[], object] | None
    myDelayedSelection: list[str]
    myTimeline: _houqt.NLE_Timeline
    myTimelineView: _houqt.NLE_QtMotionMixer
    myPathGadget: _houqt.NLE_QtMotionMixerPathGadget
    # None only until __init__ calls rebuildScene().
    myMixers: list[Mixer | None] | None
    @classmethod
    def onCreateInterface(cls, pt: hou.PythonPanel) -> "MixerPane": ...
    def __init__(self, pt: hou.PythonPanel) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def wheelEvent(self, event: QtGui.QWheelEvent) -> None: ...
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None: ...
    def dropEvent(self, e: QtGui.QDropEvent) -> None: ...
    def resizeEvent(self, e: QtGui.QResizeEvent) -> None: ...
