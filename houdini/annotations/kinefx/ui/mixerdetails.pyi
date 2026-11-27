from collections.abc import Callable
from typing import ClassVar, Literal, TypeAlias

import hou
from hutil.qt.common import config, qmlviews
from kinefx.mixer import Mixer
from PySide6 import QtCore, QtGui, QtQml, QtWidgets

# A field's value: what its getter returns, or its default (str, float or bool).
_FieldValue: TypeAlias = str | int | float

# A parm model's per-field state (its __slots__).
class Field:
    value: _FieldValue
    default: _FieldValue
    locked: bool
    time_dependent: bool
    parm: hou.Parm | None
    # The name of the hou.Parm method that gives the field's value.
    getter: Literal["eval", "evalAsInt", "evalAsString"]
    # Clamps a float field's value (only the clip cut fields have one).
    validator: Callable[["_ParmModel", str, float], float] | None
    signal: QtCore.SignalInstance

# The QObject class _buildParmModelClass() makes: a Qt property and <name>Changed signal per field.
class _ParmModel(QtCore.QObject):
    hasSelectionChanged: ClassVar[QtCore.Signal]
    _node: hou.OpNode | None
    _suffix: str
    _hasSelection: bool
    _fields: dict[str, "Field"]
    _parm_map: dict[str, "Field"]
    def clear(self) -> None: ...
    def updateFromNode(self, node: hou.OpNode, suffix: str) -> None: ...
    def isLocked(self, name: str) -> bool: ...
    def clearExpression(self, name: str) -> None: ...

ClipModel: type[_ParmModel]
TrackModel: type[_ParmModel]

class MixerDetailsState(qmlviews.SharedState[config.BaseConfig]):
    def __init__(
        self,
        *,
        panel: "MixerDetailsPanel | None" = ...,
        clip_model: _ParmModel | None = ...,
        track_model: _ParmModel | None = ...,
        **kwargs: object,
    ) -> None: ...
    def setupEngine(self, engine: QtQml.QQmlEngine, **kwargs: object) -> None: ...

class MixerDetailsQmlWidget(qmlviews.BaseQmlWidget[MixerDetailsState]): ...

class MixerDetailsPanel(QtWidgets.QWidget):
    myPaneTab: hou.PythonPanel | None
    myNode: hou.OpNode | None
    myMixer: Mixer | None
    myClipModel: _ParmModel
    myTrackModel: _ParmModel
    myQmlWidget: MixerDetailsQmlWidget
    def __init__(self, pane_tab: hou.PythonPanel | None) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setNode(self, node: hou.OpNode | None) -> None: ...
    def setActiveTab(self, index: int) -> None: ...
