import hou
from PySide6 import QtGui as QtGui, QtQml as QtQml
from collections.abc import Callable as Callable
from hutil.PySide import QtCore, QtWidgets
from hutil.qt.common import config, qmlviews
from kinefx.mixer import Mixer as Mixer
from typing import ClassVar, Literal

from typing import TypeAlias
from typing import TypeAlias
_FieldValue: TypeAlias = str | int | float
class _ParmModel(QtCore.QObject):
    hasSelectionChanged: ClassVar[QtCore.Signal]
    _node: hou.OpNode | None
    _suffix: str
    _hasSelection: bool
    _fields: dict[str, 'Field']
    _parm_map: dict[str, 'Field']
    def clear(self) -> None: ...
    def updateFromNode(self, node: hou.OpNode, suffix: str) -> None: ...
    def isLocked(self, name: str) -> bool: ...
    def clearExpression(self, name: str) -> None: ...

class Field:
    """Per-field state for a parm model. Holds value, lock state,
    cached parm object, and spec (getter, validator, signal)."""
    value: _FieldValue
    default: _FieldValue
    locked: bool
    time_dependent: bool
    parm: hou.Parm | None
    getter: Literal['eval', 'evalAsInt', 'evalAsString']
    validator: Callable[[_ParmModel, str, float], float] | None
    signal: QtCore.SignalInstance

ClipModel: type[_ParmModel]
TrackModel: type[_ParmModel]

class MixerDetailsState(qmlviews.SharedState[config.BaseConfig]):
    """SharedState that registers Mixer-specific context properties
    (panel, clipModel, trackModel) alongside the standard ones."""
    def __init__(self, *, panel: MixerDetailsPanel | None = None, clip_model: _ParmModel | None = None, track_model: _ParmModel | None = None, **kwargs: object) -> None: ...
    def setupEngine(self, engine: QtQml.QQmlEngine, **kwargs: object) -> None: ...

class MixerDetailsQmlWidget(qmlviews.BaseQmlWidget[MixerDetailsState]):
    """BaseQmlWidget host for MixerDetails.qml; refreshes globalScale on
    showEvent so the QML follows HOUDINI_UISCALE changes."""

class MixerDetailsPanel(QtWidgets.QWidget):
    """Details panel for Motion Mixer selection.
    """
    myPaneTab: hou.PythonPanel | None
    myNode: hou.OpNode | None
    myMixer: Mixer | None
    myClipModel: _ParmModel
    myTrackModel: _ParmModel
    myQmlWidget: MixerDetailsQmlWidget
    myActiveTab: int
    def __init__(self, pane_tab: hou.PythonPanel | None) -> None: ...
    def cleanup(self) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setNode(self, node: hou.OpNode | None) -> None: ...
    def setActiveTab(self, index: int) -> None: ...
    def selectTrackJoints(self) -> None:
        """Launch joint picker for the selected track."""
    def selectBlendParent(self) -> None:
        """Launch joint picker for blend parent."""
    def releaseFocus(self) -> None:
        """Clear QML active focus so Houdini's hotkey system works
        after editing. Qt focus stays on the QQuickWidget so that
        a subsequent Tab still reaches the QML focus chain."""
