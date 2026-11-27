import apex.stateutils_2 as asu
import apex.ui.animationhudwidgets as au
import apex.xformgadget as xg
import hou
import resourceui as rui
import statehud.window as shud
from PySide6.QtWidgets import QWidget
from apex.ui.animationhudwidgets import _HudState
from collections.abc import Callable as Callable, Container, Iterable, Mapping
from hutil.PySide import QtWidgets
from statehud.baseconfig import AbstractConfig
from statehud.parmutils import _HUDParmValue
from statehud.parmwidgetset import ParmWidgetSet, _HUDParmInput, _HUDParmTemplate
from statehud.window import _ParmEventDict
from typing import Final, Protocol

class _AnimateState(asu._AnimateState, _HudState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    allow_snap_triggers: bool
    frame_zoom_factor: float
    def bindMotionPath(self) -> None: ...
    def unbindMotionPath(self) -> None: ...
    def setMotionPathWidth(self, width: float) -> None: ...
    def setMotionPathKeySize(self, size: float) -> None: ...
    def setMotionPathLimitFrames(self, on: bool, before: int, after: int) -> None: ...
    def bakeKeys(self) -> None: ...
    def startRecordingPoses(self) -> None: ...
    def stopRecordingPoses(self) -> None: ...
    def setEnforceParmLimits(self, val: bool) -> None: ...
    def setShowParmLimits(self, val: bool) -> None: ...
    def getXformModeFromControl(self, control: str) -> xg._XformMode: ...

USE_COLLAPSIBLE_SETTINGS_FOLDERS: bool
HANDLE_TOOL_TAB: str
BAKE_TAB: str
TOOL_TAB_NAMES: list[str]
TRANSFORM_SETTINGS_TAB: str
MOTIONPATH_SETTINGS_TAB: str
TAB_NAMES: list[str]
HANDLE_X: Final[str]
HANDLE_T: Final[str]
HANDLE_R: Final[str]
HANDLE_S: Final[str]
HANDLE_C: Final[str]
HANDLE_WORLD: Final[str]
HANDLE_LOCAL: Final[str]
HANDLE_CPLANE: Final[str]
HANDLE_VIEW: Final[str]
HANDLE_PARENT: Final[str]
HANDLE_XFORM_MODES: list[xg._XformMode]
HANDLE_ALIGN_MODES: list[xg._AlignMode]
HANDLE_XFORM: str
HANDLE_ALIGN: str
HANDLE_XFORM_AUTO: str
GIMBAL: str
LIMIT_CTRLS: str
SHOW_LIMITS: str
ALLOW_SNAP_TRIGGERS: str
FRAMING_ZOOM: str
TRANSFORM_MODE_PARMS: dict[str, _HUDParmTemplate]
TRANSFORM_PREF_PARMS: dict[str, _HUDParmTemplate]
TRANSFORM_MISC_PARMS: dict[str, _HUDParmTemplate]
MOTIONPATH_BIND_STRIP: str
MOTIONPATH_BIND: str
MOTIONPATH_UNBIND: str
MOTIONPATH_BIND_STRIP_BUTTONS: list[str]
MOTIONPATH_LIMITFRAMES: str
MOTIONPATH_VISIBLEFRAMES: str
MOTIONPATH_KEYSIZE: str
MOTIONPATH_PATHWIDTH: str
MOTIONPATH_PARMS: dict[str, _HUDParmTemplate]
BAKE_BAKEKEYS: str
BAKE_STARTRECORDING: str
BAKE_STOPRECORDING: str
BAKE_USEFRAMERANGE: str
BAKE_FRAMERANGE: str
BAKE_KEEP: str
BAKE_RESAMPLE: str
BAKE_FREQUENCY: str
BAKE_CONFIG_PARMS: dict[str, _HUDParmTemplate]
BAKE_NEWLAYER: str
BAKE_ADDITIVELAYER: str
BAKE_LAYER_PARMS: dict[str, _HUDParmTemplate]
FOLDER_NAMES: list[str]
FOLDER_LABELS: list[str]

class FolderContainerWidget(QtWidgets.QScrollArea):
    """Scrollable container of CollapsibleFolderWidgets.
    Registered under TOOL_TAB_WIDGET name for embed/unembed compatibility."""
    def __init__(self, parent: QWidget | None = None) -> None: ...
    def addFolder(self, folder: rui.CollapsibleFolderWidget) -> None: ...
    def getFolder(self, name: str) -> rui.CollapsibleFolderWidget | None: ...
    def expandFolder(self, name: str) -> None: ...
    def showOnly(self, names: Container[str]) -> None:
        """Collapse all folders except those in names, which are expanded."""
    def setVisualSize(self, visual_size: int) -> None: ...
    def clearFolder(self, name: str) -> None:
        """Remove all dynamically-bound widgets from a folder."""

class AnimateSettingsWidget(au.ParameterWidget[_AnimateState, shud.WidgetBundleWindow]):
    """
    This class contains standard settings for the animate state
    """
    hud_window: shud.WidgetBundleWindow
    transform_mode_parm_set: ParmWidgetSet
    transform_pref_parm_set: ParmWidgetSet
    transform_misc_parm_set: ParmWidgetSet
    motionpath_parm_set: ParmWidgetSet
    bake_config_parms: ParmWidgetSet
    bake_custom_config_parms: ParmWidgetSet
    bake_layer_parms: ParmWidgetSet
    bake_custom_layer_parms: ParmWidgetSet
    bake_parm_sets: tuple[ParmWidgetSet, ParmWidgetSet, ParmWidgetSet, ParmWidgetSet]
    DEFAULT_SIZE: int
    DEFAULT_LABEL_WIDTH: int
    FOLDER_LABELS: tuple[str, ...]
    def __init__(self, state: _AnimateState, scene_viewer: hou.SceneViewer, callback: Callable[[_ParmEventDict], object] | None = None) -> None: ...
    def resetToolTabLabel(self) -> None: ...
    def setTitleFromCurrentTab(self) -> None: ...
    def setToolSectionEnabled(self, enabled: bool) -> None:
        """Show/hide the Tool section (folder or tab)."""
    def clearToolSection(self) -> None:
        """Clear dynamically-bound tool widgets."""
    def getToolSectionTabInfo(self) -> tuple[shud.WidgetBundleWindow, str, str | None]:
        """Return (hud_window, tab_widget_name, tab_name) for tool widget binding."""
    def getSectionTabInfo(self, tab_name: str) -> tuple[shud.WidgetBundleWindow, str, str | None]:
        """Return (hud_window, tab_widget_name, tab_name) for a named section."""
    def saveCurrentSection(self) -> str | None:
        """Save the current section name before a tool switch.
        In folder mode returns None (all sections visible)."""
    def restoreCurrentSection(self, name: str | None, enabled: bool) -> None:
        """Restore the previously active section after a tool switch."""
    def showToolSectionOnly(self) -> None:
        """Expand the Tool section and collapse all others.
        In tab mode, switch to the Tool tab."""
    def switchAwayFromToolSection(self) -> None:
        """Switch away from tool tab before clearing. No-op in folder mode."""
    def loadFromConfig(self, config: shud.HUDConfig) -> None:
        """ Load the window from the passed in config. """
    def saveToConfig(self, config: shud.HUDConfig) -> None:
        """ Save the hud window to the passed in config. """
    def currentTabChangedCallback(self, index: int) -> None: ...
    def onBindMotionPathCallback(self, name: str, v: bool) -> None: ...
    def onMotionPathParmChanged(self, name: str) -> None: ...
    def onMotionPathFrameRangeChanged(self) -> None: ...
    def onBakeKeys(self) -> None: ...
    def onStartRecordingPoses(self) -> None: ...
    def onStopRecordingPoses(self) -> None: ...
    def onBakeParmChanged(self, name: str) -> None: ...
    def onCustomBakeParmChanged(self, name: str) -> None: ...
    def updateBakeParms(self, for_recording: bool = False) -> None: ...
    def bindBakeConfigParm(self, name: str, value: _HUDParmInput, parm_dict: _HUDParmTemplate) -> None: ...
    def bindBakeLayerParm(self, name: str, value: _HUDParmInput, parm_dict: _HUDParmTemplate) -> None: ...
    def loadBakeParmsFromConfig(self, config: AbstractConfig, prefix: str = '') -> None: ...
    def saveBakeParmsToConfig(self, config: AbstractConfig, prefix: str = '') -> None: ...
    def clearCustomBakeParms(self) -> None: ...
    def showBakeParms(self, parm_names: Iterable[str], on: bool = True) -> None: ...
    def showAllBakeParms(self, on: bool = True) -> None: ...
    def showRecordingButton(self, on: bool) -> None: ...
    def getBakeParms(self) -> dict[str, _HUDParmValue]: ...
    def setBakeParms(self, parms: Mapping[str, object]) -> None: ...
    def onTransformMiscParmChanged(self, name: str) -> None: ...
    def onTransformModeParmChanged(self, name: str) -> None: ...
    def handleXformCallback(self, xform_mode: xg._XformMode) -> None:
        """set manual handle xform mode for the state here"""
    def handleAlignCallback(self, align_mode: xg._AlignMode) -> None:
        """change the handle alignment for the state"""
    def updateHandleChangeModeAutoFromPref(self) -> None:
        """Synchronize the auto-mode HUD toggle with its global preference."""
    def updateSettingsFromHandle(self) -> None:
        """
        Update the HUD settings when a setting is changed though
        the handle.
        """
    def setEmbedded(self, value: bool) -> None: ...
    def embedded(self) -> bool: ...
    def show(self, on: bool = True) -> None: ...
