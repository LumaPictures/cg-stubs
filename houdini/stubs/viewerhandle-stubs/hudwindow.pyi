import hou
import resourceui as rui
from collections.abc import Collection, Sequence
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import Any, ClassVar
from viewerhandle import hudapi as hudapi
from viewerhandle.hudapi import HUDWidgetBase as HUDWidgetBase, _HUDDebugInfo, _HUDHandle
from viewerhandle.hudmanager import HUDWindowManager as HUDWindowManager
from viewerhandle.hudutils import HUDDockable as HUDDockable

HUD_TOGGLE_DISPLAY_SYM: str
HUD_TOGGLE_LOCKING_SYM: str
HUD_STACK_WINDOWS_SYM: str
HUD_DOCK_WINDOWS_SYM: str
HUD_UNDOCK_WINDOWS_SYM: str
PARM_EVENTS: tuple[hou.EnumValue[hou.nodeEventType], ...]
COLOR_TONE_FACTOR: float
DEFAULT_COLOR_BG: tuple[float, float, float, float]
VISIBLE_STATE_ACTION_ID: str

class HUDWindow(hou.qt.ViewerOverlay):
    """ The HUD Handle window is the viewer overlay holding one or
        multiple HUD widgets.

        key: The window unique id
        handle: The handle impl object.
        target_parm: The handle target node parm. Maybe be None if the
                     handle is dynamic.
        scene_viewer: The active scene viewer.
        visual_size: The current visual size.

        Note: HUD widget has a different hou.Handle instancem,
              self._handle should only be used for accessing the
              handle template information. Use self._hud_widget
              to access the run-time info.
    """
    all_huds_menu: QtWidgets.QMenu
    lookChanged: ClassVar[QtCore.Signal]
    DEFAULT_TITLE_NAME: str
    class WindowBar(rui.WindowBar):
        """ Override WindowBar to draw a red dot for persistent
            handles.
        """
        def __init__(self, **kwargs: Any) -> None: ...
        def backgroundColor(self) -> tuple[float, float, float, float]:
            """ Override background color if disabled.
            """
        def setAsPersistent(self, value: bool) -> None: ...
        def isPersistent(self) -> bool: ...
        def lock(self, value: bool) -> None: ...
        def paintEvent(self, paint_event: QtGui.QPaintEvent) -> None: ...
    class WindowTitle(rui.LabelEdit):
        def __init__(self, **kwargs: Any) -> None: ...
        def shadow(self) -> QtWidgets.QGraphicsDropShadowEffect: ...
    class ToolBar(rui.ToolBar):
        def __init__(self, **kwargs: Any) -> None: ...
        def onLookChanged(self) -> None: ...
    def __init__(self, key: str, handle: _HUDHandle, target_parm: hou.Parm | None, scene_viewer: hou.SceneViewer, visual_size: int) -> None: ...
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool: ...
    def terminate(self) -> None: ...
    def debug(self) -> _HUDDebugInfo: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def enterEvent(self, event: QtGui.QEnterEvent) -> None: ...
    def leaveEvent(self, event: QtCore.QEvent) -> None: ...
    def hasQtWidget(self, widget: QtWidgets.QWidget) -> bool: ...
    def windowSize(self) -> QtCore.QSize: ...
    def isValid(self) -> bool:
        """ Return True if the HUD widget and its HOM object are
            valid.
        """
    def isPersistent(self) -> bool: ...
    def setAsPersistent(self, value: bool) -> None: ...
    def toolTip(self) -> str | None: ...
    def handle(self) -> _HUDHandle | None: ...
    def nodeType(self) -> str | None: ...
    def node(self) -> hou.OpNode | None: ...
    def setDrawBackgroundState(self, value: bool) -> None: ...
    def isDrawBackgroundEnabled(self) -> bool: ...
    def setSlidersVisible(self, value: bool) -> None: ...
    def areSlidersVisible(self) -> bool: ...
    def setTrackpadSliderVisible(self, value: bool) -> None: ...
    def isTrackpadSliderVisible(self) -> bool: ...
    def setLabelVisibleState(self, value: bool) -> None: ...
    def labelVisibleState(self) -> bool: ...
    def drawLabelColor(self) -> tuple[float, ...] | hou.Color: ...
    def setDrawLabelColor(self, color: tuple[float, ...]) -> None: ...
    def drawBackgroundColor(self) -> tuple[float, ...] | hou.Color: ...
    def setDrawBackgroundColor(self, color: tuple[float, ...]) -> None: ...
    def setShadowEffectState(self, value: bool) -> None: ...
    def hasShadowEffect(self) -> bool | None: ...
    def addHUDWidget(self, hud_widget: HUDWidgetBase) -> None:
        """ Add HUD handle widgets to the grid layout.
        """
    def hudWidget(self) -> HUDWidgetBase | None: ...
    def parm(self) -> hou.Parm | None: ...
    def setDeferredAction(self, action_id: str) -> None: ...
    def unsetDeferredAction(self, action_id: str) -> None: ...
    def isActionDeferred(self, action_id: str) -> bool: ...
    def key(self) -> str: ...
    def onEditTitle(self, title: str) -> None:
        """ Slot that handles title edits.
        """
    def setTitle(self, value: str) -> None:
        """ Set title visibility.
        """
    def title(self) -> str:
        """ Retrieve the window title.
        """
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """ Called by QWidget.close()
        """
    def clearContent(self) -> None: ...
    def isActive(self) -> bool:
        """ Returns True if the window has been activated.
            Note: The window active state may not be in sync
                  with hou.Handle.isActive() which can be active
                  before the window is activated.
        """
    def activate(self) -> None:
        """ Called by the HUD manager when the HUD window is ready to
            be activated.
        """
    def deactivate(self) -> None:
        """ Call when the window is ready to be deactivated
        """
    def isLocked(self) -> bool:
        """ Check whether the window is locked.
        """
    def hide(self) -> None:
        """ Hide this HUD and dockees if visible. Use unhide
            to show it back.
        """
    def unhide(self) -> None:
        """ Unhide this HUD and dockees if previously hidden
            with hide.
        """
    def setVisibleState(self, value: bool, defer: bool = True) -> None:
        """ Set the window visibility setting.
            All HUD widgets are updated at once.

            `value`: True to show.

            `defer`: True to defer the execution. Typically used when the
                     handles are displayed from the viewport show handle
                     menu.
        """
    def updateVisibility(self, value: bool, defer: bool = True) -> None:
        """ Update window visibility.

            `value`: True to show

            `defer`: True to defer the execution. Typically used when the
                     handles are displayed from the viewport show handle
                     menu.
        """
    def onDeferUpdateVisibility(self) -> None: ...
    def setEnabledState(self, value: bool) -> None: ...
    def setLockedState(self, value: bool) -> None:
        """ Callback invoked when the locking state is changed in the cache.
        """
    def setHUDLockedState(self, value: bool) -> None:
        """ Lock all parms mapped to the Handle.

         NOTE:
            Skip the lock change events processing while locking
            the parms.
        """
    def canLockHUD(self) -> bool: ...
    def lockParm(self, parm: hou.Parm | hou.ParmTuple | None, value: bool) -> None: ...
    def setKeyFrame(self) -> None: ...
    def removeKeyFrame(self) -> None: ...
    def makeHUDAsDefault(self) -> None: ...
    def revertHUDToDefault(self) -> None: ...
    def revertHUDToFactoryDefault(self) -> None: ...
    def exportHUDHandle(self) -> None: ...
    def exportHUDParms(self) -> None: ...
    def setVisualSize(self, visual_size: int) -> None: ...
    def visualSize(self) -> int: ...
    def makePersistent(self, value: bool) -> None:
        """ Make the HUD persistent along with other sibling HUDs
            if the HUD is docked.
        """
    def setCompactState(self, value: bool | int) -> None: ...
    def isTitleVisible(self) -> bool:
        """ Retrieves whether the title is visible.
        """
    def setTitleVisible(self, value: bool, defer: bool = True) -> None:
        """ Callback invoked when the title visibility is changed in the cache.
        """
    def isTitleVisibleWhenDocked(self) -> bool: ...
    def setTitleVisibleWhenDockedState(self, value: bool, defer: bool = True) -> None:
        """ Set the title visibility when docked state.
        """
    def isToolbarVisible(self) -> bool:
        """ Retrieves whether the toolbar is visible.
        """
    def setToolbarVisible(self, value: bool, defer: bool = True) -> None:
        """ Callback invoked when the toolbar visibility is changed in the cache.
        """
    def setDocker(self, value: str | None) -> None:
        """ Updates the docker window according to the settings cache.
        """
    def setDockee(self, value: str | None) -> None:
        """ Updates the dockee window according to the settings cache.
        """
    def dockee(self) -> HUDWindow | None:
        """ Return the window docked to ourself
            i.e. the window below.
        """
    def docker(self) -> HUDWindow | None:
        """ Return the window we are docked to
            i.e the window above.
        """
    def hasDockee(self, dockee_win: HUDWindow) -> bool: ...
    def isTopDocker(self) -> bool: ...
    def isDocker(self) -> bool:
        """ Return True if we are not docked to a window and a window
            is docked to ourself (dockee)
        """
    def isDockee(self) -> bool:
        """ Return True if we are a dockee (a window docked to the
            window above)
        """
    def isDocked(self) -> bool:
        """ Return True if we are a dockee or a docker
        """
    def isInsideDocked(self) -> bool:
        """ Return True if we are docked from above and below.
        """
    def canDisplayVisuals(self) -> bool:
        """ Returns True if the HUD can display top visual elements
            like a toolbar or the window title. Basically, this
            method makes sure visual elements can be shown on a
            top docker or regular HUD window only. Dockee windows
            don't show any visuals other than their UI controls.
        """
    def canDisplayTitle(self) -> bool:
        """ Returns True if the HUD can display the title.
        """
    def canDisplayToolbar(self) -> bool:
        """ Returns True if the HUD should display the toolbar.
        """
    def undock(self, y_spacing: int = -1) -> None:
        """ Undock from the docker if we are a dockee, undock
            from the dockee if we are a docker.
        """
    def undockFrom(self) -> None:
        """ Undock from the docker and dockees. Dock old dockee to
            old docker.
        """
    def dockTo(self, docker_key: str | None, dockee_key: str | None) -> None:
        """ Dock to a docker and dockee
        """
    def dock(self) -> None:
        """ Dock elements on the docking list
        """
    def computeDistance(self, x: float, y: float) -> list[float]: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def backgroundColor(self) -> tuple[float, ...] | hou.Color:
        """ Return the background color as a rgba tuple.
        """
    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """ Draw the window background with rounded corners.
            docker: top rounded corners
            dockee: bottom rounded corners
            enclosed: all flat corners
        """
    def onNewGeometry(self, width: int, height: int, pos: QtCore.QPoint) -> None:
        """ Called by ResizeGrip when a new geometry has
            been computed during a drag operation.

            Resize only occurs horizontally, so we ignore
            height and y-pos of new geometry.
        """
    def canMove(self) -> bool:
        """ Return true if we are movable.
        """
    def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Called by the WindowBar widget on mouse down. Prepare the
            window for docking if the SHIFT key is pressed or prepare
            the window for undocking if the CTRL key is pressed.
        """
    def onMouseMoveEvent(self, event: QtGui.QMouseEvent, new_pos: QtCore.QPoint) -> None:
        """ Called by the WindowBar widget when the mouse is moving.
            The window is moved to the new position computed by the
            WindowBar widget. The nearest window is grabbed for docking
            while the SHIFT key is pressed.

            event: mouse event object
            new_pos: position computed by the WindowBar widget to
                     move the window to.
        """
    def onMouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Called by the WindowBar widget when the mouse is released.
            Dock the window collected earlier if the SHIFT key is
            pressed or undock the window if the CTRL key is pressed.

            event: mouse event object
        """
    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """ Override to synchronize position settings.
        """
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """ Override to synchronize size settings.
        """
    def onColorSchemeChanged(self) -> None: ...
    def onViewerActivated(self) -> None:
        """ Override to unhide the entire dock stack.
        """
    def onViewerDeactivated(self) -> None:
        """ Override to hide the entire dock stack.
        """
    def onPlaybarEvent(self, event_type: hou.EnumValue[hou.playbarEvent], frame: float) -> None: ...
    def onNodeParmChangeEvent(self, event_type: hou.EnumValue[hou.nodeEventType], **kwargs: Any) -> None: ...
    def logMe(self) -> None: ...
    def onMenuAboutToShow(self) -> None: ...
    def onMenuAboutToHide(self) -> None: ...
    def onMoveAllWindowsToHome(self) -> None:
        """ Move all HUDs to the viewer bottom-left.
        """
    def onDockAllWindows(self) -> None:
        """ Dock all windows in the viewer in one single HUD.
        """
    def onUndockAllWindows(self) -> None:
        """ Undock all windows in the viewer.
        """
    def onContextMenu(self, pos: QtCore.QPoint) -> None: ...
    def onDeleteAction(self) -> None:
        """ Delete this window, its handles and the cache entry.
        """
    def onPersistAction(self) -> None: ...
    def onDisplayAction(self, value: bool) -> None:
        """ Show/Hide all dockees
        """
    def onToggleWindowsVisibleState(self) -> None: ...
    def onDisplayTitleAction(self, value: bool) -> None:
        """ Show/Hide title.
        """
    def onDisplayToolbarAction(self, value: bool) -> None:
        """ Show/Hide toolbar.
        """
    def onLockWindowAction(self) -> None:
        """ Lock/unlock all dockees.
        """
    def onIndirectMouseAction(self, value: bool) -> None:
        """ Enable or disable indirect mouse manipulation.

            Updates the underlying handle, and all docked handles
            if present, by setting their HUD_INDIRECTMOUSE setting
            to the given value.
        """
    def onToggleWindowsLockedState(self) -> None: ...
    def onLockHUDAction(self, value: bool) -> None:
        """ Lock parms of the underlying HUD along with its dockees if
            it's a docker.
        """
    def onMakeHUDAsDefaultAction(self) -> None:
        """ Make the current HUD parms as the new default
        """
    def onRevertHUDToDefaultAction(self) -> None:
        """ Revert the HUD parms to the default
        """
    def onRevertHUDToFactoryDefaultAction(self) -> None:
        """ Revert the HUD parms to the factory default
        """
    def onExportHUDParmsAction(self) -> None: ...
    def onExportHUDHandleAction(self) -> None: ...
    def onUpdateHUDPrefsAction(self) -> None: ...
    def onSetKeyFrameAction(self) -> None: ...
    def onRemoveKeyFrameAction(self) -> None: ...
    def onLogWindowAction(self) -> None: ...
    def onChangeVisualSizeAction(self) -> None: ...
    def onCompactAction(self) -> None: ...
    def onEditSettingsAction(self) -> None: ...
    def onDockAllAction(self) -> None:
        """ Dock all windows in the viewer to this HUD
        """
    def onUndockStackAction(self) -> None:
        """ Undock this HUD and its dockees.
        """
    def onUndockAction(self) -> None: ...
    def constrainPosition(self) -> None:
        """ Constrain the window position within its parent's
            rectangle.
        """
    def onInitWindow(self) -> None:
        """ Override the base implementation.
        """
    def onBeginResize(self) -> None:
        """ Override to ensure the call occurs only once on the top docker.
        """
    def onEndResize(self) -> None:
        """ Override to ensure the call occurs only once on the top docker.
        """
    def onResizing(self) -> None:
        """ Override to ensure the call occurs only once on the top docker.
        """
    def onSizeChanged(self) -> None:
        """ Override to ensure the call occurs only once on the top docker.
        """
    def onLayoutChanged(self) -> None:
        """ Override to ensure the call occurs only once on the top docker.
        """
    def onWindowPlacement(self) -> None:
        """ Custom implementation to deal with window docking when
            the viewer is resizing or moving.
        """
    def onMoveContainerWindow(self, new_pos: QtCore.QPoint, old_pos: QtCore.QPoint) -> None:
        """ Override to ensure the call occurs only once on the top docker.
        """
    def moveTo(self, pos: QtCore.QPoint | None) -> None:
        """ Move the window and all dockees to the position 'pos'.
        """
    def moveBy(self, delta: QtCore.QPoint | None) -> None:
        """ Move the window and all dockees by offset 'delta'.
        """
    def setWidth(self, new_width: int) -> None:
        """ Set the entire docked window stack with a new width.
        """
    def updateActions(self) -> None: ...
    def onSettingEvent(self, event: int, **kwargs: Any) -> None: ...

def windowManager() -> HUDWindowManager: ...
def constrainWindow(win: HUDWindow | None) -> QtCore.QPoint | None:
    """ Constrain the window position to the viewer
        boundaries.

        Returns a delta position suitable for
        HUDWindow.moveBy
    """
def dockWindows(docker_win: HUDWindow, dockee_wins: Sequence[HUDWindow], update: bool = True) -> HUDWindow: ...
def undockWindows(windows: Sequence[HUDWindow]) -> None: ...
def changeWindowsVisualSize(windows: Collection[HUDWindow], visual_size_index: int, defer: bool) -> None: ...
def stackWindows(windows: Sequence[HUDWindow]) -> None: ...
def setWindowVisibleState(win: HUDWindow, value: bool) -> None:
    """ Set a HUD window visible state with undo support.
    """
def setWindowLockedState(win: HUDWindow, value: bool, defer: bool = True) -> None:
    """ Set a HUD window locked state with undo support.
    """
