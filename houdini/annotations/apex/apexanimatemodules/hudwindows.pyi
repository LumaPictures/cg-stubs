from typing import type_check_only

import apex.stateutils_2 as asu
import hou
import statehud.utils as shu
import statehud.window as shs
from apex.apexanimatemodules.base import ApexAnimateBaseModule, _AnimateState as _BaseState
from apex.ui.channelhudwidgets import _AnimateState as _ChannelHudState
from apex.ui.selectionmanager.hudpanel import SelectionSetHUDPanel
from apex.ui.settingshudwidgets import AnimateSettingsWidget, _AnimateState as _SettingsState
from apex.ui.splitchannelwidget import SplitChannelWidgetHandler
from houtypes import (
    SceneViewerEventKwargs,
    ViewerStateCommandKwargs,
    ViewerStateEnterKwargs,
    ViewerStateEventKwargs,
    ViewerStateKwargs,
    ViewerStatePlaybackChangeKwargs,
    ViewerStateVolatileClientKwargs,
)
from apex.xformgadget import _HandleSettingsUpdateKwargs
from staterecordutils import RecordableViewerState
from statehud.window import _ParmEventDict

# Not a Protocol: the module passes the state to RecordableViewerState.recordHUDParmEvent().
class _AnimateState(RecordableViewerState, _ChannelHudState, _SettingsState, _BaseState):
    """The Animate viewer state (`viewer_states/apexanimate.py`), with the members this module uses."""

    def clearCustomBakeParms(self) -> None: ...

USRDATA_PARM_KEY: str
USRDATA_CHANNEL_KEY: str
USRDATA_SEL_KEY: str
USRDATA_MOUSE_SEL_KEY: str
PRIMARY_XFORM_INDEX: int

class ApexAnimateHUDWindows(ApexAnimateBaseModule):
    # The panels are None until the state enters, and after it exits.
    hud_channel_panel: SplitChannelWidgetHandler | None
    hud_parameter_panel: AnimateSettingsWidget | None
    hud_sel_panel: SelectionSetHUDPanel | None
    hud_mouse_sel_panel: SelectionSetHUDPanel | None
    hud_pin_mgr: shu.PinManager
    stashed_visible_huds: list[SelectionSetHUDPanel | SplitChannelWidgetHandler | AnimateSettingsWidget]
    def __init__(self, state: _AnimateState) -> None: ...
    @type_check_only
    @property
    def state(self) -> _AnimateState: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onHUDParmEvent(self, kwargs: _ParmEventDict) -> None: ...
    def onHUDSettingEvent(self, kwargs: _ParmEventDict) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> None: ...
    def onXformGadgetSettingsEvent(self, kwargs: _HandleSettingsUpdateKwargs) -> None: ...
    def onSceneViewerEvent(self, kwargs: SceneViewerEventKwargs) -> None: ...
    # tool defaults to the active tool.
    def bindToolHuds(self, tool: asu._Tool | None = ...) -> None: ...
    def unbindToolHuds(self, tool: asu._Tool | None = ...) -> None: ...
    # node defaults to the scene node (the only node passed), tool to the active tool.
    def saveToolHUDSettings(
        self, node: hou.SopNode | None = ..., tool: asu._Tool | None = ..., settings_widget: bool = ..., hud_widget: bool = ...
    ) -> None: ...
    def saveHUDSettings(
        self,
        node: hou.SopNode | None = ...,
        sel_panel: bool = ...,
        mouse_sel_panel: bool = ...,
        parm_panel: bool = ...,
        channel_panel: bool = ...,
    ) -> None: ...
    def loadToolHUDSettings(
        self, node: hou.SopNode | None = ..., tool: asu._Tool | None = ..., settings_widget: bool = ..., hud_widget: bool = ...
    ) -> None: ...
    def loadHUDSettings(
        self,
        node: hou.SopNode | None = ...,
        sel_panel: bool = ...,
        mouse_sel_panel: bool = ...,
        parm_panel: bool = ...,
        channel_panel: bool = ...,
    ) -> None: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool: ...
    def getHUDWindow(self, name: str) -> shs.WidgetBundleWindow | None: ...
