from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import ClassVar, Literal, Protocol, TypeAlias, TypedDict

import _apex
import apex
import apex.characterpathutils as acpu
import apex.stateutils_2 as asu
import apex.ui.dynamicmotionhudwidgets as dmui
import hou
from apex.autorigtool import _ToolActivateKwargs
from apex.xformgadget import _HandleStartUpdateKwargs, _HandleUpdateKwargs
from houtypes import (
    ViewerStateEventKwargs,
    ViewerStateMenuActionKwargs,
    ViewerStateMenuPreOpenKwargs,
    ViewerStateParmChangeKwargs,
    ViewerStatePlaybackChangeKwargs,
)
from statehud.parmutils import _HUDParmValue

# (graph parm name, (node name, port name)) pairs, as apex.utils.wireNewInputMapping takes them.
_PortMapping: TypeAlias = tuple[tuple[str, tuple[str, str]], ...]

class _AnimateState(acpu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members of the states it extends."""

# What apex.animstack passes to the state's onActiveLayerChanged().
class _ActiveLayerChangedKwargs(TypedDict):
    prev_active: str
    active: str

class StateData:
    callback: Callable[[bool], tuple[bool, acpu.GraphUndo | None]]

class StateMachine:
    INITIAL_STATE: ClassVar[StateId]
    def update(self) -> None: ...

class StateMachineUndo(acpu.Undo):
    def __init__(
        self,
        tool: "DynamicMotionTool",
        pre_sm: StateMachine,
        post_sm: StateMachine,
        graph_undo: acpu.GraphUndo | None = ...,
    ) -> None: ...

class GraphBuilder:
    INPUT_MAPPING: ClassVar[_PortMapping]
    OUTPUT_MAPPING: ClassVar[_PortMapping]
    PATHARRAY_PORTS: ClassVar[tuple[tuple[str, str], ...]]
    PREVIEW_INPUT_MAPPING: ClassVar[_PortMapping]
    PREVIEW_DRAW_INPUT_MAPPING: ClassVar[_PortMapping]
    @property
    def tool(self) -> "DynamicMotionTool | None": ...
    def removeMotion(self, num: int) -> None: ...

class DynamicMotionTool(acpu.CharacterPathToolBase[_AnimateState]):
    graph_builder: GraphBuilder
    # None until onActivate().
    convert_proj_life: apex.Graph | None
    convert_proj_plane: apex.Graph | None
    convert_proj_speed: apex.Graph | None
    # None until the first pose or slider start.
    pre_graph_parms: apex.Dict | None
    # None while the tool is inactive.
    hud_widget: dmui.DynamicMotionParmsWidget | None
    settings_widget: dmui.DynamicMotionSettingsWidget | None
    hud_rows: list[hou._HudRow]
    def __init__(self, state: _AnimateState) -> None: ...
    def _getPairedControls(self, control_selection: Iterable[str]) -> list[str]: ...
    def onActivate(self, kwargs: _ToolActivateKwargs) -> bool: ...
    def convertProjectileFromLife(self, parms: apex.Dict) -> dict[str, _apex._Value | None]: ...
    def convertProjectileFromPlane(self, parms: apex.Dict) -> dict[str, _apex._Value | None]: ...
    def convertProjectileFromInitialSpeed(self, parms: apex.Dict) -> dict[str, _apex._Value | None]: ...
    def onActiveLayerChanged(self, kwargs: _ActiveLayerChangedKwargs) -> None: ...
    def onSelectionChanged(self, control_selection: Sequence[str]) -> bool: ...
    def onPoseStartEvent(self, kwargs: ViewerStateEventKwargs | _HandleStartUpdateKwargs) -> None: ...
    def onPoseEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> None: ...
    def onPoseEndEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> None: ...
    def updateVisibleControls(self) -> None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> bool: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> Literal[False] | None: ...
    def shiftKeys(
        self,
        revert: bool = ...,
        add_undo: bool = ...,
        shift_frame: bool = ...,
        layer_name: str | None = ...,
    ) -> None: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
    def onToolParmChanged(self, parm_name: str, val: _HUDParmValue) -> None: ...
    def onToolParmSliderStart(self, name: str, value: _HUDParmValue) -> None: ...
    def onToolParmSliderEnd(self, name: str, start_value: _HUDParmValue, value: _HUDParmValue) -> None: ...
    # The bake parameters of the Animate state's settings HUD.
    def onBakeEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> bool: ...
    def resolveSelectCom(self, forward: bool) -> tuple[bool, acpu.GraphUndo | None]: ...

def load(viewer_state: _AnimateState) -> DynamicMotionTool: ...
def bindActionsToMenu(menu: hou.ViewerStateMenu, hotkeys: asu.Hotkeys) -> None: ...
