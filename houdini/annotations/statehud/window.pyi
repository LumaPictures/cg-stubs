from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, ClassVar, Concatenate, Literal, Never, NotRequired, ParamSpec, Protocol, TypeAlias, TypedDict, TypeVar, Unpack, overload

import hou
import resourceui as rui
import statehud.utils as shu
from PySide6 import QtCore, QtGui, QtWidgets
from statehud.baseconfig import AbstractConfig
from statehud.config import ConfigWrapper
from statehud.parmutils import HUDParm, ParmEvent, _HUDParmSetValue, _HUDParmValue

_P = ParamSpec("_P")
_R = TypeVar("_R")
_ParmT = TypeVar("_ParmT", bound=HUDParm)

class _ParmUpdater(Protocol):
    def __call__(self, fn: Callable[_P, _R], /) -> Callable[_P, _R]: ...

# What WidgetBundleWindow.onParmEvent() passes its callback: the parm's, and the keywords of
# the event (parmCallback()'s, the context menu's `action`, ...).
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

class _PrefixKwargs(TypedDict, total=False):
    prefix: str | None

class _MultiChangeCallback(Protocol):
    def __call__(self, driver_name: str, started: bool, names: list[str] = ..., /) -> object: ...

# HUDParm.executeCallback() passes a callback as many of the event's arguments as it takes; a
# widget's toggle reports QCheckBox.stateChanged's int.
_ToggleCallback: TypeAlias = Callable[[], object] | Callable[[int], object]

# A callback that takes whatever a widget's signal emits: what parmCallback() makes for a Changed
# event without expect_index, and ParmWidgetSet._onParmChanged().
class _ParmChangedCallback(Protocol):
    def __call__(self, *args: object) -> None: ...

# One of the callbacks parmCallback() makes, depending on the event type and expect_index.
_ParmEventCallback: TypeAlias = (
    _ParmChangedCallback
    | Callable[Concatenate[int, ...], None]
    | Callable[[str], None]
    | Callable[[int, str], None]
    | Callable[[bool], None]
)

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
    windowVisibility: ClassVar[QtCore.Signal]
    scene_viewer: hou.SceneViewer
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        default_size: int | None = ...,
        full_resize: bool = ...,
        auto_resize: bool = ...,
        title: str | None = ...,
        title_alignment: QtCore.Qt.AlignmentFlag = ...,
        bold_title: bool = ...,
    ) -> None: ...
    def setWindowSetting(self, window: object, pref_name: str, pref_val: object) -> None: ...
    def changeVisualSize(self, visual_size_index: int, defer: bool = ...) -> None: ...
    def setDrawBackgroundState(self, pref_value: bool) -> None: ...
    def isDrawBackgroundEnabled(self) -> bool: ...
    def setDrawBackgroundColor(self, color: tuple[float, float, float, float]) -> None: ...
    def drawBackgroundColor(self) -> hou.Color | tuple[float, float, float, float]: ...
    def setDrawLabelColor(self, color: tuple[float, float, float, float]) -> None: ...
    def drawLabelColor(self) -> hou.Color | tuple[float, float, float, float]: ...
    def setShadowEffectState(self, pref_value: bool) -> None: ...
    def hasShadowEffect(self) -> bool: ...
    def openPreferences(self) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def isClosed(self) -> bool: ...
    def show(self, value: bool = ...) -> None: ...
    def isVisible(self, check_embedded: bool = ...) -> bool: ...
    def setEmbedded(self, value: bool) -> None: ...
    def embedded(self) -> bool: ...
    def isValid(self) -> bool: ...
    def loadFromConfig(self, hud_config: "HUDConfig", **kwargs: bool) -> None: ...
    def saveToConfig(self, hud_config: "HUDConfig", **kwargs: bool) -> None: ...
    def addHUDWidget(self, hud_widget: QtWidgets.QWidget, vbox: QtWidgets.QBoxLayout | None = ...) -> None: ...
    def removeHUDWidget(self, hud_widget: QtWidgets.QWidget, vbox: QtWidgets.QBoxLayout | None = ...) -> None: ...
    def hudWidgets(self) -> list[QtWidgets.QWidget]: ...
    def setTitle(self, title: str) -> None: ...
    def title(self) -> str: ...
    def clearContent(self, vbox: QtWidgets.QBoxLayout | None = ...) -> None: ...
    def setEnabledState(self, value: bool) -> None: ...
    def isPosLocked(self) -> bool: ...
    def setLockState(self, value: bool) -> None: ...
    def isMinimized(self) -> bool: ...
    def clearFixedSize(self, defer: bool = ...) -> None: ...
    def revertFixedSize(self, defer: bool = ...) -> None: ...
    def refreshSize(self, defer: bool = ...) -> None: ...
    def autoResize(self, defer: bool = ...) -> bool: ...
    def setMinimizeState(self, value: bool) -> None: ...
    def setMinimizeOverride(self, callback: Callable[[bool], object] | None) -> None: ...
    def isTitleVisible(self) -> bool: ...
    def setTitleVisible(self, value: bool) -> None: ...
    def onDisplayTitleAction(self, value: bool) -> None: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def visualSize(self) -> int: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def windowSize(self) -> QtCore.QSize: ...
    def setWidth(self, new_width: int) -> None: ...
    def setHeight(self, new_height: int) -> None: ...
    def setFullWidth(self, w: int) -> None: ...
    def setFullHeight(self, h: int) -> None: ...
    def getFullWidth(self) -> int: ...
    def getFullHeight(self) -> int: ...
    def restoreFullHeight(self) -> None: ...
    def restoreFullWidth(self) -> None: ...
    def onNewWidth(self, new_width: int) -> None: ...
    def onNewHeight(self, new_height: int) -> None: ...
    def onNewGeometry(self, w: int, h: int, new_pos: QtCore.QPoint) -> None: ...
    def beginResizing(self, region: int | None) -> None: ...
    def endResizing(self) -> None: ...
    def canMove(self) -> bool: ...
    def onWindowPlacement(self, defer: bool = ...) -> None: ...
    def onViewerActivated(self) -> None: ...
    def onViewerDeactivated(self) -> None: ...
    def isPinned(self) -> bool: ...
    def setPinState(self, value: int) -> None: ...
    def setPinManager(self, mgr: shu.PinManager) -> None: ...
    def pinLeft(self) -> None: ...
    def pinRight(self) -> None: ...
    def pinTopRight(self) -> None: ...
    def clearPin(self) -> None: ...
    def getPinState(self) -> int: ...
    def setFadeUnpinned(self, enabled: bool) -> None: ...
    def onMenuAboutToShow(self) -> None: ...
    def onMenuAboutToHide(self) -> None: ...
    def onContextMenu(self, pos: QtCore.QPoint) -> None: ...
    def onHideAction(self) -> None: ...
    def onInitWindow(self) -> None: ...
    def setAutoResize(self, val: bool) -> None: ...
    def isAutoResize(self) -> bool: ...
    def setAutoPosition(self, val: bool) -> None: ...
    def isAutoPosition(self) -> bool: ...
    def shouldAutoPosition(self) -> bool: ...
    def adjustHeaderForTabBar(self, tab_widget: QtWidgets.QTabWidget) -> None: ...
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def onMouseMoveEvent(self, event: QtGui.QMouseEvent, new_pos: QtCore.QPoint) -> None: ...
    def onMouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def onMouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setBackgroundColor(self, col: tuple[float, float, float, float]) -> None: ...
    def backgroundColor(self) -> hou.Color | tuple[float, float, float, float]: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...

class HUDConfig(ConfigWrapper):
    def loadHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None: ...
    def saveHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None: ...

class HUDUserDataConfig(HUDConfig):
    # UserDataConfig's (node, prefix=None).
    @overload
    def __init__(self, *args: Unpack[tuple[hou.Node | None, str | None]], **kwargs: Never) -> None: ...
    @overload
    def __init__(self, *args: Unpack[tuple[hou.Node | None]], **kwargs: Unpack[_PrefixKwargs]) -> None: ...

class WidgetBundleWindow(HUDWindow):
    parmUpdater: ClassVar[_ParmUpdater]
    slider_range: dict[str, float]
    callback: Callable[[_ParmEventDict], object] | None
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        default_size: int | None = ...,
        full_resize: bool = ...,
        auto_resize: bool = ...,
        title: str | None = ...,
        title_alignment: QtCore.Qt.AlignmentFlag = ...,
        bold_title: bool = ...,
        callback: Callable[[_ParmEventDict], object] | None = ...,
        custom_style: bool = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def getParm(self, name: str) -> HUDParm | None: ...
    def addParm(self, parm: _ParmT) -> _ParmT: ...
    def removeParm(self, name: str) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def selectedSliders(self) -> list[str]: ...
    def resetSelectedSliders(self, skip: str | None = ...) -> None: ...
    def bindSelectedMultiChangeCallback(self, callback: _MultiChangeCallback) -> None: ...
    def removeSelectedMultiChangeCallback(self, callback: _MultiChangeCallback) -> None: ...
    def addSliderGrouping(
        self,
        names: list[str],
        modifier: QtCore.Qt.KeyboardModifier | None = ...,
        relative: bool = ...,
        adhoc: bool = ...,
    ) -> shu.SliderGrouping: ...
    def removeGrouping(self, name: str) -> None: ...
    def getGrouping(self, driver: str) -> shu.SliderGrouping | None: ...
    def bindFolder(
        self,
        name: str,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        collapsible: bool = ...,
        collapsed: bool = ...,
        label: str | None = ...,
        label_width: int | None = ...,
    ) -> rui.FolderWidget | rui.CollapsibleFolderWidget: ...
    def wrapAndBindWidget(
        self,
        name: str,
        widget: QtWidgets.QWidget,
        tooltip: str | None = ...,
        label: str | None = ...,
        right_label: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        expanding: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        action_button: shu.ActionButtonManager | None = ...,
        toggle_name: str | None = ...,
        toggle_callback: _ToggleCallback | None = ...,
        toggle_value: bool | None = ...,
        **kwargs: object,
    ) -> rui.HUDWidgetWrapper: ...
    def getWrappedWidget(self, name: str) -> QtWidgets.QWidget | None: ...
    def getWidget(self, name: str) -> QtWidgets.QWidget | None: ...
    def unbindWidget(self, name: str, tab_widget_name: str | None = ..., tab_name: str | None = ...) -> None: ...
    def isTabScrollable(self, tab_widget_name: str, tab_name: str) -> bool: ...
    def bindTabWidget(
        self,
        name: str,
        tab_names: Sequence[str],
        tab_labels: Sequence[str] | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        tab_position: QtWidgets.QTabWidget.TabPosition | None = ...,
        tab_align_end: bool = ...,
        compact_horizontal_tabs: bool = ...,
    ) -> rui.TabWidget: ...
    def addTab(self, tab_widget_name: str, tab_name: str, tab_label: str | None = ...) -> rui.TabWidgetTab: ...
    def setTabLabel(self, tab_widget_name: str, tab_name: str | None, tab_label: str) -> None: ...
    def setTabCurrentIndexFirst(self, tab_widget_name: str) -> None: ...
    def removeTab(self, tab_widget_name: str, tab_name: str) -> None: ...
    def clearFolder(self, folder_widget_name: str) -> None: ...
    def clearTab(self, tab_widget_name: str, tab_name: str | None) -> None: ...
    def clearTabs(self, tab_widget_name: str) -> None: ...
    def getTab(self, tab_widget_name: str, tab_name: str) -> rui.TabWidgetTab | rui.TabWidgetTabNoScroll | None: ...
    def getTabIndex(self, tab_widget_name: str, tab_name: str) -> int: ...
    def setTabTitleMetadata(
        self,
        tab_widget_name: str,
        tab_name: str,
        title: str | None = ...,
        prefix: str | None = ...,
        suffix: str | None = ...,
    ) -> None: ...
    def setTitleFromTabIndex(
        self, tab_widget_name: str, tab_index: int | None = ..., prefix: str | None = ..., suffix: str | None = ...
    ) -> None: ...
    def setTitleFromCurrentTab(self, tab_widget_name: str, prefix: str | None = ..., suffix: str | None = ...) -> None: ...
    def setTitleFromTab(
        self, tab_widget_name: str, tab_name: str, prefix: str | None = ..., suffix: str | None = ...
    ) -> None: ...
    def setTabVisible(self, tab_widget_name: str, tab_name: str, on: bool) -> None: ...
    def isTabVisible(self, tab_widget_name: str, tab_name: str) -> bool: ...
    def setTabEnabled(self, tab_widget_name: str, tab_name: str, on: bool) -> None: ...
    def getCurrentTabName(self, tab_widget_name: str) -> str: ...
    def setCurrentTab(self, tab_widget_name: str, tab_name: str, default_first: bool = ...) -> bool: ...
    def setSliderRange(self, name: str, minimum: float = ..., maximum: float = ...) -> None: ...
    def setSliderCentered(self, name: str) -> None: ...
    def setSlidersCentered(self, sliders: Iterable[str] | None = ...) -> None: ...
    def moveToMouse(
        self,
        under_slider: bool = ...,
        slider_name: str | None = ...,
        defer: bool = ...,
        offset: QtCore.QPoint | None = ...,
    ) -> None: ...
    def connectSliderValueChanged(
        self, slider_name: str, callback: Callable[[float], object] | Callable[[int], object]
    ) -> None: ...
    def show(self, value: bool = ...) -> None: ...
    def updateVisibleWidgets(self) -> None: ...
    def updateVisibleSliders(self, visible_sliders: Iterable[str] | None = ...) -> None: ...
    def setWidgetsVisible(self, widget_list: Iterable[str], on: bool) -> None: ...
    def setWidgetDisabled(self, name: str, val: bool = ...) -> None: ...
    def setWidgetEnabled(self, name: str, val: bool = ...) -> None: ...
    def getWidgetEnabled(self, name: str) -> bool | None: ...
    def bindContextActionCallback(self, callback: Callable[[str, str], object]) -> None: ...
    def bindContextActionMultiCallback(self, callback: Callable[[str, list[str]], object]) -> None: ...
    def removeContextActionCallback(
        self, callback: Callable[[str, str], object] | Callable[[str, list[str]], object]
    ) -> None: ...
    def onContextMenuAction(self, action: str, widget_name: str) -> None: ...
    def bindSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: float = ...,
        max_value: float = ...,
        default_value: float = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        slider_type: type[rui.SliderBase] | None = ...,
        callback: Callable[[float], object] | Callable[[int], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        label_width: float | None = ...,
        toggle_name: str | None = ...,
        toggle_callback: _ToggleCallback | None = ...,
        toggle_value: bool | None = ...,
        **kwargs: object,
    ) -> shu.KeyableSlider: ...
    @overload
    def bindFloatSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: float | list[float] = ...,
        max_value: float | list[float] = ...,
        default_value: float | Sequence[float] | None = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        callback: Callable[[], object] | Callable[[float], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        num_components: Literal[1] = ...,
        use_component_label: bool = ...,
        **kwargs: Any,
    ) -> shu.KeyableSlider: ...
    @overload
    def bindFloatSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: float | list[float] = ...,
        max_value: float | list[float] = ...,
        default_value: float | Sequence[float] | None = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        callback: Callable[[], object] | Callable[[float | hou.Vector2 | hou.Vector3 | hou.Vector4], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        num_components: int = ...,
        use_component_label: bool = ...,
        **kwargs: Any,
    ) -> shu.KeyableSlider | list[shu.KeyableSlider] | None: ...
    def bindFloatSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: float | list[float] = ...,
        max_value: float | list[float] = ...,
        default_value: float | Sequence[float] | None = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        callback: Callable[[], object] | Callable[[float | hou.Vector2 | hou.Vector3 | hou.Vector4], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        num_components: int = ...,
        use_component_label: bool = ...,
        **kwargs: Any,
    ) -> shu.KeyableSlider | list[shu.KeyableSlider] | None: ...
    def bindFloatVector(
        self,
        name: str,
        num_components: int = ...,
        default_value: Sequence[float] | None = ...,
        callback: Callable[[], object] | Callable[[list[float]], object] | None = ...,
        min_value: float | None = ...,
        max_value: float | None = ...,
        min_locked: bool | None = ...,
        max_locked: bool | None = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        **kwargs: Unpack[_VectorBindKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    @overload
    def bindIntSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: int | list[int] = ...,
        max_value: int | list[int] = ...,
        default_value: int | Sequence[int] | None = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        callback: Callable[[], object] | Callable[[int], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        num_components: Literal[1] = ...,
        **kwargs: Any,
    ) -> shu.KeyableSlider: ...
    @overload
    def bindIntSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: int | list[int] = ...,
        max_value: int | list[int] = ...,
        default_value: int | Sequence[int] | None = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        callback: Callable[[], object] | Callable[[int | list[int]], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        num_components: int = ...,
        **kwargs: Any,
    ) -> shu.KeyableSlider | list[shu.KeyableSlider] | None: ...
    def bindIntSlider(
        self,
        name: str,
        label: str | None = ...,
        min_value: int | list[int] = ...,
        max_value: int | list[int] = ...,
        default_value: int | Sequence[int] | None = ...,
        min_locked: bool = ...,
        max_locked: bool = ...,
        tooltip: str | None = ...,
        hide_slider: bool = ...,
        keep_slider_space: bool = ...,
        bind_context_menu: bool = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        use_mouse_wheel: bool = ...,
        callback: Callable[[], object] | Callable[[int | list[int]], object] | None = ...,
        selectable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        num_components: int = ...,
        **kwargs: Any,
    ) -> shu.KeyableSlider | list[shu.KeyableSlider] | None: ...
    def bindIntVector(
        self,
        name: str,
        num_components: int = ...,
        default_value: Sequence[int] | None = ...,
        callback: Callable[[], object] | Callable[[list[int]], object] | None = ...,
        min_value: float | None = ...,
        max_value: float | None = ...,
        min_locked: bool | None = ...,
        max_locked: bool | None = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        **kwargs: Unpack[_VectorBindKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    def createActionButton(
        self,
        name: str,
        iconpath: str | None,
        callback: Callable[[bool], object] | None = ...,
        tooltip: str | None = ...,
    ) -> shu.ActionButtonManager: ...
    def bindButton(
        self,
        name: str,
        label: str,
        callback: Callable[[], object] | Callable[[bool], object] | None = ...,
        tooltip: str | None = ...,
        front_label: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        **kwargs: Unpack[_WrapAndBindExtraKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    def bindComboBox(
        self,
        name: str,
        items: Sequence[str],
        callback: Callable[[], object] | Callable[[int], object] | None = ...,
        tooltip: str | None = ...,
        label: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        **kwargs: Unpack[_WrapAndBindExtraKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    def updateComboBoxItems(self, name: str, items: Sequence[str]) -> None: ...
    def bindColorField(
        self,
        name: str,
        label: str,
        default_value: QtGui.QColor | None = ...,
        callback: Callable[[QtGui.QColor], object] | None = ...,
        tooltip: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> rui.HUDWidgetWrapper: ...
    def bindFileLineEdit(
        self,
        name: str,
        label: str,
        callback: Callable[[str], object] | None = ...,
        tooltip: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> rui.HUDWidgetWrapper: ...
    def bindSeparator(
        self,
        name: str,
        label_width: int | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> rui.HUDWidgetWrapper: ...
    def bindInputStringField(
        self,
        name: str,
        value: str,
        menu: QtWidgets.QMenu | None = ...,
        menu_callback: Callable[..., object] | None = ...,
        callback: Callable[[], object] | Callable[[list[str]], object] | None = ...,
        tooltip: str | None = ...,
        label: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        expanding: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        field_width: int | None = ...,
        action_button: shu.ActionButtonManager | None = ...,
        **kwargs: Unpack[_WrapAndBindKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    def bindFieldLabel(
        self,
        name: str,
        text: str,
        tooltip: str | None = ...,
        max_width: int | None = ...,
        label: str | None = ...,
        label_width: int | None = ...,
        centered: bool = ...,
        bold_font: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        **kwargs: Unpack[_WrapAndBindExtraKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    def bindButtonStrip(
        self,
        name: str,
        button_names: list[str],
        button_labels: list[str] | None = ...,
        callback: Callable[[], object] | Callable[[str], object] | Callable[[str, bool], object] | None = ...,
        tooltip: str | None = ...,
        allow_multi_selection: bool = ...,
        iconpaths: Sequence[str] | None = ...,
        off_iconpaths: Sequence[str | None] | None = ...,
        label: str | None = ...,
        label_width: int | None = ...,
        align_left: bool = ...,
        centered: bool = ...,
        checkable: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        button_tooltips: Sequence[str] = ...,
        **kwargs: Unpack[_WrapAndBindExtraKwargs],
    ) -> rui.HUDWidgetWrapper: ...
    def bindToggle(
        self,
        name: str,
        label: str,
        default_value: bool = ...,
        callback: Callable[[], object] | Callable[[bool], object] | None = ...,
        tooltip: str | None = ...,
        front_label: str | None = ...,
        label_width: int | None = ...,
        mouse_hotkeys: Mapping[tuple[int, int], str] | None = ...,
        centered: bool = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        **kwargs: object,
    ) -> shu.KeyableToggle: ...
    def isUpdatingValue(self) -> bool: ...
    def updateSliderValue(
        self, slider_name: str, value: float, update_slider_position: bool = ..., relative: bool = ...
    ) -> None: ...
    def getSliderValue(self, slider_name: str) -> float: ...
    def getFloatSliderValue(self, slider_name: str) -> float: ...
    def getFloatValue(
        self, parm_name: str, num_components: int = ..., is_vector: bool = ...
    ) -> float | hou.Vector2 | hou.Vector3 | hou.Vector4 | list[float] | None: ...
    def setFloatValue(
        self, name: str, value: float | Sequence[float], num_components: int = ..., is_vector: bool = ...
    ) -> None: ...
    def getIntSliderValue(self, slider_name: str) -> int: ...
    def getIntValue(self, parm_name: str, num_components: int = ..., is_vector: bool = ...) -> int | list[int] | None: ...
    def setIntValue(
        self, name: str, value: int | Sequence[int], num_components: int = ..., is_vector: bool = ...
    ) -> None: ...
    def getToggleState(self, name: str, outer_name: str | None = ...) -> bool: ...
    def setToggleState(self, name: str, on: bool, outer_name: str | None = ...) -> None: ...
    def getButtonStripState(self, widget_name: str) -> str | list[str] | None: ...
    def setButtonStripState(self, widget_name: str, button_name: str | None = ..., on: bool = ...) -> None: ...
    def getButtonStripValue(self, widget_name: str) -> int | None: ...
    def setButtonStripValue(self, widget_name: str, value: int) -> None: ...
    def setColorFieldState(self, widget_name: str, color: QtGui.QColor) -> None: ...
    def getColorFieldState(self, widget_name: str) -> QtGui.QColor | None: ...
    @overload
    def getComboBoxState(self, widget_name: str, as_int: Literal[True] = ...) -> int | None: ...
    @overload
    def getComboBoxState(self, widget_name: str, as_int: bool) -> int | str | None: ...
    def getComboBoxState(self, widget_name: str, as_int: bool = ...) -> int | str | None: ...
    def setComboBoxState(self, widget_name: str, index: int) -> None: ...
    def getInputStringFieldState(self, widget_name: str) -> str | None: ...
    def setInputStringFieldState(self, widget_name: str, value: str) -> None: ...
    def getFileLineEditState(self, widget_name: str) -> str | None: ...
    def setFileLineEditState(self, widget_name: str, value: str) -> None: ...
    def getFieldLabelText(self, widget_name: str) -> str | None: ...
    def setFieldLabelText(self, widget_name: str, text: str) -> None: ...
    def getParmValue(self, name: str, menus_as_int: bool = ...) -> _HUDParmValue: ...
    def setParmValue(self, name: str, value: _HUDParmSetValue) -> None: ...
    def loadParmFromConfig(self, name: str, config: AbstractConfig, prefix: str = ...) -> None: ...
    def saveParmToConfig(self, name: str, config: AbstractConfig, prefix: str = ...) -> None: ...
    @overload
    def parmCallback(
        self,
        name: str,
        event_type: Literal[ParmEvent.Changed] = ...,
        expect_index: Literal[False] = ...,
        **kwargs: object,
    ) -> _ParmChangedCallback: ...
    @overload
    def parmCallback(
        self, name: str, event_type: Literal[ParmEvent.Changed], expect_index: Literal[True], **kwargs: object
    ) -> Callable[Concatenate[int, ...], None]: ...
    @overload
    def parmCallback(
        self, name: str, event_type: Literal[ParmEvent.Changed] = ..., *, expect_index: Literal[True], **kwargs: object
    ) -> Callable[Concatenate[int, ...], None]: ...
    @overload
    def parmCallback(
        self,
        name: str,
        event_type: Literal[ParmEvent.HotkeyInvoked],
        expect_index: Literal[False] = ...,
        **kwargs: object,
    ) -> Callable[[str], None]: ...
    @overload
    def parmCallback(
        self, name: str, event_type: Literal[ParmEvent.HotkeyInvoked], expect_index: Literal[True], **kwargs: object
    ) -> Callable[[int, str], None]: ...
    @overload
    def parmCallback(
        self, name: str, event_type: Literal[ParmEvent.SelectionChanged], expect_index: bool = ..., **kwargs: object
    ) -> Callable[[bool], None]: ...
    @overload
    def parmCallback(
        self, name: str, event_type: ParmEvent, expect_index: bool = ..., **kwargs: object
    ) -> _ParmEventCallback | None: ...
    def parmCallback(
        self, name: str, event_type: ParmEvent = ..., expect_index: bool = ..., **kwargs: object
    ) -> _ParmEventCallback | None: ...
    def parmStartCallback(self, name: str, **kwargs: object) -> Callable[[], None]: ...
    def parmEndCallback(self, name: str, **kwargs: object) -> Callable[[], None]: ...
    def postParmChangedEvent(self, name: str, *args: object, **kwargs: object) -> None: ...
    def onParmEvent(self, name: str, event_type: ParmEvent, *args: object, **kwargs: Any) -> None: ...
    def onParmStartEvent(self, name: str, **kwargs: object) -> None: ...
    def onParmEndEvent(self, name: str, **kwargs: object) -> None: ...
    def triggerParmChangedEvent(self, name: str) -> None: ...
    def triggerContextMenuAction(self, parm_name: str, action: str, index: int | None = ...) -> None: ...
    def triggerParmHotkey(self, name: str, hotkey: str, index: int | None = ...) -> None: ...

class WidgetBundleConfig(HUDConfig):
    def loadHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None: ...
    def saveHUDSettings(self, hud_window: HUDWindow, **kwargs: bool) -> None: ...

class WidgetBundleUserDataConfig(WidgetBundleConfig):
    # UserDataConfig's (node, prefix=None).
    @overload
    def __init__(self, *args: Unpack[tuple[hou.Node | None, str | None]], **kwargs: Never) -> None: ...
    @overload
    def __init__(self, *args: Unpack[tuple[hou.Node | None]], **kwargs: Unpack[_PrefixKwargs]) -> None: ...

# The keywords wrapAndBindWidget() takes beyond those its bind*() callers already pass it.
class _WrapAndBindKwargs(TypedDict, total=False):
    right_label: str | None
    toggle_name: str | None
    toggle_callback: _ToggleCallback | None
    toggle_value: bool | None
    create_widget_shadow: bool

# The keywords wrapAndBindWidget() takes beyond those bindButton(), bindComboBox(),
# bindFieldLabel() and bindButtonStrip() already pass it.
class _WrapAndBindExtraKwargs(_WrapAndBindKwargs, total=False):
    expanding: bool
    action_button: shu.ActionButtonManager | None

# The keywords wrapAndBindWidget() takes beyond the tab that bindFloatVector() and
# bindIntVector() already pass it.
class _VectorBindKwargs(_WrapAndBindExtraKwargs, total=False):
    tooltip: str | None
    label: str | None
    label_width: int | None
    centered: bool
