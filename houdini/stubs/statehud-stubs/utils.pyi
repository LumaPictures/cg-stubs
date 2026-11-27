import enum
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
import resourceui as rui
import typing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from enum import Enum
from hutil.PySide import QtCore, QtGui, QtWidgets
from statehud.window import HUDWindow as HUDWindow, WidgetBundleWindow as WidgetBundleWindow
from typing import Any, ClassVar, Literal, Never, Protocol, Required, Self
from typing_extensions import TypedDict, Unpack
from viewerhandle.hudmanager import HUDPrefHandler

class _InputFieldKwargs(TypedDict, total=False):
    label: str | None
    size_policy: PySide6.QtWidgets.QSizePolicy | None
    notify_pending_changes: bool
    parent: PySide6.QtWidgets.QWidget | None

class _ResizeGripOptions(TypedDict, total=False):
    parent: PySide6.QtWidgets.QWidget | None
    direction: rui.ResizeDirection
    min_width: int | None
    size: PySide6.QtCore.QSize | None
    constraint_resize: bool

class _ResizeGripKwargs(_ResizeGripOptions, total=False):
    target_widget: Required[PySide6.QtWidgets.QWidget]
    scene_viewer: Required[hou.SceneViewer]

class _AnimBinding(Protocol):
    def channelIsPending(self, scene: _KeyframeScene, channel: str, /) -> bool: ...
    def channelHasKeyframes(self, scene: _KeyframeScene, channel: str, /) -> bool: ...
    def channelHasKeyAtFrame(self, scene: _KeyframeScene, channel: str, frame: float, /) -> bool: ...

class _KeyframeScene(Protocol):
    def getData(self, path: str, /) -> _AnimBinding | None: ...

class _KeyframeState(Protocol):
    @property
    def scene(self) -> _KeyframeScene: ...

class _SliderUpdater(Protocol):
    def __call__(self, *, slider_name: str, value: float, relative: bool) -> object: ...

class _MultiChangeCallback(Protocol):
    def __call__(self, driver_name: str, started: bool, names: list[str] = ..., /) -> object: ...

PIN_NONE: int
PIN_LEFT: int
PIN_RIGHT: int
PIN_TOP_RIGHT: int
PIN_RIGHT_YOFFSET: int
PIN_TOP_RIGHT_YOFFSET: int
PIN_LEFT_YOFFSET: int
PIN_MIN_RESIZE_HEIGHT: int
SUPPORTED_PREFS: tuple[str, str, str, str, str, str, str, str, str, str, str]

class StateHUDPrefHandler(HUDPrefHandler):
    """ Override the HUD Pref Handler to change how some of it works. """
    def __init__(self, hud_mgr: HUDWindow) -> None: ...

class PinManager:
    """ Encapsulate a manager that you add windows to and it
        manages the pinning for these windows so that the windows
        can be aware of each other when pinned and will stack
        properly.
    """
    def __init__(self) -> None: ...
    def addWindow(self, window: HUDWindow) -> None:
        """ Add a window to be managed. """
    def removeWindow(self, window: HUDWindow) -> None:
        """ Remove a window and update pinned positions. """
    def pinUpdated(self, window: HUDWindow, val: int) -> None:
        """ Called by the window when the pin state is updated. """
    def validateWindows(self) -> None:
        """ Remove any dead windows. """
    def updatePinnedPositions(self) -> None:
        """ Update the position of all pinned windows. """
    def onWindowPlacement(self, defer: bool = True) -> None: ...

class PositionCache:
    """ A way to cache the position information for a window
        and apply it to another window.
    """
    pin_state: int
    pos: PySide6.QtCore.QPoint
    def __init__(self, hud_window: HUDWindow) -> None:
        """ Cache the pin and position info from the window. """
    def positionWindow(self, hud_window: HUDWindow) -> None:
        """ Position the other window with the stored info. """

class ResizeGrip(rui.ResizeGrip):
    """ A modified rui.ResizeGrip to add some stuff for telling the
        window where it is being resized. This is needed for pinning.
    """
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Qt override to tell the target widget that we are resizing
            and where.
        """

class HorizontalResizeGrip(ResizeGrip):
    """ A modified rui.ResizeGrip that is meant to have the
        maximal size rather than the minimal size.
    """
    def sizeHint(self) -> PySide6.QtCore.QSize: ...

class DiagResizeGrip(ResizeGrip):
    """ A diagonal resize grip implementation that builds off the
        rui.ResizeGrip.
    """
    height_start: int
    bottom_start: int
    min_height: int
    @typing.overload
    def __init__(self, *args: Unpack[tuple[PySide6.QtWidgets.QWidget, hou.SceneViewer]], **kwargs: Unpack[_ResizeGripOptions]) -> None: ...
    @typing.overload
    def __init__(self, *args: Unpack[tuple[()]], **kwargs: Unpack[_ResizeGripKwargs]) -> None: ...
    def getResizeRegion(self) -> int:
        """ Get the resize region that this grip applies to. """
    def setMinimumHeight(self, height: int) -> None:
        """ Set the minimum height for this widget. """
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Qt override to handle starting the resize, note
            that the super class handles the X resizing,
            we handle only the Y resizing.
        """
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Qt override to have mouse events for the Y part.
            Note that the super class handles the X part of the
            resizing, so we only handle the Y part.
        """

class ColumnRowWidget(QtWidgets.QWidget):
    """ A widget wrapping multiple widgets on a line. """
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, left_widgets: Sequence[PySide6.QtWidgets.QWidget], center_widgets: Sequence[PySide6.QtWidgets.QWidget], right_widgets: Sequence[PySide6.QtWidgets.QWidget]) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """ Make the row maximally wide and minimally tall. """

class MinimalRowWidget(QtWidgets.QWidget):
    """ A widget wrapping multiple widgets on a line. """
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, widgets: Sequence[PySide6.QtWidgets.QWidget | None], stretch_between: bool = False, alignment: PySide6.QtCore.Qt.AlignmentFlag = ..., spacing: int = 0, margins: int = 0) -> None: ...

class RowWidget(MinimalRowWidget):
    """ A widget wrapping multiple widgets on a line. """
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """ Make the row maximally wide and minimally tall. """

class PushButton(QtWidgets.QPushButton):
    """ Light wrapper around QPushButton. """
    def __init__(self, *args: str) -> None: ...

class ButtonStrip(QtWidgets.QWidget):
    """ A wrapper for a simple button strip widget.
        This widget has a number of buttons each togglable,
        and manages unchecking buttons when another button is
        pressed.
    """
    allow_multi_selection: bool
    stateChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, names: list[str], labels: list[str] | None, allow_multi_selection: bool = False, iconpaths: Sequence[str] | None = None, off_iconpaths: Sequence[str | None] | None = None, align_left: bool = False, checkable: bool = True, button_tooltips: Sequence[str] = ...) -> None: ...
    def getButton(self, name: str) -> ToolButton | PushButton | None:
        """ Retrieve a button by name. """
    def setButtonState(self, state: bool, name: str) -> None:
        """ Set the button with given name to state.

            :state: The state of the button. True for clicked,
                False for unclicked.
                If set to True, will unset all other butttons.
            :name: The name of the button to change the state on.
        """
    def getCheckedButton(self) -> str | None:
        """ Get the currently checked button. """
    def getCheckedButtons(self) -> list[str]:
        """ Get the currently checked buttons. """
    def defaultButton(self) -> str: ...
    def resetExclusive(self) -> str: ...
    def resetButtons(self) -> None:
        """ Reset the state of all buttons in the button strip. """

SLIDER_ACTION_SCOPE: str
SLIDER_ACTION_KEY: str
SLIDER_ACTION_REMOVE_KEY: str
SLIDER_ACTION_CLEAR_CHANNEL: str

class SliderContextMenuHandler:
    """
    A handler that lets us bind a context menu to the label
    of a slider.

    For statehuds, we use a custom context menu handler to allow 

    """
    class Proxy:
        """ A proxy object that gets sent when binding the slider that
            properly sets up the context menu handler for this widget.
        """
        def __init__(self, handler: SliderContextMenuHandler, widget_name: str) -> None: ...
        def onContextMenu(self, pos: PySide6.QtCore.QPoint) -> None:
            """ Called when the context menu is requested. """
        def onMousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
            """ Mandatory override. """
        def __call__(self, **kwargs: object) -> Self:
            """ Used to fake calling this object to instantiate it. """
    def __init__(self, panel: WidgetBundleWindow, callback: Callable[[str, str], object] | None = None, show_title: bool = False) -> None: ...
    def showTitle(self) -> bool: ...
    def isMulti(self, widget_name: str) -> bool:
        """ Whether the context menu applies to all selected. """
    def getWidgets(self, driver_name: str) -> list[str]:
        """ Get the full list of sliders to apply the action to. """
    def hasCallback(self) -> bool:
        """ Whether at least one callback is bound. """
    def bindCallback(self, callback: Callable[[str, str], object]) -> None:
        """ Bind an action callback. """
    def bindMultiCallback(self, callback: Callable[[str, list[str]], object]) -> None:
        """ Bind an action callback that responds to multiple widgets. """
    def removeCallback(self, callback: Callable[[str, str], object] | Callable[[str, list[str]], object]) -> None:
        """ Remove an action callback. """

def formatKeyStyleSheet(template: str, background: QtGui.QColor) -> str: ...

class KeyableSlider(rui.SelectableValueField):
    BG_STYLE_SHEET: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def bindKeyframeHandler(self, parms: object = None, channel: tuple[str, str] | None = None, state: _KeyframeState | None = None) -> None:
        """
        Event callback used to bind the keyframe handler and set the keyframe
        event callback.
        """
    def unbindKeyframeHandler(self) -> None:
        """
        Event callback used to unbind the keyframe handler and unset the
        keyframe event callback.
        """
    def onParmChangedEvent(self, kwargs: Mapping[str, object]) -> None:
        """
        Event callback invoked when a bound parm changes.
        """
GroupableSlider = KeyableSlider

class KeyableToggle(rui.CheckBoxWrapper):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def bindKeyframeHandler(self, parms: object = None, channel: tuple[str, str] | None = None, state: _KeyframeState | None = None) -> None:
        """
        Event callback used to bind the keyframe handler and set the keyframe
        event callback.
        """
    def unbindKeyframeHandler(self) -> None:
        """
        Event callback used to unbind the keyframe handler and unset the
        keyframe event callback.
        """
    def onParmChangedEvent(self, kwargs: Mapping[str, object]) -> None:
        """
        Event callback invoked when a bound parm changes.
        """

class SliderGrouping:
    """ Encapsulate the idea of a slider grouping. """
    names: list[str]
    modifiers: PySide6.QtCore.Qt.KeyboardModifier | None
    relative: bool
    def __init__(self, names: list[str], modifiers: PySide6.QtCore.Qt.KeyboardModifier | None = None, relative: bool = True) -> None: ...
    def getNames(self) -> list[str]:
        """ The names in the grouping. """
    def hasModifier(self) -> bool:
        """ Whether the grouping has a modifier key. """
    def isRelative(self) -> bool:
        """ Whether the grouping is relative change. """
    def isModifierPressed(self, modifiers: PySide6.QtCore.Qt.KeyboardModifier | None = None) -> bool:
        """ Whether the modifier key(s) are pressed for this grouping,
            or return true if no modifier keys are assigned.
        """

class VectorWidget(hou.qt.InputField):
    """
    A QWidget for int and float vector parameters (could be extended to support strings).
    """
    min_value: float | None
    max_value: float | None
    mouse_hotkeys: Mapping[tuple[int, int], str] | None
    vectorValueChanged: ClassVar[PySide6.QtCore.Signal]
    vectorHotkeyInvoked: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, data_type: int, num_components: int = 1, min_value: float | None = None, max_value: float | None = None, min_locked: bool | None = False, max_locked: bool | None = False, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, **kwargs: Unpack[_InputFieldKwargs]) -> None: ...
    def setValues(self, values: Sequence[int] | hou._FloatSequence | Sequence[str]) -> None: ...
    def setValue(self, value: float | str | None, index: int = 0) -> None: ...

STEP_SIZES: list[float]
STEP_LABELS: list[str]
STEP_DEFAULT_INDEX: int

class StepSizeButton(QtWidgets.QToolButton):
    """Cycles through step sizes for label drag value changes."""
    stepSizeChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def stepSize(self) -> float: ...

class SliderGroupingManager:
    parent: PySide6.QtWidgets.QWidget
    widget_lookup: Callable[[str], PySide6.QtWidgets.QWidget | None]
    update_slider: _SliderUpdater
    multiChangeCallbacks: list[_MultiChangeCallback]
    def __init__(self, parent: PySide6.QtWidgets.QWidget, widget_lookup: Callable[[str], PySide6.QtWidgets.QWidget | None], update_slider: _SliderUpdater) -> None: ...
    def bindMultiChangeCallback(self, cb: _MultiChangeCallback) -> None: ...
    def removeMultiChangeCallback(self, cb: _MultiChangeCallback) -> None: ...
    def bindSignals(self, name: str, slider: KeyableSlider) -> None: ...
    def getWidget(self, name: str) -> PySide6.QtWidgets.QWidget | None: ...
    def updateSliderValue(self, slider_name: str, value: float, relative: bool = False) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        """
        Qt override for catching key press events.
        This is only used for checking if the modifier
        keys for the grouping change while interacting.
        """
    def keyReleaseEvent(self, event: PySide6.QtGui.QKeyEvent) -> None:
        """
        Qt override for catching key release events.
        This is only used for checking if the modifier
        keys for the grouping change while interacting.
        """
    def beginSliderGrouping(self, driver: str) -> None:
        """
        Begin grouping together driver and the other widgets
        in its grouping.
        """
    def beginSelectedSlidersGrouping(self, driver: str) -> None:
        """ Begin an adhoc grouping with the selected sliders using the driver. """
    def endSliderGrouping(self) -> None:
        """ End a slider grouping. """
    def addSliderGrouping(self, names: list[str], modifier: PySide6.QtCore.Qt.KeyboardModifier | None = None, relative: bool = True, adhoc: bool = False) -> SliderGrouping:
        """
        Add a slider grouping with the given list of names.

        :names: A list of names to add to a grouping.
        :modifer: One of Qt.ShiftModifier, Qt.ControlModifier, or an OR'd
                  combination of them.
        :relative: Whether the grouping applies the relative delta instead of
                   absolute value.
        :adhoc: Whether the grouping is destroyed when it is done being used.
        """
    def removeGrouping(self, name: str) -> None:
        """ Remove a grouping in which name is a part of. """
    def getGrouping(self, driver: str) -> SliderGrouping | None:
        """
        Get the names tied together in the grouping in which driver is
        part of.
        """

class SliderSelectionManager(SliderGroupingManager):
    LABEL_DRAG_DEADZONE: int
    def __init__(self, *args: Unpack[tuple[PySide6.QtWidgets.QWidget, Callable[[str], PySide6.QtWidgets.QWidget | None], _SliderUpdater]], **kwargs: Never) -> None: ...
    def bindSignals(self, name: str, slider: KeyableSlider) -> None: ...
    def removeSlider(self, name: str) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> bool:
        """ Handle clicking on empty space to reset selection. """
    def setLabelDragStepSize(self, step_size: float) -> None: ...
    def selectedSliders(self) -> list[str]:
        """ Get the list of selected sliders. """
    def resetSelectedSliders(self, skip: str | None = None) -> None:
        """ Reset the list of selected sliders. Optionally skipping one. """

class ActionButtonManager:
    DEFAULT_ICON: str
    def __init__(self, name: str, iconpath: str | None, callback: Callable[[bool], object] | None = None, tooltip: str | None = None) -> None: ...
    def button(self) -> ToolButton | None: ...
    def callback(self) -> Callable[[bool], object] | None: ...
    def setupUI(self) -> None: ...

class ToolButton(QtWidgets.QToolButton):
    """ A Tool button with a transparent background and and icon 
    """
    on_icon: PySide6.QtGui.QIcon
    off_icon: PySide6.QtGui.QIcon | None
    DEFAULT_ICON: str
    def __init__(self, *args: PySide6.QtWidgets.QWidget, iconpath: str | None = None, tooltip: str | None = None, icon: PySide6.QtGui.QIcon | None = None, off_iconpath: str | None = None) -> None: ...
    def setChecked(self, on: bool) -> None: ...

class ToolbarWidget(QtWidgets.QWidget):
    component_buttonstrip: None
    names: Sequence[str]
    icons: Sequence[str]
    def __init__(self, names: Sequence[str], icons: Sequence[str]) -> None: ...
    def getButton(self, name: str) -> ToolButton | None: ...

class KeyState(Enum):
    Normal = 0
    Pending = enum.auto()
    Keyed = enum.auto()
    HasKeys = enum.auto()
    def themeColorName(self) -> Literal['PendingColor', 'IsKeyColor', 'IsNotKeyColor'] | None:
        """The UI theme color for this key state, or None for Normal."""
    def parmState(self) -> Literal[0, 4, 5, 7]: ...
    def color(self) -> QtGui.QColor:
        """Background color for this key state."""

class ChannelKeyFrameHandler(QtCore.QObject):
    """ This class provides the support to HUD Handles for 
        adding/removing key frames. HUD handles are notified when 
        a key is added or removed.
    """
    SET_KEY_FRAME: ClassVar[int]
    DEL_KEY_FRAME: ClassVar[int]
    FRAME_CHANGED: ClassVar[int]
    INIT: ClassVar[int]
    keyFrameEvent: ClassVar[PySide6.QtCore.Signal]
    @staticmethod
    def createKey(functions: Iterable[Callable[[], object]]) -> None:
        """ Undoable command for creating keys
        """
    @staticmethod
    def deleteKey(functions: Iterable[Callable[[], object]]) -> None:
        """ Undoable command for deleting keys
        """
    def __init__(self, channel: tuple[str, str] | None = None, state: _KeyframeState | None = None) -> None: ...
    @property
    def scene(self) -> _KeyframeScene | None: ...
    def setChannel(self, channel: tuple[str, str] | None) -> None: ...
    def channel(self) -> tuple[str, str] | None: ...
    def targetBinding(self) -> _AnimBinding | None: ...
    def keyState(self) -> KeyState | None: ...
    def isPending(self) -> bool: ...
    def hasKeyFrames(self) -> bool: ...
    def hasKeyFrame(self, frame: float | None = None) -> bool: ...
    def setKeyFrame(self, function: Callable[[], object] | None = None) -> bool: ...
    def removeKeyFrame(self, function: Callable[[], object] | None = None) -> bool: ...
    def onPlaybarChanged(self, kwargs: Mapping[str, object]) -> None: ...
SliderBound = float | int | list[float] | list[int]

def resolveSliderBounds(bound: SliderBound, num_components: int) -> list[float] | list[int]: ...
