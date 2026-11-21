# Houdini stubs generated from Houdini 22.0.466

import hou
import resourceui as rui
import statehud.config as config
import statehud.utils as shu
import typing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from hutil.PySide import QtCore, QtGui, QtWidgets
from statehud.baseconfig import AbstractConfig as AbstractConfig
from statehud.config import ConfigWrapper as ConfigWrapper
from statehud.parmutils import ButtonParm as ButtonParm, ButtonStripParm as ButtonStripParm, FloatParm as FloatParm, HUDParm as HUDParm, IntegerParm as IntegerParm, LabelParm as LabelParm, MenuParm as MenuParm, ParmEvent as ParmEvent, StringParm as StringParm, ToggleParm as ToggleParm, _HUDParmValue
from typing import Any, ClassVar, Concatenate, Literal, NotRequired, Protocol, TypedDict

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_ParmT = TypeVar('_ParmT', bound=HUDParm)
class _ParmUpdater(Protocol):
    def __call__(self, fn: Callable[_P, _R], /) -> Callable[_P, _R]: ...

class _ParmEventDict(TypedDict):
    parm_name: str
    parm_value: _HUDParmValue
    event: ParmEvent
    type_name: str | None
    tab_widget_name: str | None
    tab_name: str | None
    alt_value: NotRequired[str | list[str]]
    args: NotRequired[tuple[_HUDParmValue, ...]]
    index: NotRequired[int]
    hotkey: NotRequired[str]
    on: NotRequired[bool]
    action: NotRequired[str]

class _MultiChangeCallback(Protocol):
    def __call__(self, driver_name: str, started: bool, names: list[str] = ..., /) -> object: ...

SIZE12: int
ICON_SIZE: int
PIN_ICON: QtGui.QIcon
MINIMIZE_ICON: QtGui.QIcon
MAXIMIZE_ICON: QtGui.QIcon
LOCK_ICON: QtGui.QIcon
UNLOCK_ICON: QtGui.QIcon
MINIMIZE_TOOLTIP: str
MAXIMIZE_TOOLTIP: str
LOCK_TOOLTIP: str
UNLOCK_TOOLTIP: str
CFG_WIDTH_KEY: str
CFG_HEIGHT_KEY: str
CFG_PIN_KEY: str
CFG_POS_KEY: str
CFG_POSX_KEY: str
CFG_POSY_KEY: str
CFG_LOCK_KEY: str
CFG_VIS_KEY: str
CFG_TITLEVIS_KEY: str
CFG_MIN_KEY: str
CFG_WIDGETS_KEY: str
CFG_AUTOPOS_KEY: str
CFG_AUTORESIZE_KEY: str

class HUDWindow(hou.qt.ViewerOverlay):
    """
    The HUD Handle window is the viewer overlay holding one or
    multiple HUD widgets.

    :scene_viewer: The active scene viewer.
    :visual_size: The current visual size.
    """
    scene_viewer: hou.SceneViewer
    windowVisibility: ClassVar[QtCore.Signal]
    def __init__(self, scene_viewer: hou.SceneViewer, default_size: int | None = None, full_resize: bool = False, auto_resize: bool = False, title: str | None = None, title_alignment: QtCore.Qt.AlignmentFlag = ..., bold_title: bool = True) -> None: ...
    def setWindowSetting(self, window: object, pref_name: str, pref_val: object) -> None:
        """ Callback for the HUD pref handler. """
    def changeVisualSize(self, visual_size_index: int, defer: bool = True) -> None:
        """ Callback for the HUD pref handler. """
    def setDrawBackgroundState(self, pref_value: bool) -> None:
        """ Callback for the HUD pref handler. """
    def isDrawBackgroundEnabled(self) -> bool:
        """ Callback for the HUD pref handler. """
    def setDrawBackgroundColor(self, color: hou.Color | tuple[float, ...]) -> None:
        """
        Callback for the HUD pref handler.

        :color: The color to set the background to.
        """
    def drawBackgroundColor(self) -> hou.Color | tuple[float, ...]:
        """ Callback for the HUD pref handler. Get the background color. """
    def setDrawLabelColor(self, color: tuple[float, ...]) -> None:
        """ Callback for the HUD pref handler. """
    def drawLabelColor(self) -> hou.Color | tuple[float, ...]:
        """ Callback for the HUD pref handler. """
    def setShadowEffectState(self, pref_value: bool) -> None:
        """ Callback for the HUD pref handler. """
    def hasShadowEffect(self) -> bool:
        """ Callback for the HUD pref handler. """
    def openPreferences(self) -> None: ...
    def activate(self) -> None:
        """ Call when the HUD window is ready to be activated. """
    def deactivate(self) -> None:
        """ Call when the window is ready to be deactivated. """
    def isClosed(self) -> bool:
        """ Whether the window is closed. """
    def show(self, value: bool = True) -> None:
        """ Change the window visibility state.
            All HUD widgets are changed at once.

            value: True to show
        """
    def isVisible(self, check_embedded: bool = False) -> bool: ...
    def setEmbedded(self, value: bool) -> None: ...
    def embedded(self) -> bool: ...
    def isValid(self) -> bool:
        """ Whether the HUD Window is valid. """
    def loadFromConfig(self, hud_config: HUDConfig, **kwargs: bool) -> None:
        """ Load my settings from the config. """
    def saveToConfig(self, hud_config: HUDConfig, **kwargs: bool) -> None:
        """ Save my settings to the config. """
    def addHUDWidget(self, hud_widget: QtWidgets.QWidget, vbox: QtWidgets.QBoxLayout | None = None) -> None:
        """ Add HUD handle widgets to the grid layout.
        """
    def removeHUDWidget(self, hud_widget: QtWidgets.QWidget, vbox: QtWidgets.QBoxLayout | None = None) -> None:
        """ Remove a HUD widget from the specified layout. """
    def hudWidgets(self) -> list[QtWidgets.QWidget]:
        """ Get the HUD Widgets. """
    def setTitle(self, title: str) -> None:
        """ Set the title text. """
    def title(self) -> str:
        """ Get the title text. """
    def clearContent(self, vbox: QtWidgets.QBoxLayout | None = None) -> None:
        """ Clear the contents of the window. """
    def setEnabledState(self, value: bool) -> None:
        """ Set whether the window is enabled. """
    def isPosLocked(self) -> bool:
        """ Wether the position is locked. """
    def setLockState(self, value: bool) -> None:
        """ Lock the window position, disable title,
            hide window bar
        """
    def isMinimized(self) -> bool:
        """ Whether this panel is minimized. """
    def clearFixedSize(self, defer: bool = False) -> None:
        """
        Clear the fixed size on the panel.

        If ignore_manual_resize is true, min size is set to (0,0) and
        max size is set to the viewport size.

        Otherwise, if there is a full resize frame, then this
        resets the current fixed size to the cached fixed size.

        Otherwise, if there is only a width resize grip, then this
        keeps the fixed width, and sets the minimum height to 0 and
        maximum height to the height of the viewport.

        The two latter cases are designed so that you can call
        clearFixedSize() to enable dynamic resizing of only those
        dimensions not tied to a resize grip which should actually
        keep that size.
        """
    def revertFixedSize(self, defer: bool = False) -> None:
        """
        Revert the size back to the stored fixed size.
        This is used for example if the size was set automatically
        or the panel was minimized to revert back to the manually
        set size.
        """
    def refreshSize(self, defer: bool = False) -> None:
        """
        Refresh the size of widgets. First clear the fixed size, and
        then reset it, or leave it as non-fixed size if auto resize
        disabled or minimize is enabled.
        """
    def autoResize(self, defer: bool = False) -> bool:
        """ Auto resize the window if enabled. """
    def setMinimizeState(self, value: bool) -> None:
        """ Called when changing the minimize state of the window programmatically. """
    def setMinimizeOverride(self, callback: Callable[[bool], object] | None) -> None:
        """Set a callback(bool) that overrides the default minimize behavior.
        If set, called instead of _setMinimizeState. Pass None to clear."""
    def isTitleVisible(self) -> bool:
        """ Whether the title is visible. """
    def setTitleVisible(self, value: bool) -> None:
        """ Set whether the title row is visible. """
    def onDisplayTitleAction(self, value: bool) -> None:
        """ Update on changing whether the title is displayed."""
    def setVisualSize(self, visual_size: int) -> None:
        """ Set the visible size of the window. """
    def visualSize(self) -> int:
        """ The visual size of the window. """
    def sizeHint(self) -> QtCore.QSize:
        """ The size hint for the window. Qt will read this to see how to
            size the window.
        """
    def windowSize(self) -> QtCore.QSize:
        """ Get the window size. """
    def setWidth(self, new_width: int) -> None:
        """ Set the width of the window."""
    def setHeight(self, new_height: int) -> None:
        """ Set the height of the window."""
    def setFullWidth(self, w: int) -> None:
        """ Set the unminimized width of the panel. """
    def setFullHeight(self, h: int) -> None:
        """ Set the unminimized height of the panel. """
    def getFullWidth(self) -> int:
        """ The unminimized width of the panel. """
    def getFullHeight(self) -> int:
        """ The unminimized height of the panel. """
    def restoreFullHeight(self) -> None:
        """ Reset the height to the stored fixed height. """
    def restoreFullWidth(self) -> None:
        """ Reset the width to the stored fixed width. """
    def onNewWidth(self, new_width: int) -> None:
        """
        Called when a new width has been computed
        during a window geometry update.

        :new_width: The new width of the window.
        """
    def onNewHeight(self, new_height: int) -> None:
        """
        Called when a new height has been computed during a window geometry update.

        :new_height: The new height of the window.
        """
    def onNewGeometry(self, w: int, h: int, new_pos: QtCore.QPoint) -> None:
        """
        Called by ResizeFrame when a new size and position has been
        computed during a drag operation.

        :w: The new width
        :h: The new height
        :new_pos: The new top-left position.
        """
    def beginResizing(self, region: int | None) -> None:
        """
        Called when the resize frame or resize grips begin resizing.
        Look at the region and if the resize region is against
        at least one of the boundaries we are pinned to i.e.
        bottom and left, then unpin.

        :region: Where on the frame is grabbed.
        """
    def endResizing(self) -> None:
        """ Finish resizing the window frame. """
    def canMove(self) -> bool:
        """ Called by the WindowBar, return true if we are movable. """
    def onWindowPlacement(self, defer: bool = True) -> None:
        """
        Update the windows geometry and possibly move it in bounds.
        This should be called when the window is moved or changes size.

        :defer: Whether to defer execution of the _onWindowPlacement internal func.
        """
    def onViewerActivated(self) -> None:
        """ Override to set visibility on the window to False. """
    def onViewerDeactivated(self) -> None:
        """ Override to set visibility on the window to True. """
    def isPinned(self) -> bool:
        """ Whether we are pinned at all. """
    def setPinState(self, value: int) -> None:
        """ Set the pin state. """
    def setPinManager(self, mgr: shu.PinManager) -> None:
        """ Set the pin manager for this window. """
    def pinLeft(self) -> None:
        """ Set the window to be pinned to the bottom left. """
    def pinRight(self) -> None:
        """ Set the window to be pinned to the bottom right. """
    def pinTopRight(self) -> None:
        """ Set the window to be pinned to the top right. """
    def clearPin(self) -> None:
        """ Unpin the window. """
    def getPinState(self) -> int:
        """ Get the current pin state. """
    def setFadeUnpinned(self, enabled: bool) -> None:
        """Opt-in: when enabled and the window position is unlocked,
        the thin border around the window is fully transparent at rest
        and only appears on mouse hover at the edge."""
    def onMenuAboutToShow(self) -> None:
        """ Called when the context menu is about to be shown.
            Currently only hides the title tooltip.
        """
    def onMenuAboutToHide(self) -> None:
        """ Called when the menu is about to be hidden. """
    def onContextMenu(self, pos: QtCore.QPoint) -> None:
        """ Open the context menu. """
    def onHideAction(self) -> None:
        """ Hide this window. """
    def onInitWindow(self) -> None:
        """ Override the base implementation."""
    def setAutoResize(self, val: bool) -> None:
        """ Set whether auto resizing is enabled, and update the toggle. """
    def isAutoResize(self) -> bool:
        """ Whether auto resizing is enabled. """
    def setAutoPosition(self, val: bool) -> None:
        """ Set whether auto postioning is enabled and update the toggle. """
    def isAutoPosition(self) -> bool:
        """ Whether auto positioning is enabled. """
    def shouldAutoPosition(self) -> bool:
        """
        Whether the window should be auto positioned.
        Only auto position the window if autopositioning is enabled,
        and the window is not locked and not pinned.
        """
    def adjustHeaderForTabBar(self, tab_widget: QtWidgets.QTabWidget) -> None:
        """Adjust header right margin to avoid overlapping an East-positioned tab bar."""
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Override from ViewerOverlay to always consume the window
        deactivate on the window container.

        Returns true for events to prevent sending to descendants.

        :source: The source widget of the event.
        :event: The event.
        """
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """ Called by QWidget.close(). """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Qt override for mouse press. """
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Qt override for mouse released. """
    def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Called by the WindowBar widget on mouse down."""
    def onMouseMoveEvent(self, event: QtGui.QMouseEvent, new_pos: QtCore.QPoint) -> None:
        """
        Called by the WindowBar widget when the mouse is moving.
        The window is moved to the new position computed by the
        WindowBar widget.

        event: mouse event object
        new_pos: position computed by the WindowBar widget to
               move the window to.
        """
    def onMouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Called by the WindowBar widget when the mouse is released.

        event: mouse event object
        """
    def onMouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Called by the WindowBar widget when double clicked. """
    def setBackgroundColor(self, col: hou.Color | tuple[float, ...]) -> None:
        """ Set the background colour of the panel. """
    def backgroundColor(self) -> hou.Color | tuple[float, ...]: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """
        Draw the window background with rounded corners.
        enclosed: all flat corners
        """

class HUDConfig(config.ConfigWrapper):
    """
    A wrapper for all functions for loading and saving state from
    HUD windows.

    Any config type can theoretically be slotted in here to allow
    saving and loading from many different sources.
    """
    def loadHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None:
        """
        Load the settings for the HUD from this config.

        :hud_window: The window to set settings on.
        :kwargs: The dictionary supplied with options for whether to load each setting.
        """
    def saveHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None:
        """
        Save the settings for the HUD to this config.

        :hud_window: The window to save settings from.
        :kwargs: The dictionary supplied with options for whether to save each setting.
        """

class HUDUserDataConfig(HUDConfig):
    """ A config wrapper for storing HUD settings to user data. """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class WidgetBundleWindow(HUDWindow):
    """
    Encapsulate a bundle of HUD sliders in a hou.qt.ViewerOverlay
    window. These windows and sliders are designed to be instantiated
    through a python state, and are designed to work directly with the
    python state.

    The functions in this class are loosely grouped into the following
    categories.
    - Widget Utility: These are utility functions for binding the parameters.
    - Tab Management: These function manage the tab widget type.
    - Slider Utility: These are utility functions for managing sliders
    - Context Actions: These function manage the addition of callback for the
                       right-click menu of the parameters.
    - Widget Visibility: These functions manage widget visibility
    - Enabling/Disabling Widgets: These functions manage whether the parameters
                                  are enabled.
    - Binding Parameters: These are the function that bind specific widget types.
    - Setting/Getting Parameters: These function manage evaluating/setting parameters.
    - Configuration Management: These functions load and save parameters to a config.
    - Parameter Callback Management: These function execute the value changed and 
                                     button clicked callbacks for the parameters.

    """
    slider_range: dict[str, float]
    callback: Callable[[_ParmEventDict], object] | None
    parmUpdater: ClassVar[_ParmUpdater]
    def __init__(self, scene_viewer: hou.SceneViewer, default_size: int | None = None, full_resize: bool = False, auto_resize: bool = False, title: str | None = None, title_alignment: QtCore.Qt.AlignmentFlag = ..., bold_title: bool = True, callback: Callable[[_ParmEventDict], object] | None = None, custom_style: bool = False) -> None: ...
    def close(self) -> None: ...
    def getParm(self, name: str) -> HUDParm | None: ...
    def addParm(self, parm: _ParmT) -> _ParmT: ...
    def removeParm(self, name: str) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Qt override for catching key press events.
        This is only used for checking if the modifier
        keys for the grouping change while interacting.
        """
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Qt override for catching key release events.
        This is only used for checking if the modifier
        keys for the grouping change while interacting.
        """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Handle clicking on empty space to reset selection. """
    def selectedSliders(self) -> list[str]:
        """ Get the list of selected sliders. """
    def resetSelectedSliders(self, skip: str | None = None) -> None:
        """ Reset the list of selected sliders. Optionally skipping one. """
    def bindSelectedMultiChangeCallback(self, callback: _MultiChangeCallback) -> None: ...
    def removeSelectedMultiChangeCallback(self, callback: _MultiChangeCallback) -> None: ...
    def addSliderGrouping(self, names: list[str], modifier: QtCore.Qt.KeyboardModifier | None = None, relative: bool = True, adhoc: bool = False) -> shu.SliderGrouping:
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
    def getGrouping(self, driver: str) -> shu.SliderGrouping | None:
        """
        Get the names tied together in the grouping in which driver is
        part of.
        """
    def bindFolder(self, name: str, tab_widget_name: str | None = None, tab_name: str | None = None, collapsible: bool = False, collapsed: bool = False, label: str | None = None, label_width: int | None = None) -> rui.FolderWidget | rui.CollapsibleFolderWidget:
        """ Binds a folder widget. """
    def wrapAndBindWidget(self, name: str, widget: QtWidgets.QWidget, tooltip: str | None = None, label: str | None = None, right_label: str | None = None, label_width: int | None = None, centered: bool = False, expanding: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None, action_button: shu.ActionButtonManager | None = None, toggle_name: str | None = None, toggle_callback: Callable[..., object] | None = None, toggle_value: bool | None = None, **kwargs: object) -> rui.HUDWidgetWrapper:
        """
        Wrap a generic Qt widget and bind it to the window.
        The returned widget is a HUDWidgetWrapper around widget.
        To get the provided widget, use HUDWidgetWrapper.getWidget().
        """
    def getWrappedWidget(self, name: str) -> QtWidgets.QWidget | None:
        """ Get a bound, wrapped widget. """
    def getWidget(self, name: str) -> QtWidgets.QWidget | None:
        """ Get a widget by name or None if not found. """
    def unbindWidget(self, name: str, tab_widget_name: str | None = None, tab_name: str | None = None) -> None:
        """ Remove a HUD widget by name. """
    def isTabScrollable(self, tab_widget_name: str, tab_name: str) -> bool: ...
    def bindTabWidget(self, name: str, tab_names: Sequence[str], tab_labels: Sequence[str] | None = None, tab_widget_name: str | None = None, tab_name: str | None = None, tab_position: QtWidgets.QTabWidget.TabPosition | None = None, tab_align_end: bool = False, compact_horizontal_tabs: bool = True) -> rui.TabWidget:
        """ Bind a tab widget and create the given tabs. """
    def addTab(self, tab_widget_name: str, tab_name: str, tab_label: str | None = None) -> rui.TabWidgetTab:
        """ Add a tab to the tab widget. """
    def setTabLabel(self, tab_widget_name: str, tab_name: str | None, tab_label: str) -> None:
        """ Set the tab label for a tab in a tab widget,
        or update a folder header if tab_name is None and the name
        resolves to a CollapsibleFolderWidget. """
    def setTabCurrentIndexFirst(self, tab_widget_name: str) -> None:
        """ Set the current tab to the first visible and enabled tab. """
    def removeTab(self, tab_widget_name: str, tab_name: str) -> None:
        """ Remove a tab from a tab widget. """
    def clearFolder(self, folder_widget_name: str) -> None:
        """ Clear a folder widget. """
    def clearTab(self, tab_widget_name: str, tab_name: str | None) -> None:
        """ Clear a tab in a tabwidget, or a folder if tab_name is None. """
    def clearTabs(self, tab_widget_name: str) -> None:
        """ Clear all tabs in a tab widget. """
    def getTab(self, tab_widget_name: str, tab_name: str) -> rui.TabWidgetTab | rui.TabWidgetTabNoScroll | None:
        """ Get a tab widget by name. """
    def getTabIndex(self, tab_widget_name: str, tab_name: str) -> int:
        """ Get the tab index of a tab widget by name. """
    def setTabTitleMetadata(self, tab_widget_name: str, tab_name: str, title: str | None = None, prefix: str | None = None, suffix: str | None = None) -> None:
        """
        Set the tab title metadata, this is picked up when switching tabs
        to set the title of the window. If currently on the tab, this will
        also update the title of the window.
        """
    def setTitleFromTabIndex(self, tab_widget_name: str, tab_index: int | None = None, prefix: str | None = None, suffix: str | None = None) -> None:
        """
        Set the title of the window from a tab.
        First will check if the tab has existing tab title metadata,
        (see setTabTitleMetadata) and if so, will use that to set the title,
        otherwise will set the title from the tab label.
        """
    def setTitleFromCurrentTab(self, tab_widget_name: str, prefix: str | None = None, suffix: str | None = None) -> None:
        """
        Set the title of the window from the current tab.
        First will check if the tab has existing tab title metadata,
        (see setTabTitleMetadata) and if so, will use that to set the title,
        otherwise will set the title from the tab label.
        """
    def setTitleFromTab(self, tab_widget_name: str, tab_name: str, prefix: str | None = None, suffix: str | None = None) -> None:
        """
        Set the title of the window from a tab.
        First will check if the tab has existing tab title metadata,
        (see setTabTitleMetadata) and if so, will use that to set the title,
        otherwise will set the title from the tab label.
        """
    def setTabVisible(self, tab_widget_name: str, tab_name: str, on: bool) -> None:
        """ Set whether a tab is visible. """
    def isTabVisible(self, tab_widget_name: str, tab_name: str) -> bool:
        """ Whether a tab is visible. """
    def setTabEnabled(self, tab_widget_name: str, tab_name: str, on: bool) -> None:
        """ Set whether a tab is enabled. """
    def getCurrentTabName(self, tab_widget_name: str) -> str:
        """ Get the name of the current tab. """
    def setCurrentTab(self, tab_widget_name: str, tab_name: str, default_first: bool = False) -> bool:
        """
        Set the current tab of a tab widget by name. 
        If default_first is True and the tab is not enabled or not visible,
        will set the current tab to the first visible and enabled tab.
        """
    def setSliderRange(self, name: str, minimum: float = 0.0, maximum: float = 10.0) -> None:
        """ Reset the sliders range to be between [minimum, maximum]. """
    def setSliderCentered(self, name: str) -> None:
        """
        Centers the slider with the given name. If the
        previous range was [min, max] and the current value
        is val, the new range is [val-(max-min)/2, val+(max-min)/2].
        """
    def setSlidersCentered(self, sliders: Iterable[str] | None = None) -> None:
        """
        Centers all sliders around their current value. If the
        current range is [min, max], and the current value is val,
        the new range is [val-(max-min)/2, val+(max-min)/2].

        sliders: A list of slider names to be centered.
        """
    def moveToMouse(self, under_slider: bool = True, slider_name: str | None = None, defer: bool = True, offset: QtCore.QPoint | None = None) -> None:
        """ Move the window to the mouse. """
    def connectSliderValueChanged(self, slider_name: str, callback: Callable[[float], object] | Callable[[int], object]) -> None:
        """ Connect the slider with name 'slider_name' to the given 'callback'."""
    def show(self, value: bool = True) -> None:
        """
        Show the window and the sliders. Optionally, you can pass in
        a list of slider names to make visible, and only these
        sliders will be made visible.

        value: whether to show or hide the window.
        """
    def updateVisibleWidgets(self) -> None:
        """
        Update the visible widgets.
        If widgets are hidden or shown while the window is minimized
        or hidden, they will not have the correct visibility when the window
        this is used to set the visibility on all widgets using the cached
        visibility stored by the window.
        """
    def updateVisibleSliders(self, visible_sliders: Iterable[str] | None = None) -> None:
        """
        Update the set of visible sliders.

        visible_sliders: A list or tuple of slider names to set
            as visible. If set to None, then all sliders are
            made visible.
        """
    def setWidgetsVisible(self, widget_list: Iterable[str], on: bool) -> None:
        """ Set the sliders in the given list to be shown or hidden. """
    def setWidgetDisabled(self, name: str, val: bool = True) -> None:
        """ Set the widget by name to be disabled. """
    def setWidgetEnabled(self, name: str, val: bool = True) -> None:
        """ Set the widget by name to be enabled. """
    def getWidgetEnabled(self, name: str) -> bool | None:
        """ Get the widget by name if disabled. """
    def bindContextActionCallback(self, callback: Callable[[str, str], object]) -> None:
        """
        Bind a callback that gets called when an action in
        the context menu for a slider is triggered.

        When triggered it calls callback(ACTION_KEY, widget_name)
        """
    def bindContextActionMultiCallback(self, callback: Callable[[str, list[str]], object]) -> None:
        """
        Bind a callback that gets called when an action in
        the context menu for a slider is triggered.

        This callback will either be given [widget_name] if the widget is
        not part of the selected widgets, otherwise will provide the
        full list of selected widgets.

        When triggered it calls callback(ACTION_KEY, widget_names)
        """
    def removeContextActionCallback(self, callback: Callable[[str, str], object] | Callable[[str, list[str]], object]) -> None:
        """
        Remove a callback that gets called when an action in
        the context menu for a slider is triggered.
        """
    def onContextMenuAction(self, action: str, widget_name: str) -> None: ...
    @parmUpdater
    def bindSlider(self, name: str, label: str | None = None, min_value: float = 0.0, max_value: float = 10.0, default_value: float = 2.5, min_locked: bool = False, max_locked: bool = False, tooltip: str | None = None, hide_slider: bool = False, keep_slider_space: bool = True, bind_context_menu: bool = True, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, use_mouse_wheel: bool = False, slider_type: type[rui.SliderBase] | None = None, callback: Callable[[float], object] | Callable[[int], object] | None = None, selectable: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None, label_width: float | None = None, toggle_name: str | None = None, toggle_callback: Callable[..., object] | None = None, toggle_value: bool | None = None, **kwargs: object) -> shu.KeyableSlider:
        """
        Bind a slider with the given parameters to the slider bundle
        window.

        :name: Name of the slider widget internally.
        :label: The label to give the slider.
        :min_value: Minimum value of the slider.
        :max_value: Maximum value of the slider.
        :default_value: Default value for the slider.
        :min_locked: Whether minimum limit is a hard limit.
        :max_locked: Whether maximum limit is a hard limit.
        :decimals: For float sliders, the number of decimal digits.
        :tooltip: The tooltip text for the slider.
        :slider_type: Slider class.
        :callback: Function to use for a value callback.
        :bind_context_menu: Whether to bind the context menu.
        :mouse_hotkeys: Hotkeys for the mouse when clicked.
        :hide_slider: Whether to hide the slider part.
        :keep_slider_space: When slider is hidden, whether to keep a space to ensure proper alignment.
        :label_width: The width of the label part.
        :use_mouse_wheel: Whether the mouse wheel is used to change the slider.
        :value_width: The width of the value part.
        :tab_widget_name: The name of a tab widget to insert this widget in.
        :tab_name: The name of the tab within the tab widget to insert the widget in.
        :toggle_name: The name of the preceeding toggle parameter.
        :toggle_callback: The callback that is run when the slider's toggle is toggled.
        :toggle_value: The default value of the preceeding toggle parameter.
        """
    @typing.overload
    def bindFloatSlider(self, name: str, label: str | None = ..., min_value: float | list[float] = ..., max_value: float | list[float] = ..., default_value: float | Sequence[float] | None = ..., min_locked: bool = ..., max_locked: bool = ..., tooltip: str | None = ..., hide_slider: bool = ..., keep_slider_space: bool = ..., bind_context_menu: bool = ..., mouse_hotkeys: Mapping[tuple[int, int], str] | None = ..., use_mouse_wheel: bool = ..., callback: Callable[..., object] | None = ..., selectable: bool = ..., tab_widget_name: str | None = ..., tab_name: str | None = ..., num_components: Literal[1] = ..., use_component_label: bool = ..., **kwargs: Any) -> shu.KeyableSlider: ...
    @typing.overload
    def bindFloatSlider(self, name: str, label: str | None = ..., min_value: float | list[float] = ..., max_value: float | list[float] = ..., default_value: float | Sequence[float] | None = ..., min_locked: bool = ..., max_locked: bool = ..., tooltip: str | None = ..., hide_slider: bool = ..., keep_slider_space: bool = ..., bind_context_menu: bool = ..., mouse_hotkeys: Mapping[tuple[int, int], str] | None = ..., use_mouse_wheel: bool = ..., callback: Callable[..., object] | None = ..., selectable: bool = ..., tab_widget_name: str | None = ..., tab_name: str | None = ..., num_components: int = ..., use_component_label: bool = ..., **kwargs: Any) -> shu.KeyableSlider | list[shu.KeyableSlider] | None: ...
    @parmUpdater
    def bindFloatVector(self, name: str, num_components: int = 1, default_value: Sequence[float] | None = None, callback: Callable[..., object] | None = None, min_value: float | None = None, max_value: float | None = None, min_locked: bool | None = None, max_locked: bool | None = None, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, tab_widget_name: str | None = None, tab_name: str | None = None, **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Binds an float vector parameter to the HUD
        """
    @typing.overload
    def bindIntSlider(self, name: str, label: str | None = ..., min_value: int | list[int] = ..., max_value: int | list[int] = ..., default_value: int | Sequence[int] | None = ..., min_locked: bool = ..., max_locked: bool = ..., tooltip: str | None = ..., hide_slider: bool = ..., keep_slider_space: bool = ..., bind_context_menu: bool = ..., mouse_hotkeys: Mapping[tuple[int, int], str] | None = ..., use_mouse_wheel: bool = ..., callback: Callable[..., object] | None = ..., selectable: bool = ..., tab_widget_name: str | None = ..., tab_name: str | None = ..., num_components: Literal[1] = ..., **kwargs: Any) -> shu.KeyableSlider: ...
    @typing.overload
    def bindIntSlider(self, name: str, label: str | None = ..., min_value: int | list[int] = ..., max_value: int | list[int] = ..., default_value: int | Sequence[int] | None = ..., min_locked: bool = ..., max_locked: bool = ..., tooltip: str | None = ..., hide_slider: bool = ..., keep_slider_space: bool = ..., bind_context_menu: bool = ..., mouse_hotkeys: Mapping[tuple[int, int], str] | None = ..., use_mouse_wheel: bool = ..., callback: Callable[..., object] | None = ..., selectable: bool = ..., tab_widget_name: str | None = ..., tab_name: str | None = ..., num_components: int = ..., **kwargs: Any) -> shu.KeyableSlider | list[shu.KeyableSlider] | None: ...
    @parmUpdater
    def bindIntVector(self, name: str, num_components: int = 1, default_value: Sequence[int] | None = None, callback: Callable[..., object] | None = None, min_value: float | None = None, max_value: float | None = None, min_locked: bool | None = None, max_locked: bool | None = None, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, tab_widget_name: str | None = None, tab_name: str | None = None, **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Binds an int vector parameter to the HUD
        """
    @parmUpdater
    def createActionButton(self, name: str, iconpath: str | None, callback: Callable[[bool], object] | None = None, tooltip: str | None = None) -> shu.ActionButtonManager: ...
    @parmUpdater
    def bindButton(self, name: str, label: str, callback: Callable[..., object] | None = None, tooltip: str | None = None, front_label: str | None = None, label_width: int | None = None, centered: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None, **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt Push Button with the given name and label.
        Optionally you can also pass in a callback to have it
        connect the button to the callback.
        """
    @parmUpdater
    def bindComboBox(self, name: str, items: Sequence[str], callback: Callable[..., object] | None = None, tooltip: str | None = None, label: str | None = None, label_width: int | None = None, centered: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None, **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt Combo Box with the given name and items.
        Optionally you can also pass in a callback to have it
        connect the combo box to the callback.

        This will give an ordered menu like those found in the
        parameter pane.
        """
    def updateComboBoxItems(self, name: str, items: Sequence[str]) -> None: ...
    @parmUpdater
    def bindColorField(self, name: str, label: str, default_value: QtGui.QColor | None = None, callback: Callable[[QtGui.QColor], object] | None = None, tooltip: str | None = None, label_width: int | None = None, centered: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt Color Field with the given name and label.
        Optionally you can also pass in a callback to have it
        connect the color field to the callback.
        """
    @parmUpdater
    def bindFileLineEdit(self, name: str, label: str, callback: Callable[[str], object] | None = None, tooltip: str | None = None, label_width: int | None = None, centered: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt File Chooser with the given name and label.
        Optionally you can also pass in a callback to have it
        connect the file chooser to the callback.
        """
    @parmUpdater
    def bindSeparator(self, name: str, label_width: int | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt Push Button with the given name and label.
        Optionally you can also pass in a callback to have it
        connect the button to the callback.
        """
    @parmUpdater
    def bindInputStringField(self, name: str, value: str, menu: QtWidgets.QMenu | None = None, menu_callback: Callable[..., object] | None = None, callback: Callable[..., object] | None = None, tooltip: str | None = None, label: str | None = None, label_width: int | None = None, centered: bool = False, expanding: bool = True, tab_widget_name: str | None = None, tab_name: str | None = None, field_width: int | None = None, action_button: shu.ActionButtonManager | None = None, **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt Input Field of type String with the given name and value.
        Optionally you can also pass in a callback to have it
        connect the input field to a callback. 
        Furthermore you can provide a hou.qt.QtWidget.QMenu for an additional 
        dropdown menu. You can bind an additional menu callback.

        This will give an ordered menu like those found in the
        parameter pane.
        """
    @parmUpdater
    def bindFieldLabel(self, name: str, text: str, tooltip: str | None = None, max_width: int | None = None, label: str | None = None, label_width: int | None = None, centered: bool = False, bold_font: bool = True, tab_widget_name: str | None = None, tab_name: str | None = None, **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Bind a Qt Field Label with the given text.
        """
    @parmUpdater
    def bindButtonStrip(self, name: str, button_names: list[str], button_labels: list[str] | None = None, callback: Callable[..., object] | None = None, tooltip: str | None = None, allow_multi_selection: bool = False, iconpaths: Sequence[str] | None = None, off_iconpaths: Sequence[str | None] | None = None, label: str | None = None, label_width: int | None = None, align_left: bool = False, centered: bool = False, checkable: bool = True, tab_widget_name: str | None = None, tab_name: str | None = None, button_tooltips: Sequence[str] = ..., **kwargs: Any) -> rui.HUDWidgetWrapper:
        """
        Bind a button strip, which is a strip of Qt Push Buttons.
        The full strip is given 'name', the individual buttons are
        given 'labels'.

        :name: The name of the button strip.
        :button_names: The internal names for the individual buttons. This is a list.
        :button_labels: The labels for the individual buttons. This is a list.
            If set to None, uses the 'button_names' as the labels.
        :callback: A function that will be connected to the button
            strip's stateChanged signal.
            Usage - callback(button_name, is_checked)
        :tooltip: The tooltip to be displayed when hovering over the
            button strip.
        """
    @parmUpdater
    def bindToggle(self, name: str, label: str, default_value: bool = False, callback: Callable[..., object] | None = None, tooltip: str | None = None, front_label: str | None = None, label_width: int | None = None, mouse_hotkeys: Mapping[tuple[int, int], str] | None = None, centered: bool = False, tab_widget_name: str | None = None, tab_name: str | None = None, **kwargs: object) -> shu.KeyableToggle:
        """
        Bind a Qt Check Box with the given name and label.
        Optionally you can also pass in a callback to have it
        connect the checkbox to the callback.
        """
    def isUpdatingValue(self) -> bool:
        """
        Whether we are currently updating the sliders value
        through the updateSliderValue function. This can be useful
        when updating the slider value in response to some other
        event, to be able to tell if the slider value that is emitted
        is due to a slider being interacted with, or is due to
        a slider value being explicitly set.
        """
    @parmUpdater
    def updateSliderValue(self, slider_name: str, value: float, update_slider_position: bool = False, relative: bool = False) -> None:
        """ Set the slider with name 'slider_name' to 'value'."""
    def getSliderValue(self, slider_name: str) -> float:
        """ Get the slider value given the 'slider_name'"""
    def getFloatSliderValue(self, slider_name: str) -> float:
        """ Get the float slider value given the 'slider_name'. """
    def getFloatValue(self, parm_name: str, num_components: int = 1, is_vector: bool = False) -> float | hou.Vector2 | hou.Vector3 | hou.Vector4 | list[float] | None:
        """ Gets a float vector value """
    @parmUpdater
    def setFloatValue(self, name: str, value: float | Sequence[float], num_components: int = 1, is_vector: bool = False) -> None:
        """ Sets a float vector value """
    def getIntSliderValue(self, slider_name: str) -> int:
        """ Get the int slider value given the 'slider_name'. """
    def getIntValue(self, parm_name: str, num_components: int = 1, is_vector: bool = False) -> int | list[int] | None:
        """ Gets an int vector value """
    @parmUpdater
    def setIntValue(self, name: str, value: int | Sequence[int], num_components: int = 1, is_vector: bool = False) -> None:
        """ Sets an int vector value """
    def getToggleState(self, name: str, outer_name: str | None = None) -> bool:
        """ Get the toggle state for a checkbox. """
    @parmUpdater
    def setToggleState(self, name: str, on: bool, outer_name: str | None = None) -> None:
        """ Set whether the toggle is on. """
    def getButtonStripState(self, widget_name: str) -> str | list[str] | None:
        """
        Return the name of the checked button, or None if none are
        toggled.
        """
    @parmUpdater
    def setButtonStripState(self, widget_name: str, button_name: str | None = None, on: bool = True) -> None:
        """
        Set the state of the button strip.

        :widget_name: The top level name of the button widget.
        :button_name: The name of a button to change the state on.
            If left to None, and on=False, resets all buttons.
        :on: Whether to set the button to clicked or not.
        """
    def getButtonStripValue(self, widget_name: str) -> int | None:
        """
        Returns the state of the buttons as a bit mask integer.

        :widget_name: The top level name of the button widget.
        """
    @parmUpdater
    def setButtonStripValue(self, widget_name: str, value: int) -> None:
        """
        Sets the state of the buttons on a button strip given a bit mask integer.

        :widget_name: The top level name of the button widget.
        :value: The bit mask.
        """
    @parmUpdater
    def setColorFieldState(self, widget_name: str, color: QtGui.QColor) -> None:
        """
        Set the current index of the combo box of the given name.

        :widget_name: The name of the combo box to set the state on.
        :index: The index in the combo box to set it to.
        """
    @parmUpdater
    def getColorFieldState(self, widget_name: str) -> QtGui.QColor | None:
        """
        Set the current index of the combo box of the given name.

        :widget_name: The name of the combo box to set the state on.
        :index: The index in the combo box to set it to.
        """
    @typing.overload
    def getComboBoxState(self, widget_name: str, as_int: Literal[True] = ...) -> int | None: ...
    @typing.overload
    def getComboBoxState(self, widget_name: str, as_int: bool) -> int | str | None: ...
    @parmUpdater
    def setComboBoxState(self, widget_name: str, index: int) -> None:
        """
        Set the current index of the combo box of the given name.

        :widget_name: The name of the combo box to set the state on.
        :index: The index in the combo box to set it to.
        """
    def getInputStringFieldState(self, widget_name: str) -> str | None:
        """
        Return the current value of the string field with the given name.

        :widget_name: The name of the string field to read from.
        """
    @parmUpdater
    def setInputStringFieldState(self, widget_name: str, value: str) -> None:
        """
        Sets the current value of the string field with the given name.

        :widget_name: The name of the string field to write to.
        :value: The value to write into the string field.
        """
    @parmUpdater
    def getFileLineEditState(self, widget_name: str) -> str | None:
        """
        Return the current value of the string field with the given name.

        :widget_name: The name of the string field to read from.
        """
    @parmUpdater
    def setFileLineEditState(self, widget_name: str, value: str) -> None:
        """
        Sets the current value of the string field with the given name.

        :widget_name: The name of the string field to write to.
        :value: The value to write into the string field.
        """
    def getFieldLabelText(self, widget_name: str) -> str | None:
        """
        Return the current text of the field label with the given name.

        :widget_name: The name of the field label to read from.
        """
    @parmUpdater
    def setFieldLabelText(self, widget_name: str, text: str) -> None:
        """
        Set the text of the field label with the given name.

        :widget_name: The name of the field label to write to.
        :text: The new text of the label
        """
    def getParmValue(self, name: str, menus_as_int: bool = True) -> _HUDParmValue:
        """
        Gets the value of a parameter in the window.
        """
    @parmUpdater
    def setParmValue(self, name: str, value: object) -> None:
        """
        Sets the value of a parameter in the window.
        """
    @parmUpdater
    def loadParmFromConfig(self, name: str, config: AbstractConfig, prefix: str = '') -> None:
        """
        Loads the parameter value from the configuration.
        """
    def saveParmToConfig(self, name: str, config: AbstractConfig, prefix: str = '') -> None:
        """
        Loads the parameter value from the configuration.
        """
    @typing.overload
    def parmCallback(self, name: str, event_type: Literal[ParmEvent.Changed] = ..., expect_index: Literal[False] = ..., **kwargs: object) -> Callable[..., None]: ...
    @typing.overload
    def parmCallback(self, name: str, event_type: Literal[ParmEvent.Changed], expect_index: Literal[True], **kwargs: object) -> Callable[Concatenate[int, ...], None]: ...
    @typing.overload
    def parmCallback(self, name: str, event_type: Literal[ParmEvent.Changed] = ..., *, expect_index: Literal[True], **kwargs: object) -> Callable[Concatenate[int, ...], None]: ...
    @typing.overload
    def parmCallback(self, name: str, event_type: Literal[ParmEvent.HotkeyInvoked], expect_index: Literal[False] = ..., **kwargs: object) -> Callable[[str], None]: ...
    @typing.overload
    def parmCallback(self, name: str, event_type: Literal[ParmEvent.HotkeyInvoked], expect_index: Literal[True], **kwargs: object) -> Callable[[int, str], None]: ...
    @typing.overload
    def parmCallback(self, name: str, event_type: Literal[ParmEvent.SelectionChanged], expect_index: bool = ..., **kwargs: object) -> Callable[[bool], None]: ...
    @typing.overload
    def parmCallback(self, name: str, event_type: ParmEvent, expect_index: bool = ..., **kwargs: object) -> Callable[..., None] | None: ...
    def parmStartCallback(self, name: str, **kwargs: object) -> Callable[[], None]:
        """
        Creates a callback function for the parm start event
        """
    def parmEndCallback(self, name: str, **kwargs: object) -> Callable[[], None]:
        """
        Creates a callback function for the parm start event
        """
    def postParmChangedEvent(self, name: str, *args: object, **kwargs: object) -> None:
        """
        Executes the custom callback for a parameter and posts a deferred
        parameter changed event if one has not already been posted for the
        parameter.
        """
    def onParmEvent(self, name: str, event_type: ParmEvent, *args: object, **kwargs: Any) -> None:
        """
        Responds to parameter events, executing the window's generic
        callback function for the provided parameter.
        """
    def onParmStartEvent(self, name: str, **kwargs: object) -> None:
        """
        Responds to parameter start events.
        """
    def onParmEndEvent(self, name: str, **kwargs: object) -> None:
        """
        Responds to parameter start events.
        """
    def triggerParmChangedEvent(self, name: str) -> None:
        """
        Triggers the parm changed event for a parameter.
        """
    def triggerContextMenuAction(self, parm_name: str, action: str, index: int | None = None) -> None:
        """
        Triggers the context menu action event for a parameter
        """
    def triggerParmHotkey(self, name: str, hotkey: str, index: int | None = None) -> None:
        """
        Triggers the parm hotkey event for a parameter
        """

class WidgetBundleConfig(HUDConfig):
    """
    Used to store everything stored by HUDConfig, and also the
    visibility of named widgets added through a WidgetBundleWindow.
    """
    def loadHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None: ...
    def saveHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None: ...

class WidgetBundleUserDataConfig(WidgetBundleConfig):
    """ A config wrapper for storing HUD settings to user data. """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
SliderBundleWindow = WidgetBundleWindow
