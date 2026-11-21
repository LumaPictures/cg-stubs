import hou
import typing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from hutil.PySide import QtCore, QtGui, QtWidgets
from hutil.qt.pluto.parts import ParmState
from typing import ClassVar, Protocol, TypedDict
from viewerhandle.hudapi import HUDWidgetBase as HUDWidgetBase, _HUDHandle
from viewerhandle.hudwindow import HUDWindow as HUDWindow

from typing import TypeVar
from typing import TypeVar
_KwargsT = TypeVar('_KwargsT', bound=Mapping[str, object])
class _KeyFrameEventKwargs(TypedDict, total=False):
    frame: float | None
    color: QtGui.QColor | None

class _RangeHUDWidget(Protocol):
    def handle(self) -> _HUDHandle: ...
    def useParmRange(self) -> int: ...
    def rangeInfo(self, use_parm_range: int) -> Mapping[str, 'RangeInfo']: ...
    def handleRangeInfoChange(self, parm_value: bool, /) -> None: ...

class _OrderedRangeHUDWidget(_RangeHUDWidget, Protocol):
    def orderingInfo(self) -> Mapping[str, int]: ...
    def handleOrderingInfoChange(self, ordering_info: dict[str, int], /) -> None: ...

class SettingDialog(QtWidgets.QDialog):
    """ HUD widget setting dialog base class. Subclass
        to add HUD type-specific options.

        Layout structure
        +----------------------------------------+
         [win bar]
         [title]
         +                                      +
         | +------------------+ | [resize grip] |
         |  [range limit]       |               |
         |  [range locking]     |               |
         | +------------------+ |               |
         +                                      +
         | +------------------+ |               |
         |  [options]                           |
         | +------------------+ |               |
         +                                      +
         [ok] [cancel]
        +----------------------------------------+

    """
    def __init__(self, hud_window: HUDWindow) -> None: ...
    def hud(self) -> HUDWindow: ...
    def onAcceptSettings(self) -> bool: ...
    def onRejectSettings(self) -> None: ...
    def onSetupUI(self) -> None: ...
    def onNewGeometry(self, width: int, height: int, pos: QtCore.QPoint) -> None: ...
    def windowSize(self) -> QtCore.QSize: ...
    def canMove(self) -> bool: ...
    def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def onMouseMoveEvent(self, event: QtGui.QMouseEvent, new_pos: QtCore.QPoint) -> None: ...
    def onMouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
    def setupUI(self) -> None: ...

@dataclass
class RangeInfo:
    """
    Dataclass that holds info on a parameter value range.

    self.valid indicates whether this RangeInfo is
    associated to an existing widget
    """
    valid: bool = ...
    enabled: bool = ...
    index: int = ...
    label: str | None = ...
    min_val: float = ...
    max_val: float = ...
    min_locked: bool = ...
    max_locked: bool = ...
    precision: float = ...

class RangeSettingDialog(SettingDialog):
    """ HUD widget settings dialog used for editing
        range parms, namely min/max limit and
        locking settings.

        THe HUD widget must implement the following methods:

        useParmRange(): indicates whether the custom parm range
            is used

        rangeInfo(): provides a rangeInfo struct mapping for that
            widget's parms

        handleRangeInfoChanged(): callback invoked when the range
            info is updated via the settings dialog
    """
    def __init__(self, hud_widget: _RangeHUDWidget, hud: HUDWindow) -> None: ...
    def buildGridRows(self) -> list[list[QtWidgets.QWidget] | None]:
        """ Called by the base class for building a list of widgets
            required for populating the dialog grid layout.
        """
    def buildOptions(self) -> list[QtWidgets.QCheckBox]:
        """ Called by the base class for creating extra option
            widgets.
        """
    def onSetupUI(self) -> None:
        """ Call by the base class for initializing the dialog
        """
    def onAcceptSettings(self) -> bool:
        """ Update the HUD slider range
        """
    def onSetUseParmRange(self, check_state: int | QtCore.Qt.CheckState) -> None:
        """ If use_parm_range=True, set the range/locking with
            the node parm range or with the HUD range if False.
        """

class OrderedRangeSettingDialog(SettingDialog):
    """ HUD widget settings dialog used for editing
        range parms, namely min/max limit and
        locking settings. Additionally supports specifying
        a sequential ordering of parms via combo boxes.

        THe HUD widget must implement the following methods:

        useParmRange(): indicates whether the custom parm range
            is used

        rangeInfo(): provides a rangeInfo struct mapping for that
            widget's parms

        handleRangeInfoChanged(): callback invoked when the range
            info is updated via the settings dialog

        orderingInfo(): provides ordering info that maps parms
            to ordinals.

        handleOrderingInfoChanged(): callback invoked when the ordering
            info is updated via the settings dialog
    """
    def __init__(self, hud_widget: _OrderedRangeHUDWidget, hud: HUDWindow, ordering_labels: Sequence[str]) -> None: ...
    def buildGridRows(self) -> list[list[QtWidgets.QWidget] | None]:
        """ Called by the base class for building a list of widgets
            required for populating the dialog grid layout.
        """
    def buildOptions(self) -> list[QtWidgets.QCheckBox]:
        """ Called by the base class for creating extra option
            widgets.
        """
    def onSetupUI(self) -> None:
        """ Call by the base class for initializing the dialog
        """
    def onAcceptSettings(self) -> bool:
        """ Update the HUD slider range
        """
    def onSetUseParmRange(self, check_state: int | QtCore.Qt.CheckState) -> None:
        """ If use_parm_range=True, set the range/locking with
            the node parm range or with the HUD range if False.
        """

class KeyFrameHandler(QtCore.QObject):
    """ This class provides the support to HUD Handles for
        adding/removing key frames. HUD handles are notified when
        a key is added or removed.
    """
    SET_KEY_FRAME: int
    DEL_KEY_FRAME: int
    FRAME_CHANGED: int
    INIT: int
    BACKGROUND_COLOR: int
    keyFrameEvent: ClassVar[QtCore.Signal]
    parmStateChanged: ClassVar[QtCore.Signal]
    @staticmethod
    def createKey(functions: Iterable[Callable[[], object]]) -> None:
        """ Undoable command for creating keys
        """
    @staticmethod
    def deleteKey(functions: Iterable[Callable[[], object]]) -> None:
        """ Undoable command for deleting keys
        """
    def __init__(self, parm: hou.Parm, widget: QtWidgets.QWidget, style_sheet: str) -> None: ...
    def term(self) -> None: ...
    def parm(self) -> hou.Parm | None: ...
    def setKeyFrame(self) -> bool: ...
    def removeKeyFrame(self) -> bool: ...
    def hasKeyFrame(self, frame: float | None) -> bool: ...
    def backgroundColor(self) -> QtGui.QColor | None: ...
    def parmState(self) -> ParmState: ...
    def hasPendingChange(self) -> bool: ...
    def commitPendingChange(self, parm_value: float | str, style_sheet: str | None = None) -> None: ...
    def updateWidgetColor(self, frame: float | None, style_sheet: str | None = None) -> bool:
        ''' Update the widget background color for a given widget 
            and style sheet.

            On the old UI: style_sheet is used and must be formatted 
                with a bg_color tag, e.g.
                "background: {bg_color}; color:white; border: 1px solid black"

            On the new UI: the background is applied via QPalette 
                instead.
        '''

def lockUndoTitle(text: str) -> str: ...
def lockParm(hudwidget: HUDWidgetBase, parm: hou.Parm | hou.ParmTuple | None, value: bool) -> None: ...
def lockParmTuple(hudwidget: HUDWidgetBase, parm: hou.Parm | hou.ParmTuple | None, value: bool) -> None: ...
def isParmLocked(parm: hou.Parm | None) -> bool:
    """ Return True if a single parm is locked or all tuple parms
        are locked.
    """
def cursorPos() -> QtCore.QPoint: ...
def winPos(x: int, y: int) -> QtCore.QPoint: ...
@typing.overload
def iterateLayout(layout: QtWidgets.QLayout, callback: Callable[[QtWidgets.QWidget], object], kwargs: None = ...) -> None: ...
@typing.overload
def iterateLayout(layout: QtWidgets.QLayout, callback: Callable[[QtWidgets.QWidget, _KwargsT], object], kwargs: _KwargsT) -> None: ...
