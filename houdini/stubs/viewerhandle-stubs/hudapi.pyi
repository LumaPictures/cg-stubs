import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from collections.abc import Iterable, Mapping
from houtypes import ViewerHandleKwargs, ViewerHandleParmChangeKwargs, ViewerParmProperties
from hutil.PySide import QtWidgets
from typing import Any, Callable, Generic, NotRequired, Protocol, Required, Unpack
from typing_extensions import TypedDict
from viewerhandle.hudmanager import HUDWindowManager
from viewerhandle.hudwidgets import SettingDialog
from viewerhandle.hudwindow import HUDWindow as HUDWindow

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_HUDSettingValue: TypeAlias = int | float | str
_W = TypeVar('_W', bound='HUDWidgetBase')
__all__ = ['HUDWindow']

class _HUDHandle(Protocol):
    def parms(self) -> dict[str, ViewerParmProperties]: ...
    def object(self) -> hou.Handle: ...

class _CreateHUDWidgetOptions(TypedDict, Generic[_W], total=False):
    hud_widget_type: Required[type[_W]]
    kwargs: dict[str, Any]

class _HUDSettings(TypedDict, total=False, extra_items=_HUDSettingValue):  # type: ignore[call-arg]
    hudid: str
    huddockee: str
    huddocker: str
    hudtitle: str
    hudx: int
    hudy: int
    hudwidth: int
    hudheight: int
    hudlocked: int
    visible: int
    hudtitlevisible: int
    hudtoolbarvisible: int
    huddocking: str
    hudcachevalue: str
    hudbindingargs: str
    hudplacingmode: int
    handleindirectmouse: int
    hudparmmin: str
    hudparmmax: str
    hudparmdefault: int | str
    hudparmlabel: str
    hudparmminlock: str
    hudparmmaxlock: str
    huduseparmrange: int
    hudparmordering: str
    hudbtntype: str
    hudbtntext: str
    hudbtnicon: str
    hudbtntooltip: str
    hudbtntogglestate: str
    hudbtnradiostrip: int
    hudbtnradiostripdefault: int
    hudmenulabels: str
    hudmenuitems: str
    hudmenudefault: int

class _HUDParmChangeKwargs(TypedDict):
    parm_name: str
    parm_value: Any

class _HUDParmAnimatedKwargs(TypedDict):
    node: hou.OpNode
    parm_tuple: hou.ParmTuple

class _HUDParmTemplateChangeKwargs(TypedDict):
    node: NotRequired[hou.OpNode]
    parm_template: hou.ParmTemplate | None
    parm_label_hidden: bool
    parm_label_changed: list[str] | None

class _HUDDebugInfo(TypedDict):
    hudplacingmode: int
    hudnodetype: str | None
    hudhandlename: str | None
    hudid: str
    huddockee: str
    huddocker: str
    hudtitle: str
    hudlocked: bool
    visible: bool
    hudtitlevisible: bool
    hudtoolbarvisible: bool
    hudx: int
    hudy: int
    hudwidth: int
    hudheight: int

class _MouseIndirectUpdateOptions(TypedDict, total=False):
    mouse_pos: tuple[float, float]
    index: int

class _MouseIndirectStartOptions(TypedDict, total=False):
    mouse_pos: tuple[float, float]

def applyStyle(style: PySide6.QtWidgets.QStyle, child_widget: PySide6.QtWidgets.QWidget) -> None:
    """Apply the given style to the widget and its descendents.
    """

class HUDWidgetBase(QtWidgets.QWidget):
    """ Base class for HUD Handle widgets. HUD widgets are used by
        HUD handle to manipulate a node parm.

        handle:         The HUD python handle instance.
        target_parm:    The parm targeted by the HUD handle. May be
                        set to None if the HUD python handle is
                        dynamically bound to a python state.
        hud_widget_key: Widget ID computed by the HUD framework.
        window_key:     Widget's containing window ID computed by the
                        HUD framework.
        parent:         The widget window parent.
    """
    def __init__(self, handle: _HUDHandle, target_parm: hou.Parm | None, hud_widget_key: str, window_key: str, parent: HUDWindow | None) -> None: ...
    def applyStyle(self, child_widget: PySide6.QtWidgets.QWidget) -> None:
        """Apply the HUD widget's style to the given child/descendant widget.
        """
    def setVisualSize(self, visual_size: int) -> None:
        """ Update the visual size of the widget. There is no need to
            override this method, updateVisualSize should be
            implemented by the derived class instead.
        """
    def visualSize(self) -> int: ...
    def key(self) -> str:
        """ The HUD widget unique id.
        """
    def windowKey(self) -> str:
        """ The HUD widget window unique id.
        """
    def handle(self) -> _HUDHandle:
        """ Return the HUD python handle instance created by Houdini.
        """
    def sceneViewer(self) -> hou.SceneViewer:
        """ Return the scene viewer this HUD widget belongs to.
        """
    def parm(self) -> hou.Parm | None:
        """ Return the parm targeted by this HUD widget.
        """
    def supportKeyFrames(self) -> bool:
        """ Return True if the HUD widgets can set or remove key
            frames on the target parm.
        """
    def setKeyFrame(self) -> None:
        """ Set a key frame on the target parm. Must be implemented by
            the derived class.
        """
    def removeKeyFrame(self) -> None:
        """ Remove a key frame on the target parm. Must be implemented
            by the derived class.
        """
    def hasKeyFrame(self, frame: float | None) -> bool:
        """ Return True if the target parm has a key at frame.
            Must be implemented by the derived class.
        """
    def hasPendingChange(self) -> bool:
        """ Return True if the target parm has a pending change
            awaiting to be committed.
            Must be implemented by the derived class.
        """
    def onParmAnimatedEvent(self, kwargs: _HUDParmAnimatedKwargs) -> None:
        """ Called by the HUD framework when a
            hou.nodeEventType.ParmTupleAnimated is triggered for the HUD handle
            parm.
            Must be implemented by the derived class.

            kwargs: same as hou.nodeEventType.ParmTupleAnimated
        """
    def onParmTemplateChangeEvent(self, kwargs: _HUDParmTemplateChangeKwargs) -> None:
        ''' Called by the HUD framework when the template event
            hou.nodeEventType.SpareParmTemplatesChanged is triggered
            for the HUD handle parm. Must be implemented by the derived
            class to react.

            kwargs: same as hou.nodeEventType.SpareParmTemplatesChanged
            kwargs["parm_template"]: The parm template.
            kwargs["parm_label_changed"]: list of new labels if the template
                                         label has changed or set to None
                                         otherwise.
            kwargs["parm_label_hidden"]: Template label is hidden.
        '''
    def onTerminate(self) -> None:
        """ Called by the HUD framework when the HUD window containing
            this widget is about to be terminated. Can be optionally
            implemented by the derived class for cleaning purposes.
        """
    def onParmChangeEvent(self, kwargs: _HUDParmChangeKwargs) -> None:
        ''' Called by the HUD framework when the HUD handle parm is
            changed. Must be implemented by the derived class for
            updating its widgets for the new parm value.

            kwargs: dictionary containing the information about the parm
                    change.
            "parm_name": Handle parm name
            "parm_value": New parm value
        '''
    def onUpdateVisualSize(self) -> None:
        """ Derived class should implement this method to update the
            widget items size based on their visual size option.
        """
    def settingValues(self) -> _HUDSettings:
        """ Returns a dictionary containing the HUD up to date setting
            values. The format: {SETTING_NAME:VALUE, ...}
        """
    def onLoadSettings(self, settings: _HUDSettings) -> None:
        """ Called by the HUD framework when the HUD settings have
            been loaded and ready for processing. This callback allows
            the HUD to process the settings one by one by calling
            onParmChangeEvent. onLoadSettings can be overriden by
            derived classes to process the settings in batch instead.

            kwargs: Dictionary containing the setting values keyed by
                    the Handle setting names.
        """
    def settingEditor(self) -> type[SettingDialog] | None:
        """ Returns the dialog class used for editing the HUD settings.
        """
    def createSettingEditor(self, setting_editor: type[SettingDialog], parent: HUDWindow) -> SettingDialog | None:
        """ Called by the HUD framework to create an instance of the HUD setting
            editor returned by the settingEditor() method.
        """
    def canLockHandle(self) -> bool:
        """ HUD handles with parms can be locked. Dynamic handles don't
            bind parms so they can't be locked.
        """
    def isLocked(self) -> bool:
        """ Return True if the hud parm is locked, False otherwise.
        """
    def onLockHandle(self, value: bool) -> None:
        """ Called when a HUD handle is locked or unlocked.
            value: handle is locked if True, unlocked otherwise.
        """
    def onUpdateHandleLock(self, parms_update: list[int]) -> None:
        """ Called when a parm lock has been updated. This allows
            the HUD to refresh its UI.
            parms_update: array holding the update state of each
                          parm.
                          1: parm is locked.
                          0: parm is unlocked.
                         -1: no update required.
        """
    def onUpdateShadowEffectState(self, value: bool) -> None:
        """ Derived class should implement this method to update the
            state of their widget items shadow effects.
        """
    def hasShadowEffect(self) -> bool:
        """ Return True if this HUD widget has shadow effect enabled.
        """
    def onUpdateLabelVisibleState(self, value: bool) -> None:
        """ Derived class should implement this method to update
            label visibility.
        """
    def onUpdateLabelColor(self, color: PySide6.QtGui.QColor) -> None:
        """ Derived class should implement this method to update the
            label color of their widget items.
        """
    def onUpdateSlidersVisible(self, value: bool) -> None:
        """ Derived class should implement this method to update the
            visibility of sliders for numeric parms.
            Intended for use by HUDSlider.
        """
    def onUpdateTrackpadSliderVisible(self, value: bool) -> None:
        """ Derived class should implement this method to update the
            visibility of an extra slider.
            Intended for use by HUDTrackPad.
        """
    def indirectParms(self) -> list[hou.Parm | None]:
        """ Return the parm or list of parm tuple components targeted
            by this indirect mouse manipulation.
        """
    def onMouseIndirectUpdate(self, level: int, mouse_pos: tuple[float, float], index: int, allowed_parms: list[hou.Parm | None]) -> bool:
        """ Derived class should implement this method to update
            the widget on an indirect update.
        """
    def onMouseIndirectStart(self, level: int, mouse_pos: tuple[float, float], allowed_parms: list[hou.Parm | None]) -> None:
        """ Derived class should implement this method to set up
            widget state when an indirect update begins.
        """
    def hasQtWidget(self, qt_widget: PySide6.QtWidgets.QWidget) -> bool:
        """ Return True if this HUD widget contains a given Qt widget
        """
    def computeDistance(self, x: float, y: float) -> list[float]:
        """ Compute the distance to x,y for the underlying QT widget.
            If the HUD widget has multiple QT widgets, the closest
            QT widget to x,y is returned along with its component index.
        """

def buttonEventInfo(parm_value: int) -> list[int]:
    """ Return the event info of a button when clicked. This function
        is typically used with a HUD button dynamically bound to a
        python state. Call this function from the python state
        onHandleToState handler to extract the id of the button along
        with its toggled state if the button is a TOGGLE button.

        parm_value: The parm_value passed to onHandleToState:

        Return:     Array of ints containing the button info.

                    Index 0:  button id relative to the button creation
                              order with hou.ViewerStateTemplate.bindHandle.

                    Index 1:  Toggled state, 0 or 1, for a TOGGLE button.
                              -1 if the button is a PUSH button.

        Note: [-1, -1] is returned if parm_value is invalid.
    """
def hudCommand(scene_viewer: hou.SceneViewer, windows: list[HUDWindow] | None = None, docking: int = 0, undocking: int = 0, display: int = -1, stacking: int = 0, enable: int = -1, compact: int = -1, display_title: int = -1, display_toolbar: int = -1, lock_position: int = -1, freeze: int = -1, position: tuple[int, int] | None = None, width: int | None = None, query_windows: Callable[[list[HUDWindow]], None] | None = None, visible_windows: int = -1, defer: int = 1) -> None:
    """ An API for performing operations on the HUD windows that
        currently exist in the viewer.

    scene_viewer:       Mandatory scene viewer to specify the
                        scoping of the operations. Only the windows
                        contained in the scene viewer will be
                        processed.

    windows:            List of HUD windows to operate on, if None the list
                        is set with all windows in the viewer.
                        Use query_windows to get a list of all windows
                        currently available in the viewer.

    docking:            If 1, the command will dock the windows
                        together.
                        NOTE: Ignore the docking operation if the
                              top window is already docked.
                        NOTE: Ignored if set to 0 (default).

    undocking:          If 1, the command will undock the
                        windows.
                        NOTE: The docking option has precedence over
                        the undocking option.

                        NOTE: Ignored if set to 0 (default).

    stacking:           If set to 1, the windows are moved to the
                        viewport bottom-left position and stacked
                        bottom-up.

                        NOTE: Ignored if set to 0 (default).

    display:            Display the windows if set to 1, hide if 0.

                        NOTE: Ignored if set to -1 (default).

    enable:             Enable the windows if set to 1, disable if 0.

                        NOTE: Ignored if set to -1 (default).

    compact:            Compact the windows if 1 or uncompact if 0.

                        NOTE: Ignored if set to -1 (default).

    display_title:      Display the top window title if 1 or hide if 0.

                        NOTE: Ignored if set to -1 (default).

    display_toolbar:    Display the top window toolbar if 1 or hide if 0.

                        NOTE: Ignored if set to -1 (default).

    position:           Position tuple (X,Y) to place the windows
                        relative to the viewer. If None (default), the
                        cached window position is used for positionning
                        the window. If there is no cached position, the
                        window is positionned at the viewport lower-left
                        position.

                        NOTE: The position coordinates must be relative
                        to the viewer top-left (Qt origin)

    width:              Set the window(s) with a new width. If None
                        (default), the cached window width is used.

    lock_position:      Lock the position of the windows contained in
                        the window list if set to 1. Unlock if set to 0.

                        NOTE: Ignored if set to -1 (default).

    freeze:             Ignore activate and deactivate operations of
                        all windows or a list of windows.

                        NOTE: Ignored if set to -1

    query_windows:      A callback called by the HUD manager with a list
                        of all HUD window objects currently in the system.
                        NOTE: Other options are ignored when a query is
                        requested.

    visible_windows:    Specify if only visible (1) or hidden (0) windows
                        are picked for processing. Default to -1 to pick
                        all windows.

    defer:              If 1 (default) the command is executed when the
                        Houdini's event loop is idle. If 0, the command
                        is run immediately.
                        NOTE: This option is for internal use as HUD
                              windows activation is usually deferred, so
                              they may not be fully defined yet if defer=0.
    """
def windowManager() -> HUDWindowManager: ...
def clearStateWindowSettings(state_name: str) -> None:
    """ Clear all state window setting caches
    """
def hudDebug(win: HUDWindow) -> _HUDDebugInfo: ...
def createHUDWidget(handle: _HUDHandle, **kwargs: Unpack[_CreateHUDWidgetOptions[_W]]) -> _W | None: ...
def onLoadSettings(hud_widget: HUDWidgetBase, kwargs: Mapping[str, ViewerParmProperties | _HUDSettingValue]) -> None: ...
def activateWindow(hud_widget: HUDWidgetBase) -> None: ...
def deactivateWindow(hud_widget: HUDWidgetBase, kwargs: ViewerHandleKwargs) -> None: ...
def parmChangeEvent(hud_widget: HUDWidgetBase, kwargs: ViewerHandleParmChangeKwargs) -> None: ...
def onWindowHoverEvent(event: PySide6.QtCore.QEvent) -> None: ...
def onMouseIndirectUpdate(hud_widget: HUDWidgetBase, **kwargs: Unpack[_MouseIndirectUpdateOptions]) -> bool: ...
def onMouseIndirectStart(hud_widget: HUDWidgetBase, **kwargs: Unpack[_MouseIndirectStartOptions]) -> None: ...
def dockWindows(docker_win: HUDWindow, dockee_windows: list[HUDWindow], update: bool = False) -> HUDWindow:
    """ Dock a list of windows under a top window.
        docker_window: The window to dock all dockee windows.
        dockee_windows: list of HUD windows to dock
    """
def undockWindows(windows: list[HUDWindow]) -> None: ...
def stackWindows(windows: list[HUDWindow]) -> None: ...
def setWindowVisibleState(win: HUDWindow, value: int) -> None: ...
def setWindowLockedState(win: HUDWindow, value: int) -> None: ...
def changeWindowsVisualSize(windows: Iterable[HUDWindow], visual_size_index: int, defer: int) -> None: ...
def lockParm(hud_widget: HUDWidgetBase, parm: hou.Parm, value: int) -> None: ...
def lockParmTuple(hud_widget: HUDWidgetBase, parm: hou.ParmTuple, value: int) -> None: ...
def displayAllWindows(scene_viewer: hou.SceneViewer, value: int) -> None: ...
def toggleWindowsLockedState(scene_viewer: hou.SceneViewer) -> None: ...
def toggleWindowsVisibleState(scene_viewer: hou.SceneViewer) -> None: ...
def setWindowVisibleStateByHandleName(scene_viewer: hou.SceneViewer, handle_name: str, onoff: bool) -> None: ...
def dockAllWindows(scene_viewer: hou.SceneViewer) -> None: ...
def undockAllWindows(scene_viewer: hou.SceneViewer) -> None: ...
def stackAllWindows(scene_viewer: hou.SceneViewer) -> None: ...
