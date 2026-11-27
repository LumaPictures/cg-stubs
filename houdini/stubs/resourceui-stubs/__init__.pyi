import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
import numpy
import resourceutils as ru
from collections.abc import Callable as Callable, Iterable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from enum import Enum
from hutil.PySide import QtWidgets
from typing import Any, ClassVar, Literal, Protocol, Self, TypeAlias, TypedDict, Unpack

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_LineEditT = TypeVar('_LineEditT', bound=PySide6.QtWidgets.QLineEdit)
_NumT = TypeVar('_NumT', int, float)
PushButtonBase: TypeAlias = PySide6.QtWidgets.QAbstractButton
class _ResourceBrowser(Protocol):
    def resourceType(self) -> hou.EnumValue[hou.resourceType]: ...
    def printMessage(self, msg: str, msg_type: hou.EnumValue[hou.severityType] = ..., immediate: bool = ...) -> None: ...


class _QLabelKwargs(TypedDict, total=False):
    parent: PySide6.QtWidgets.QWidget | None
    f: PySide6.QtCore.Qt.WindowType
    text: str | None
    textFormat: PySide6.QtCore.Qt.TextFormat | None
    pixmap: PySide6.QtGui.QPixmap | None
    scaledContents: bool | None
    alignment: PySide6.QtCore.Qt.AlignmentFlag | None
    wordWrap: bool | None
    margin: int | None
    indent: int | None
    openExternalLinks: bool | None
    textInteractionFlags: PySide6.QtCore.Qt.TextInteractionFlag | None
    hasSelectedText: bool | None
    selectedText: str | None

class _LabelMinSpacerKwargs(_QLabelKwargs, total=False):
    min_size_hint: int | None

class _LabelMaxSpacerKwargs(TypedDict, total=False):
    max_size_hint: int | None

class _LabelEditKwargs(TypedDict, total=False):
    parent: PySide6.QtWidgets.QWidget | None
    text: str | None
    tooltip: str | None
    alignment: PySide6.QtCore.Qt.AlignmentFlag
    bold_font: bool
    width: int | None
    use_max_width: bool
    label_editing: bool

class _QSliderKwargs(TypedDict, total=False):
    parent: PySide6.QtWidgets.QWidget | None
    tickPosition: PySide6.QtWidgets.QSlider.TickPosition | None
    tickInterval: int | None

class _LabelWrapperKwargs(TypedDict, total=False):
    parent: PySide6.QtWidgets.QWidget | None
    f: PySide6.QtCore.Qt.WindowType
    modal: bool | None
    windowModality: PySide6.QtCore.Qt.WindowModality | None
    enabled: bool | None
    geometry: PySide6.QtCore.QRect | None
    frameGeometry: PySide6.QtCore.QRect | None
    normalGeometry: PySide6.QtCore.QRect | None
    x: int | None
    y: int | None
    pos: PySide6.QtCore.QPoint | None
    frameSize: PySide6.QtCore.QSize | None
    size: PySide6.QtCore.QSize | None
    height: int | None
    rect: PySide6.QtCore.QRect | None
    childrenRect: PySide6.QtCore.QRect | None
    childrenRegion: PySide6.QtGui.QRegion | None
    sizePolicy: PySide6.QtWidgets.QSizePolicy | None
    minimumSize: PySide6.QtCore.QSize | None
    maximumSize: PySide6.QtCore.QSize | None
    minimumWidth: int | None
    minimumHeight: int | None
    maximumWidth: int | None
    maximumHeight: int | None
    sizeIncrement: PySide6.QtCore.QSize | None
    baseSize: PySide6.QtCore.QSize | None
    palette: PySide6.QtGui.QPalette | None
    font: PySide6.QtGui.QFont | None
    cursor: PySide6.QtGui.QCursor | None
    mouseTracking: bool | None
    tabletTracking: bool | None
    isActiveWindow: bool | None
    focusPolicy: PySide6.QtCore.Qt.FocusPolicy | None
    focus: bool | None
    contextMenuPolicy: PySide6.QtCore.Qt.ContextMenuPolicy | None
    updatesEnabled: bool | None
    visible: bool | None
    minimized: bool | None
    maximized: bool | None
    fullScreen: bool | None
    sizeHint: PySide6.QtCore.QSize | None
    minimumSizeHint: PySide6.QtCore.QSize | None
    acceptDrops: bool | None
    windowTitle: str | None
    windowIcon: PySide6.QtGui.QIcon | None
    windowIconText: str | None
    windowOpacity: float | None
    windowModified: bool | None
    toolTip: str | None
    toolTipDuration: int | None
    statusTip: str | None
    whatsThis: str | None
    accessibleName: str | None
    accessibleDescription: str | None
    layoutDirection: PySide6.QtCore.Qt.LayoutDirection | None
    autoFillBackground: bool | None
    styleSheet: str | None
    locale: PySide6.QtCore.QLocale | None
    windowFilePath: str | None
    inputMethodHints: PySide6.QtCore.Qt.InputMethodHint | None

class _QWidgetKwargs(_LabelWrapperKwargs, total=False):
    width: int | None

GRIP_ALPHA: float
GRIP_ALPHA_HOVER: float
GRIP_ALPHA_DISABLED: float

def newUI() -> bool | Literal[''] | None: ...
def oldUI() -> bool: ...
def defer(func: Callable[_P, object], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
@contextmanager
def skipHUDStyle() -> Iterator[None]:
    """Context manager: resourceui widgets created inside skip the HUD style."""
def applyHUDStyle(widget: PySide6.QtWidgets.QWidget) -> None: ...
def applyHoloButtonStyle(button: PySide6.QtWidgets.QAbstractButton) -> None:
    """Opt-in: gives a QPushButton or QToolButton the holo/new-UI look
    (transparent background with a bright white outline and hover
    highlight). No-op on the new UI — the HUD QStyle already supplies
    this look."""
def applyHoloComboBoxStyle(combo: PySide6.QtWidgets.QComboBox) -> None:
    """Opt-in: gives a QComboBox the holo/new-UI look (transparent
    background with a subtle white outline). No-op on the new UI."""

class _MessageView(QtWidgets.QTextEdit):
    """ Implements the message console for Viewer Browsers.
    """
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Ignore MMB events to allow Houdini to handle these events
        """
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Ignore MMB events to allow Houdini to handle these events
        """
    def reset(self) -> None: ...
    def appendText(self, txt: str | list[str], severity: hou.EnumValue[hou.severityType] = ..., want_timestamp: bool = False, counter_prefix: bool = True, immediate: bool = False) -> None: ...

def messageView(parent: PySide6.QtWidgets.QWidget | None = None) -> _MessageView:
    """ Returns a text widget for browsers such as the Viewer State
        Browser for displaying messages.
    """

class TraceEventHandlerDialog(QtWidgets.QDialog):
    """ A dialog used by the viewer state and viewer handle browsers
        for enabling the event handlers to use for tracing.
    """
    log_options_group: PySide6.QtWidgets.QButtonGroup
    UNCHECK_LIST: tuple[str, str, str, str]
    def __init__(self, browser: _ResourceBrowser) -> None: ...
    def __del__(self) -> None: ...
    def display(self) -> None:
        """ Initialize and open the dialog.
        """
    def setTraceOption(self, log_option: str) -> None: ...
    def onResourceEvent(self, **kwargs: hou._ResourceEventValue) -> None: ...
    def accept(self) -> None: ...

class PushButton(PushButtonBase):
    """ Custom QToolButton with support for checkable buttons
        with dual icons.
    """
    def __init__(self, action: PySide6.QtGui.QAction, parent: PySide6.QtWidgets.QWidget | None = None, icon_names: list[str] | None = None, size: PySide6.QtCore.QSize | None = None, label: str | None = None, flat: bool = False) -> None: ...
    def action(self) -> PySide6.QtGui.QAction: ...
    def setIcon(self, icon_name: str) -> None: ...
    def setText(self, text: str) -> None: ...
    def setToolTip(self, text: str) -> None: ...
    def setAction(self, action: PySide6.QtGui.QAction) -> None:
        """ Configures the push button with a Qt action.
        """
    def icons(self) -> list[PySide6.QtGui.QIcon]: ...
    def onClickedEvent(self) -> None:
        """ Update the action checked state when the button is
            clicked.
        """
    def onMousePressedEvent(self) -> None:
        """ Update the button with the new icon when the mouse
            is pressed..
        """

RESIZE_TOP_LEFT: int
RESIZE_TOP_RIGHT: int
RESIZE_BOTTOM_LEFT: int
RESIZE_BOTTOM_RIGHT: int
RESIZE_TOP: int
RESIZE_BOTTOM: int
RESIZE_RIGHT: int
RESIZE_LEFT: int

class ResizeDirection(Enum):
    """ Indicates the direction which the widget is resized.
    """
    left = 0
    right = 1

class ResizeGrip(QtWidgets.QLabel):
    """ Qt widget used for resizing a target widget from either the
        left or right of a target widget.

        Note: ResizeGrip expects the target widget to implement this
              method for setting the width:
              onNewGeometry(width, height, pos)
    """
    target_widget: PySide6.QtWidgets.QWidget
    constraint_resize: bool
    grip_size: PySide6.QtCore.QSize
    min_width: int
    mouse_start: PySide6.QtCore.QPoint | None
    width_start: int
    right_start: int
    resizing: bool
    alpha: float
    origin: PySide6.QtCore.QPoint | None
    visual_size: int
    color_options: ru.ColorOptions
    resize_direction: ResizeDirection
    target_origin: PySide6.QtCore.QPoint | int
    DEFAULT_MIN_WIDTH: int
    def __init__(self, target_widget: PySide6.QtWidgets.QWidget, scene_viewer: hou.SceneViewer, parent: PySide6.QtWidgets.QWidget | None = None, direction: ResizeDirection = ..., min_width: int | None = None, size: PySide6.QtCore.QSize | None = None, constraint_resize: bool = True) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def setSize(self, w: int, h: int) -> None: ...
    def visualSize(self) -> int: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def getResizeRegion(self) -> int: ...
    def paintEvent(self, paint_event: PySide6.QtGui.QPaintEvent) -> None: ...
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...

class HoverWidget(QtWidgets.QWidget):
    """
    A Qt widget that just tracks when it is hovered and
    emits when the hover changes.
    """
    hovered: ClassVar[PySide6.QtCore.Signal]
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None:
        """ Qt override when the mouse enters the widget. """
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Qt override when the mouse leaves the widget. """

class ResizeFrame(QtWidgets.QFrame):
    """
    A frame that tracks when the border is hovered, and changes the mouse cursor,
    and highlights the border, and when the border is pressed,
    starts resizing the widget.
    """
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    def __init__(self, parent: PySide6.QtWidgets.QWidget, scene_viewer: hou.SceneViewer, layout: PySide6.QtWidgets.QLayout, line_width: int = 4, hover_col: tuple[float, float, float, float] | None = None, rest_col: tuple[float, float, float, float] | None = None, min_width: int | None = None, min_height: int | None = None) -> None: ...
    def setResizeEnabled(self, val: bool) -> None:
        """ Set whether resizing is enabled. """
    def isResizeEnabled(self) -> bool:
        """ Whether resizing of the frame is enabled. """
    def onHoverInner(self, val: bool) -> None:
        """ Callback when the hover of the inner container changes. """
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None:
        """ Qt override when the mouse enters the widget. """
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Qt override when the mouse leaves the widget."""
    def getResizeRegion(self, pos: PySide6.QtCore.QPoint) -> int | None:
        """ Get the region on the resize frame. This tells it
            which way we are resizing.
        """
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Qt override for when mouse is pressed. """
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Qt override when the mouse is released. """
    def isResizing(self) -> bool:
        """ Whether we have an active resize region.
            NOTE: You should also check if the mouse is down.
        """
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Qt override on mouse move event. """
    def getBorderColor(self) -> tuple[float, float, float, float]:
        """ Get the border color, we change the color when it is hovered. """
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        """ Qt override to paint the frame. We are using this to draw the
            border.
        """

TAB_BG_ALPHA: float
TAB_DISABLED_BG_ALPHA: float
TAB_SELECTED_ALPHA: float

class _NewUITabBarBase(QtWidgets.QTabBar):
    """Base class for new UI tab bars (horizontal and vertical).

    Subclasses provide:
      _tabPath(rect, index, count, rad) -> QPainterPath
      _stripBg(palette, bg) -> QColor|None  (None = no strip fill)
      _unselColor(palette, bg) -> QColor
      _drawText(painter, rect, text)
    """

class NewUIHorizontalTabBar(_NewUITabBarBase):
    """Horizontal tab bar for the new UI style.
    Rounded top-left on first tab, top-right on last tab."""
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None, compact: bool = False) -> None: ...
    def setSelectedPillStyle(self, on: bool) -> None:
        """When enabled, the currently selected tab is drawn as a pill
        (fully rounded) instead of inheriting the first/last/middle shape.
        Useful for nested/embedded tab bars to differentiate them from
        outer tabs."""
    def tabSizeHint(self, index: int) -> PySide6.QtCore.QSize: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

class NewUIVerticalTabBar(_NewUITabBarBase):
    """Vertical tab bar for the new UI style.
    Rounded outer corners for East/West positions, rotated text."""
    def tabSizeHint(self, index: int) -> PySide6.QtCore.QSize: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

class VerticalTabBar(QtWidgets.QTabBar):
    """ Tab bar with properly rotated text for vertical tab positions (old UI).

    Qt's stylesheet engine does not rotate tab text for West/East positions,
    so we handle sizing and painting ourselves. Text colors are derived from
    the parent TabWidget's label_color.
    """
    def tabSizeHint(self, index: int) -> PySide6.QtCore.QSize: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

class TabWidget(QtWidgets.QTabWidget):
    """ Used for Tab Widgets. """
    name: str
    label_color: PySide6.QtGui.QColor
    tab_bg: hou.Vector4 | tuple[float, float, float, float]
    tab_disabled_bg: hou.Vector4 | tuple[float, float, float, float]
    tab_sel_bg: tuple[float, float, float, float]
    def __init__(self, parent: PySide6.QtWidgets.QWidget, name: str, scene_viewer: hou.SceneViewer | None = None, tab_position: PySide6.QtWidgets.QTabWidget.TabPosition | None = None, tab_align_end: bool = False, compact_horizontal_tabs: bool = True, custom_style: bool = False) -> None: ...
    def rebuildWithPosition(self, tab_position: PySide6.QtWidgets.QTabWidget.TabPosition) -> TabWidget:
        """Create a new TabWidget with a different tab position and move
        all tab pages into it.  Returns the new widget (caller must swap
        it into the layout / widget registry)."""
    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        """
        Fix for after Qt6.5.1 so that it doesn't end up
        cutting off all tabs before the current index.

        A similar issue is described here https://bugreports.qt.io/browse/QTBUG-115109

        For reference the issue is located in QTabBarPrivate::makeVisible which
        in Qt6.5.1+ now will check the scroll rect with the offsets of the tabs
        and scroll right to ensure the current tab is visible.

        If we clear the size, then the minimum size is 0 initially and the rect
        is not yet updated at that point so it always cuts off before the
        current index.

        We can fix it for now by setting the current index to 0 before the
        QTabBarPrivate::makeVisible call and setting it back afterward.
        """
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> bool | None:
        """ Qt override to disable arrow keys. """
    def setSelectedPillStyle(self, on: bool) -> None:
        """When enabled (and custom_style=True horizontal), draws the
        selected tab as a pill. Useful for nested/embedded tab widgets."""
    def setVisualSize(self, visual_size: int) -> None: ...
    def onUpdateLabelColor(self, val: PySide6.QtGui.QColor) -> None:
        """ Callback for updating label color from prefs. """

class FolderWidgetInner(QtWidgets.QWidget):
    """ Inner pane for the TabWidgetTab which is a scroll area. """
    vbox: PySide6.QtWidgets.QVBoxLayout
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None) -> None: ...

class FolderWidget(FolderWidgetInner):
    name: str
    scene_viewer: hou.SceneViewer
    widgets: dict[str, PySide6.QtWidgets.QWidget]
    def __init__(self, folder_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def addWidget(self, widget: PySide6.QtWidgets.QWidget, widget_name: str) -> None: ...
    def removeWidget(self, widget_name: str) -> None: ...

class CollapsibleFolderWidget(QtWidgets.QWidget):
    """ A folder widget with a clickable header that collapses/expands content. """
    name: str
    scene_viewer: hou.SceneViewer
    widgets: dict[str, PySide6.QtWidgets.QWidget]
    def __init__(self, folder_name: str, label: str, scene_viewer: hou.SceneViewer, label_width: int | None = None, collapsed: bool = False) -> None: ...
    @property
    def vbox(self) -> PySide6.QtWidgets.QVBoxLayout: ...
    def setCollapsed(self, collapsed: bool) -> None: ...
    def isCollapsed(self) -> bool: ...
    def setLabel(self, label: str) -> None: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def addWidget(self, widget: PySide6.QtWidgets.QWidget, widget_name: str) -> None: ...
    def removeWidget(self, widget_name: str) -> None: ...
    def onUpdateLabelColor(self, col: PySide6.QtGui.QColor) -> None: ...
    def onUpdateShadowEffectState(self, val: bool) -> None: ...

class TabWidgetTabNoScroll(FolderWidgetInner):
    tab_name: str
    scene_viewer: hou.SceneViewer
    widgets: dict[str, PySide6.QtWidgets.QWidget]
    metadata: dict[str, str | None]
    def __init__(self, tab_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def getTitleMetadata(self) -> str | None: ...
    def setTitleMetadata(self, title: str | None) -> None: ...
    def resetMetadata(self) -> None: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def addWidget(self, widget: PySide6.QtWidgets.QWidget, widget_name: str) -> None: ...
    def removeWidget(self, widget_name: str) -> None: ...

TAB_TITLE_METADATA: str
SCROLL_ALPHA_REST: float
SCROLL_ALPHA_HOVER: float

def formatColorRGBA(col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor, factor: float = 1.0) -> str: ...

class TabWidgetTab(QtWidgets.QScrollArea):
    """ Widget used for pane tabs in a TabWidget. """
    tab_name: str
    scene_viewer: hou.SceneViewer
    inner_widget: FolderWidgetInner
    widgets: dict[str, PySide6.QtWidgets.QWidget]
    metadata: dict[str, str | None]
    def __init__(self, tab_name: str, scene_viewer: hou.SceneViewer, custom_style: bool = False) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> bool | None:
        """ Qt override to disable arrow keys. """
    def getTitleMetadata(self) -> str | None: ...
    def setTitleMetadata(self, title: str | None) -> None: ...
    def resetMetadata(self) -> None: ...
    @property
    def vbox(self) -> PySide6.QtWidgets.QVBoxLayout: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def minimumSizeHint(self) -> PySide6.QtCore.QSize: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def addWidget(self, widget: PySide6.QtWidgets.QWidget, widget_name: str) -> None: ...
    def removeWidget(self, widget_name: str) -> None: ...

class LabelMinSpacer(QtWidgets.QLabel):
    min_size_hint: int
    def __init__(self, *args: str | PySide6.QtWidgets.QWidget | PySide6.QtCore.Qt.WindowType | None, **kwargs: Unpack[_LabelMinSpacerKwargs]) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def label(self) -> Self: ...

class LabelMaxSpacer(QtWidgets.QLabel):
    max_size_hint: int
    def __init__(self, *args: str | PySide6.QtWidgets.QWidget | PySide6.QtCore.Qt.WindowType | None, **kwargs: Unpack[_LabelMaxSpacerKwargs]) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def label(self) -> Self: ...

class HUDWidgetWrapper(QtWidgets.QWidget):
    """ A wrapper around a widget that adds specific functions
        needed to work with the HUD window, and to properly align
        the widgets in the window.
    """
    def __init__(self, *args: PySide6.QtWidgets.QWidget | None, widget: PySide6.QtWidgets.QWidget | None = None, tooltip: str | None = None, label: str | None = None, right_label: str | None = None, label_width: int | None = None, centered: bool = False, create_widget_shadow: bool = True, action_button: PySide6.QtWidgets.QWidget | None = None, expanding: bool = False, toggle_callback: Callable[[int], object] | None = None) -> None: ...
    def frontLabel(self) -> LabelMinSpacer | SliderLabel | None: ...
    def backLabel(self) -> LabelEdit | LabelMinSpacer | None: ...
    def getWidget(self) -> PySide6.QtWidgets.QWidget | None:
        """ Get the wrapped widget. """
    def actionButton(self) -> PySide6.QtWidgets.QWidget | None: ...
    def toggle(self) -> PySide6.QtWidgets.QCheckBox | None: ...
    def onUpdateShadowEffectState(self, val: bool) -> None:
        """ Callback for updating shadow effect from prefs. """
    def onUpdateLabelColor(self, val: PySide6.QtGui.QColor) -> None:
        """ Callback for updating label color from prefs. """
    def setVisualSize(self, visual_size: int) -> None:
        """ Needed for HUD Window integration. """
    def visualSize(self) -> int:
        """ Needed for HUD Window integration. """
    def sizeHint(self) -> PySide6.QtCore.QSize:
        """ Qt override for sizing of widget. """
    def eventFilter(self, source: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool:
        """ Catch enter events and show the tooltip. """

class ToggleWidget(QtWidgets.QCheckBox):
    """ Implement the HUD toggle checkbox for key frame support.
        Style sheets are normally used in the old UI for changing 
        a widget background color, but for QCheckBox, style sheets 
        don't work as it breaks the drawing of the indicator.
    """
    mouse_hotkeys: Mapping[tuple[int, int], str] | None
    hotkeyInvoked: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, label: str, parent: PySide6.QtWidgets.QWidget | None = None, callback: Callable[[bool], object] | None = None, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Support for animation keying.
        """
    def setBackgroundColor(self, color: PySide6.QtGui.QColor | PySide6.QtCore.Qt.GlobalColor | None) -> None: ...
    def setParmState(self, state: int) -> None: ...
    def backgroundColor(self) -> PySide6.QtGui.QColor | PySide6.QtCore.Qt.GlobalColor: ...
    def setHovered(self, val: bool) -> None: ...
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

class CheckBoxWrapper(HUDWidgetWrapper):
    """
    Wrapper for a checkbox with a label spacer in front and a right label as a
    LabelEdit that supports colouring and drop shadows.
    """
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, label: str | None, front_label: str | None = None, tooltip: str | None = None, label_width: int | None = None, centered: bool = False, create_widget_shadow: bool = True, callback: Callable[[bool], object] | None = None, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None) -> None: ...
    def isWidgetLabel(self, source: PySide6.QtCore.QObject) -> bool | None: ...
    def eventFilter(self, source: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...

class ComboBoxExclusiveGroup:
    """
    Grouping of combo boxes that enforces mutually exclusive
    selections.

    Assumes items are in the same order since checks are made
    by-index.
    """
    def __init__(self) -> None: ...
    def addCombobox(self, combobox: PySide6.QtWidgets.QComboBox) -> None:
        """Add a new combobox to the exclusive group."""
    def comboboxUpdated(self, target: PySide6.QtWidgets.QComboBox) -> None:
        """Slot invoked when any of the comboboxes are updated."""

class WindowBar(QtWidgets.QLabel):
    """ Widget used as a window bar for HUD windows. The widget is also
        used for moving the HUD window interactively.
    """
    alpha: float
    grip_size: PySide6.QtCore.QSize
    color_options: ru.ColorOptions
    target_widget: PySide6.QtWidgets.QWidget
    target_origin: PySide6.QtCore.QPoint | None
    target_boundary: PySide6.QtCore.QRect | None
    start_offset: PySide6.QtCore.QPoint
    start_pos: PySide6.QtCore.QPoint | None
    prev_pos: PySide6.QtCore.QPoint | None
    roffset: int | None
    loffset: int | None
    toffset: int | None
    boffset: int | None
    def __init__(self, target_widget: PySide6.QtWidgets.QWidget, scene_viewer: hou.SceneViewer, target_origin: PySide6.QtCore.QPoint | None = None, target_boundary: PySide6.QtCore.QRect | None = None, size: PySide6.QtCore.QSize | None = None, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def setSize(self, w: int, h: int) -> None: ...
    def recomputeOriginAndBounds(self) -> None:
        """ Recompute the self.target_origin and self.target_boundary
            members which tell the window bar where the viewport window
            is and where its boundaries are in relation.

            These values must be set to the correct values before dragging
            the window, or else the window will not be correctly
            constrained to the viewport.

            It is recommended that this is called whenever the parent
            viewport resizes or is moved.
        """
    def setCompactState(self, value: bool) -> None: ...
    def visualSize(self) -> int: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Compute a delta position from the previous mouse position
        """
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def paintEvent(self, paint_event: PySide6.QtGui.QPaintEvent) -> None: ...
    def backgroundColor(self) -> tuple[float, float, float, float]: ...

class LabelEdit(QtWidgets.QWidget):
    """ Edit/Label widget combo for editing a label.
    """
    textChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: Unpack[_LabelEditKwargs]) -> None:
        """ Available options (default):
            text: Label text (None)
            tooltip: Tooltip string (None)
            alignment: Qt alignment (Qt.AlignCenter|Qt.AlignVCenter)
            bold_font: Draw text in bold (True)
            width: Label width (None)
            use_max_width: Set the label/line edit maximum width (False)
            label_editing: Enable editing (False)
        """
    def toolTip(self) -> ToolTip: ...
    def label(self) -> PySide6.QtWidgets.QLabel: ...
    def enterEvent(self, event: PySide6.QtGui.QEnterEvent) -> None:
        """ Display tooltip when the mouse enters. The tooltip won't
            show up in edit mode or if the widget is disabled.
        """
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def visualSize(self) -> int: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def setCompactState(self, value: bool) -> None: ...
    def text(self) -> str: ...
    def setText(self, text: str | None) -> None: ...
    def setTextColor(self, color: PySide6.QtGui.QColor) -> None: ...
    def setColors(self, text_color: PySide6.QtGui.QColor, bg_color: PySide6.QtGui.QColor) -> None: ...
    def onHandleTextChange(self, text: str) -> None: ...
    def eventFilter(self, watched: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...

class ToolTip:
    """ ToolTip class to show a tooltip with a delay.
    """
    DELAY: int
    def __init__(self, text: str | None = None, delay: int | None = None) -> None: ...
    def setText(self, text: str | None) -> None: ...
    def hide(self) -> None: ...
    def show(self, pos: PySide6.QtCore.QPoint) -> None: ...
    def enable(self, value: bool) -> None: ...
    def canShow(self) -> bool: ...

def styledEdit(w: _LineEditT, size: int = 0) -> _LineEditT: ...
def styledLabel(text: str, size: int = 0, bold: bool = False, italic: bool = False, wrap: bool = False, alignment: PySide6.QtCore.Qt.AlignmentFlag | None = None) -> PySide6.QtWidgets.QLabel: ...

class UI:
    VISUAL_SIZE_XSMALL: int
    VISUAL_SIZE_SMALL: int
    VISUAL_SIZE_MEDIUM: int
    VISUAL_SIZE_LARGE: int
    LAYOUT_HORIZ_MARGINS: list[int]
    LAYOUT_VERT_MARGINS: list[int]
    LAYOUT_HSPACE_SIZES: list[int]
    GRIP_HEIGHT_RATIOS: list[float]
    GRIP_WIDTHS: list[int]
    LABEL_FONT_SIZES: list[int]
    LABEL_WIDTH_SIZES: list[int]
    VALUE_WIDTH_SIZES: list[int]
    WIDGET_HEIGHTS: list[int]
    SLIDER_VALUE_SIZES: list[int]
    SLIDER_LABEL_SIZES: list[int]
    SLIDER_HORIZ_GROOVE_SIZES: list[int]
    SLIDER_HORIZ_GROOVE_HEIGHTS: list[int]
    SLIDER_HORIZ_HANDLE_WIDTHS: list[int]
    PROPORTIONAL: str
    class __UI:
        SIZE2: int
        SIZE4: int
        SIZE5: int
        SIZE6: int
        SIZE8: int
        SIZE10: int
        SIZE12: int
        SIZE14: int
        SIZE16: int
        SIZE18: int
        SIZE22: int
        SIZE24: int
        SIZE26: int
        SIZE28: int
        SIZE30: int
        SIZE32: int
        SIZE100: int
        BTN_SIZE: int
        MARGIN2: PySide6.QtCore.QMargins | None
        MARGIN4: PySide6.QtCore.QMargins | None
        MARGIN8: PySide6.QtCore.QMargins | None
        MARGIN12: PySide6.QtCore.QMargins | None
        def __init__(self) -> None: ...
        def setShadowEffect(self, widget: PySide6.QtWidgets.QWidget, enable: bool = True) -> PySide6.QtWidgets.QGraphicsDropShadowEffect: ...
        def labelFontSize(self, visual_size: int) -> int: ...
        def labelWidthSize(self, visual_size: int) -> int: ...
        def labelFixedWidth(self) -> int: ...
        def layoutSpacingFixedWidth(self) -> int: ...
        def valueWidthSize(self, visual_size: int) -> int: ...
        def widgetHeightSize(self, visual_size: int) -> int: ...
        def gripHeight(self, visual_size: int) -> float: ...
        def gripWidth(self, visual_size: int) -> int: ...
        def sliderLabelWidth(self, visual_size: int) -> int: ...
        def sliderValueWidth(self, visual_size: int) -> int: ...
        def sliderHGrooveWidth(self, visual_size: int) -> int: ...
        def layoutHMargin(self, visual_size: int) -> int: ...
        def layoutVMargin(self, visual_size: int) -> int: ...
        def layoutHSpaceSize(self, visual_size: int) -> int: ...
        def defaultVisualSize(self) -> int: ...
        def defaultFontFamily(self) -> str: ...
        def margin(self, factor: int = 1) -> int: ...
        def cornerRoundness(self) -> int: ...
        def lockedRgb(self) -> int: ...
        def disabledColor(self) -> PySide6.QtGui.QColor: ...
        def textColor(self) -> PySide6.QtGui.QColor: ...
        def tickmarkColor(self) -> PySide6.QtGui.QColor: ...
        def selectedBgColor(self) -> PySide6.QtGui.QColor: ...
        def pressedBgColor(self) -> PySide6.QtGui.QColor: ...
        def hoveredBgColor(self) -> PySide6.QtGui.QColor: ...
        def tickmarkTopY(self) -> int: ...
        def tickmarkHeight(self) -> int: ...
        def checkmarkColor(self) -> PySide6.QtGui.QColor: ...
        def lockedHEXColor(self) -> str: ...
        def valueStyleSheet(self) -> str: ...
        def labelStyleSheet(self, color: PySide6.QtGui.QColor = ...) -> str: ...
        def bgLabelStyleSheet(self, text_color: PySide6.QtGui.QColor = ..., bg_color: PySide6.QtGui.QColor = ...) -> str: ...
        def pushButtonStyleSheet(self) -> str: ...
        def comboBoxStyleSheet(self) -> str: ...
        def checkBoxStyleSheet(self) -> str: ...
        def sliderPadding(self) -> int: ...
        def sliderStyleSheet(self) -> str: ...
        def tabWidgetStyleSheet(self, label_col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor, bg_col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor, disabled_bg_col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor, select_bg_col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor, tab_position: PySide6.QtWidgets.QTabWidget.TabPosition | None = None, tab_align_end: bool = False) -> str: ...
        def tabWidgetTabStyleSheet(self, rest_col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor, hover_col: Sequence[float] | hou.Vector4 | PySide6.QtGui.QColor) -> str: ...
        def setForegroundColor(self, widget: PySide6.QtWidgets.QWidget, color: PySide6.QtGui.QColor) -> None: ...
    instance: UI.__UI | None
    def __new__(cls) -> UI.__UI: ...
    def __getattr__(self, name: str) -> Any: ...

def mapValueToSlider(slider: SliderBase, value: float, value_min: float, value_max: float) -> numpy.float64: ...
def mapSliderToValue(slider: SliderBase, value: float, value_min: float, value_max: float) -> numpy.float64: ...
def clampInt32(value: _NumT) -> _NumT | int:
    """
    Clamps an integer to within the 32-bit signed range.
    """
def clampFloat64Exp(value: float) -> float:
    """
    Clamps an exponent within the 64-bit float base-10 exponent range.
    """

class SliderBase(QtWidgets.QSlider):
    """ Base class for HUD sliders mostly for handling mouse events.
    """
    TYPE: type[float] | type[int]
    def __init__(self, *args: PySide6.QtCore.Qt.Orientation | PySide6.QtWidgets.QWidget | None, **kwargs: Unpack[_QSliderKwargs]) -> None: ...
    def event(self, event: PySide6.QtCore.QEvent) -> bool: ...
    def leaveEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def precision(self) -> int:
        """
        Retrieves slider precision.
        """
    def emitValueChanged(self, value: float) -> None: ...
    def updateFromHandle(self, value: int) -> float:
        """ Update the slider following a handle interaction. Note that the
            value is clamped to the slider limits only when they are locked.
        """
    def updateFromValue(self, value: float, allow_off_bound: bool = False, update_slider_position: bool = False) -> float | None:
        """ Update the slider value directly. E.g., this method is called when
            the corresponding parm is updated by an external source. Note that
            the value is clamped to the slider limits only when they are locked.

            allow_off_bound:
            When True, the value can be set beyond the limits, ignoring locks.

            update_slider_position:
            Indicates whether the slider's handle position should be updated to
            reflect the new value.
        """
    def intValue(self, value: float) -> int | None: ...
    def toTypeValue(self, value: float) -> float | None: ...
    def minimumLocked(self) -> bool: ...
    def maximumLocked(self) -> bool: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Make the slider handle jump to the mouse position.
        """
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Allow the slider handle to follow the mouse position.
            Set the value to make sure a signal is emitted.
        """
    def minimum(self) -> int | None: ...
    def setMinimum(self, value: float) -> None:
        """ Set the minimum value. Block signals to avoid resetting the
            slider if the new min is > slider value and the min limit
            is off.
        """
    def maximum(self) -> int | None: ...
    def setMaximum(self, value: float) -> None:
        """ Set the maximum value. Block signals to avoid resetting the
            slider if the new max is < slider value and the max limit
            is off.
        """
    def setTickmarkColor(self, color: PySide6.QtGui.QColor) -> None: ...

class FloatSlider(SliderBase):
    """ The class provides a QSlider implementation for controlling
        bound and unbound float values with a default precision
        factor of 3 digits.
    """
    sliderChanged: ClassVar[PySide6.QtCore.Signal]
    TYPE = float
    DECIMALS: int
    @staticmethod
    def dataType() -> type[float]: ...
    def __init__(self, *args: PySide6.QtCore.Qt.Orientation | PySide6.QtWidgets.QWidget | None, **kwargs: Unpack[_QSliderKwargs]) -> None: ...
    def intValue(self, value: float) -> int | None:
        """ Multiply the value (expecting a float value) by the
            precision factor  to hold the value as an integer.
        """
    def toTypeValue(self, value: float) -> float | None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def emitValueChanged(self, value: float) -> None:
        """ Emit a value changed event for a given value.
            NOTE: the value may be unbound
        """
    def value(self) -> float | None:
        """ Return value as float
        """
    def setSingleStep(self, value: float) -> None: ...
    def singleStep(self) -> float | None: ...
    def enumType(self) -> int: ...
    def toType(self, value: float | str) -> float: ...
    def lockUI(self, value: bool) -> None:
        """ Disable the widget if we are locked.
        """

class IntSlider(SliderBase):
    """ Slider for int values
    """
    sliderChanged: ClassVar[PySide6.QtCore.Signal]
    TYPE = int
    @staticmethod
    def dataType() -> type[int]: ...
    def __init__(self, *args: PySide6.QtCore.Qt.Orientation | PySide6.QtWidgets.QWidget | None, **kwargs: Unpack[_QSliderKwargs]) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def toType(self, value: float | str) -> int: ...
    def intValue(self, value: int) -> int: ...
    def toTypeValue(self, value: int) -> int: ...
    def emitValueChanged(self, value: int) -> None: ...
    def enumType(self) -> int: ...
    def lockUI(self, value: bool) -> None:
        """ Disable the widget if we are locked.
        """

class LogFloatSlider(FloatSlider):
    """
    The class provides a QSlider implementation for controlling
    bound and unbound logarithmic float values with a default precision
    factor of 6 digits.
    """
    DECIMALS: int
    DOMAIN_MINIMUM: float
    def __init__(self, *args: PySide6.QtCore.Qt.Orientation | PySide6.QtWidgets.QWidget | None, **kwargs: Unpack[_QSliderKwargs]) -> None: ...
    def paintEvent(self, paint_event: PySide6.QtGui.QPaintEvent) -> None: ...
    def setTickmarkColor(self, color: PySide6.QtGui.QColor) -> None: ...

class LogIntSlider(IntSlider):
    """
    The class provides a QSlider implementation for controlling
    bound and unbound logarithmic int values.
    """
    DECIMALS: int
    DOMAIN_MINIMUM: int
    def __init__(self, *args: PySide6.QtCore.Qt.Orientation | PySide6.QtWidgets.QWidget | None, **kwargs: Unpack[_QSliderKwargs]) -> None: ...
    def paintEvent(self, paint_event: PySide6.QtGui.QPaintEvent) -> None: ...
    def setTickmarkColor(self, color: PySide6.QtGui.QColor) -> None: ...

class SliderLabel(LabelEdit):
    def __init__(self, **kwargs: Any) -> None: ...
    def resetStyleSheet(self) -> None: ...
    def factoryStyleSheet(Self: SliderLabel) -> str: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def lockUI(self, value: bool) -> None: ...

class LabelWrapper(QtWidgets.QWidget):
    toggle: PySide6.QtWidgets.QCheckBox
    label: PySide6.QtWidgets.QWidget
    def __init__(self, toggle: PySide6.QtWidgets.QCheckBox, label: PySide6.QtWidgets.QWidget, width: int | None = None, **kwargs: Unpack[_LabelWrapperKwargs]) -> None: ...

class SliderValue(hou.qt.InputField):
    def __init__(self, data_type: int, **kwargs: Any) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...
    def onMousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def onMouseWheelEvent(self, event: PySide6.QtGui.QWheelEvent) -> None:
        """ Increment/decrement the slider value and handle based
            on the wheel direction.
            The value increment is computed as follows:
                wheel: by one-tenth
                Hold CTRL key + wheel: by one number
                Hold SHIFT key + wheel: by one-hundredth
                Hold SHIFT+CTRL key + wheel: by one-thousandth
        """
    def onContextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent, context_menu: PySide6.QtWidgets.QMenu) -> None: ...
    def eventFilter(self, obj: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...
    def setValue(self, value: float | str | None) -> None: ...
    def setText(self, value: float | str) -> None: ...
    def editor(self) -> PySide6.QtWidgets.QLineEdit: ...
    def isLadderOpen(self) -> bool: ...
    def factoryStyleSheet(Self: SliderValue) -> str: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def lockUI(self, value: bool) -> None:
        """ Change the background color and disable the widget
            if we are locked.
        """

class Slider(QtWidgets.QWidget):
    """ A uber slider with an horizontal orientation for
        controlling parms:
        [parm label][value label][slider]
    """
    floatValueChanged: ClassVar[PySide6.QtCore.Signal]
    intValueChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, label: str, minval: float, maxval: float, defval: float, min_locked: bool, max_locked: bool, label_editing: bool = True, **kwargs: Any) -> None: ...
    def label(self) -> SliderLabel: ...
    def value(self) -> SliderValue: ...
    def toggle(self) -> PySide6.QtWidgets.QCheckBox | None: ...
    def lockUI(self, value: bool) -> None: ...
    def qtSlider(self) -> FloatSlider | IntSlider: ...
    def keyButton(self) -> PySide6.QtWidgets.QToolButton | None: ...
    def resetButton(self) -> PySide6.QtWidgets.QToolButton | None: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def visualSize(self) -> int: ...
    def setShadowEffectState(self, value: bool) -> None: ...
    def hasShadowEffect(self) -> bool: ...
    def setTextColor(self, color: PySide6.QtGui.QColor) -> None: ...
    def setTickmarkColor(self, color: PySide6.QtGui.QColor) -> None: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def minimumLocked(self) -> bool: ...
    def maximumLocked(self) -> bool: ...
    def setMinimumLocked(self, value: bool) -> None: ...
    def setMaximumLocked(self, value: bool) -> None: ...
    def updateSlider(self, value: float, allow_off_bound: bool = True) -> None:
        """ Set the slider value. Call updateSlider to allow values to
            be set off limits. updateSlider is typically called to
            set the slider value programmatically.
        """
    def updateSliderFromMousePosition(self, mouse_pos: PySide6.QtCore.QPoint, prev_mouse_pos: PySide6.QtCore.QPoint, parm_value: float) -> None:
        """ Set the slider value from a mouse position. The new
            slider value is computed with the mouse position
            relative to the previous parm value.
        """
    def connectToValueChanged(self, callback: Callable[[float], object] | Callable[[int], object], connect: bool = True) -> None:
        """ Connect to a value changed signal which is sent off
            when the slider value changed.
        """

LABEL_STYLE_DEFAULT: int
LABEL_STYLE_PRESSED: int
LABEL_STYLE_SELECT: int
LABEL_STYLE_HOVER: int
SLIDER_VALUE_TOLERANCE: float

class SelectableSlider(Slider):
    """
    Extend the Slider to allow selecting the labels.
    Requires the owner to connect to the sliderBeginSelect,
    sliderDragSelect, sliderReleaseSelect, and sliderResetSelect
    signals and implement them properly to control the selection.
    """
    start_value: float
    prev_value: float
    prev_ladder_open: bool
    selectable: bool
    label_color: PySide6.QtGui.QColor
    is_selected: bool
    cur_label_style: int | None
    sliderBeginSelect: ClassVar[PySide6.QtCore.Signal]
    sliderDragSelect: ClassVar[PySide6.QtCore.Signal]
    sliderReleaseSelect: ClassVar[PySide6.QtCore.Signal]
    sliderResetSelect: ClassVar[PySide6.QtCore.Signal]
    sliderSelectionChanged: ClassVar[PySide6.QtCore.Signal]
    sliderStart: ClassVar[PySide6.QtCore.Signal]
    sliderEnd: ClassVar[PySide6.QtCore.Signal]
    ladderChange: ClassVar[PySide6.QtCore.Signal]
    editingFinished: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def resetLabelColor(self) -> None:
        """ Set the label to its default color. """
    def setLabelSelected(self) -> None:
        """ Set the label color to it selected. """
    def setLabelHovered(self) -> None:
        """ Set the label color to it hovered. """
    def setLabelPressed(self) -> None:
        """ Set the label color to it hovered. """
    def onUpdateLabelColor(self, val: PySide6.QtGui.QColor) -> None:
        """ Callback for updating label color from prefs. """
    def onUpdateShadowEffectState(self, val: bool) -> None:
        """ Callback for updating shadow effect from prefs. """
    def updateSelected(self) -> None:
        """ Update the state based on whether its selected. """
    def setSelected(self, val: bool) -> None:
        """ Set this slider to be selected. """
    def resetSelection(self) -> None:
        """ Reset the selection. """
    def isSelected(self) -> bool:
        """ Whether the slider is selected. """
    def isPosOnLabel(self, global_pos: PySide6.QtCore.QPoint) -> bool:
        """ Whether the position is on my label. """
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """
        After the mouse is pressed on the widget, it then captures all further
        mouse drags and the release and sends it all to this widget.

        To process the drag select, send the event to the handler to
        then process the drag.
        """
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """
        After the mouse is pressed on the widget, it then captures all further
        mouse drags and the release and sends it all to this widget.

        To process the drag select, send the event to the handler to
        then process the release.
        """
    def labelPressed(self, event: PySide6.QtGui.QMouseEvent) -> None:
        """ Handle the label being pressed, send the event to the handler. """
    def isLadderOpen(self) -> bool:
        """ Whether the value ladder is open on this slider. """
    def getSliderValue(self) -> float:
        """ Get the value in the field. """
    def setStartValue(self) -> None:
        """ Stash the current value. """
    def getRelativeChange(self) -> float:
        """ Get change from the last call to setStartValue. """
    def updateSliderRelative(self, delta: float, allow_off_bound: bool = True) -> None:
        """ Change the value adding delta to the value when setStartValue() was called. """
    def eventFilter(self, source: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool:
        """ Qt override for catching mouse press and release. """

class SelectableValueField(SelectableSlider):
    """
    Extend the SelectableSlider to allow hiding the slider itself and the label,
    and also add support for mouse hotkeys and changing the width of the value
    field.
    """
    use_mouse_wheel: bool
    value_width: int | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def setVisualSize(self, visual_size: int) -> None:
        """ Callback for updating visual size. """
    def eventFilter(self, source: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool:
        """ Qt override for catching mouse press and release. """

class ToolBar(QtWidgets.QWidget):
    color_options: ru.ColorOptions | None
    COLOR_FACTOR: dict[hou.EnumValue[hou.viewportColorScheme], int]
    def __init__(self, button_size: PySide6.QtCore.QSize | None = None, spacing: int | None = None, margin: PySide6.QtCore.QMargins | None = None, transparent: bool = True, stretch_end: bool = True, **kwargs: Unpack[_QWidgetKwargs]) -> None: ...
    def addButton(self, btn_action: PySide6.QtGui.QAction, icon_names: list[str] | None = None) -> None:
        """ Add a toolbar button.
            btn_action: QtGui.QAction for defining the toolbar
                        button.
            icon_names: list of icons, can contain up to 2 icons
                        for checkable buttons.
        """
    def updateLook(self) -> None:
        """ Update the tool bar buttons look.
        """

class RadioButtonToolBar(QtWidgets.QWidget):
    """ Implements a radio button strip with Qt which behaves like
        a group of radio buttons arranged in a toolbar.
    """
    buttonClicked: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, btn_actions: Iterable[tuple[PySide6.QtGui.QAction, str]], button_size: PySide6.QtCore.QSize | None = None, stretch_end: bool = True, spacing: int | None = None, margin: PySide6.QtCore.QMargins | None = None, parent: PySide6.QtWidgets.QWidget | None = None) -> None:
        """ btn_actions: list of buttons, each item is a tuple of
                         QAction and icon name.
            button_size: Button size for the toolbar
            spacing:     Layout spacing between buttons
            margin:      Layout margin around buttons
        """
    def onActionTriggered(self) -> None: ...
    def selectedAction(self) -> PySide6.QtGui.QAction | None: ...
    def setSelectedAction(self, index: int) -> None: ...
