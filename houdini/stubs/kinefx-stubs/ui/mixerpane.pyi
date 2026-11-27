from kinefx.ui.mixerutils import *
import _houqt
import apex
import hou
from collections.abc import Callable
from hutil.PySide import QtCore, QtGui as QtGui, QtWidgets
from kinefx.mixer import Mixer as Mixer, _MixerNode
from kinefx.mixerfx import _FXDict
from kinefx.ui import mixerpaneactions as mixerpaneactions, mixerpaneevents as mixerpaneevents, mixerpaneinit as mixerpaneinit, mixerpanerebuild as mixerpanerebuild, mixerpaneselection as mixerpaneselection
from kinefx.ui.mixerbake import BakeDialog as BakeDialog
from kinefx.ui.mixercreatenested import BakeToOverrideDialog as BakeToOverrideDialog, CreateNestedDialog as CreateNestedDialog, ExtractNestedDialog as ExtractNestedDialog
from kinefx.ui.mixermatchjoints import MatchJointDialog as MatchJointDialog
from typing import Protocol

from typing import TypeAlias
from collections.abc import Sequence
from typing import Literal
from typing import TypeAlias
_NodeCallbackEntry: TypeAlias = tuple[Literal['node'], hou.OpNode, Sequence[hou.EnumValue[hou.nodeEventType]], hou._NodeEventCallback]
_PlaybarCallbackEntry: TypeAlias = tuple[Literal['playbar'], Callable[[hou.EnumValue[hou.playbarEvent], float], object]]
_DelayedChange: TypeAlias = tuple[Literal['delayedRebuildScene'], None]
class _AnimateState(Protocol):
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def control_manager(self) -> apex.ControlManager: ...
    def runSceneCallbacks(self, update_handle: bool = ..., force: bool = ...) -> None: ...

class MixerPane(QtWidgets.QWidget, mixerpaneinit.MixerPaneInit, mixerpaneactions.MixerPaneActions, mixerpanerebuild.MixerPaneRebuild, mixerpaneevents.MixerPaneEvents, mixerpaneselection.MixerPaneSelection):
    """ The main QWidget for the Houdini Python Panel. The file is split into
        multiple files because the class was getting too large."""
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
    myMenuWidget: QtWidgets.QWidget | None
    myDelayedRebuildNodes: list[_MixerNode | None] | None
    myDelayedRebuildCaller: Callable[[], object] | None
    myDelayedSelection: list[str]
    myTimeline: _houqt.NLE_Timeline
    myTimelineView: _houqt.NLE_QtMotionMixer
    myPathGadget: _houqt.NLE_QtMotionMixerPathGadget
    myMixers: list[Mixer | None] | None
    mixerSelectionUpdated: QtCore.Signal
    @classmethod
    def onCreateInterface(cls, pt: hou.PythonPanel) -> MixerPane:
        """ Entry point to create the widget and link it to a panel."""
    def __del__(self) -> None:
        """ MixerPane.__del__ removes the registered callbacks"""
    myIgnoreFxChanged: bool
    myRequestRefreshAnimateState: bool
    myLastRegisterEffectsIndex: int
    myIsRebuilding: bool
    myCurrentTrackIndex: int
    myCurrentMixerIndex: int
    myIgnoreSelectionChanged: bool
    myDelayedSelectionChanged: bool
    myIgnoreClipChanged: bool
    myFirstResize: bool
    def __init__(self, pt: hou.PythonPanel) -> None:
        """ MixerPane.doinit"""
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def wheelEvent(self, event: QtGui.QWheelEvent) -> None: ...
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        """ Drag enter for the whole panel. Accepts houdini SOP nodes and files. """
    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        """ drop event for the whole panel. Accepts houdini SOP nodes and files. """
    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        """ resize event for the whole panel."""
