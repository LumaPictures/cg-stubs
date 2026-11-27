import hou
from .handle_manager import Curve3HandleProviderBase as Curve3HandleProviderBase, HandleTarget as HandleTarget
from .move_points import apply_drag_display_context as apply_drag_display_context, restore_drag_display_context as restore_drag_display_context
from .tool_base import Curve3ToolBase as Curve3ToolBase
from .tool_helpers import is_anchor_point as is_anchor_point, point_group_string as point_group_string
from .undo_helpers import execute_with_undo as execute_with_undo
from apex import xformgadget as xg
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from curvestate.curve3.controller_backend import _VerbParmArg
from curvestate.curve3.handle_manager import Curve3HandleManager as Curve3HandleManager, _HandleContext, _HandleDragState, _HandleInstanceContext
from curvestate.curve3.pick_controller import _CurvePickEvent
from dataclasses import dataclass
from houtypes import ViewerStateEventKwargs
from typing import Literal

@dataclass
class ModeSpec:
    mode_name: Literal['orient', 'scale']
    control_group_parm: str
    create_op: str
    remove_op: str
    change_op: str
    value_parm: str
    attrib_parm: str
    default_attrib: str
    default_value: hou.Vector3 | float
    undo_label: str
    xform_mode: xg._XformMode
    enabled_modes: list[xg._XformMode]

class _OrientScaleHandleProvider(Curve3HandleProviderBase):
    tool: Curve3OrientScaleBaseTool
    spec: ModeSpec
    def __init__(self, tool: Curve3OrientScaleBaseTool, spec: ModeSpec) -> None: ...
    def provider_name(self) -> str: ...
    def is_enabled(self) -> bool: ...
    def uses_custom_drag_lifecycle(self) -> bool: ...
    def build_targets(self, context: _HandleContext) -> list[HandleTarget]: ...
    def configure_instance(self, manager: Curve3HandleManager, instance_index: int, target: HandleTarget, context: _HandleInstanceContext) -> None: ...
    def on_handle_start(self, event: xg._HandleStartUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None: ...
    def _drag_operation_parms(self, target: HandleTarget, drag_state: _HandleDragState) -> dict[str, _VerbParmArg]:
        """Build the identical explicit payload for live publication and commit."""
    def on_handle_update(self, event: xg._HandleUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None: ...
    def on_handle_end(self, event: xg._HandleUpdateKwargs, target: HandleTarget, context: _HandleContext) -> None: ...

class Curve3OrientScaleBaseTool(Curve3ToolBase[hou.Vector3 | float]):
    mode_spec: ModeSpec | None
    def __init__(self, controller: Curve3Controller) -> None: ...
    def handle_provider(self) -> Curve3HandleProviderBase: ...
    def operation_override_parms(self, optype: str) -> dict[str, hou.Vector3 | float]:
        """Seed create-control ops from the selected point's current attrib value."""
    def force_handle_visible(self) -> bool:
        """Orient/scale tools always show their transform handle."""
    def drawable_allows_intool_orient_guide(self) -> bool:
        """Orient and scale modes own the in-tool frame/orient guide display."""
    def drawable_overlay_visible(self, *, interactive_drag_active: bool, processed_geo: hou.Geometry, preview_geo: hou.Geometry) -> bool:
        """Honor the shared Always preview policy in orient and scale modes."""
    def hotkey_create_mode_point_command(self) -> str | None:
        """Create this mode's control point for the shared create hotkey."""
    def hotkey_delete_mode_action_command(self) -> str | None:
        """Remove this mode's control point for the shared delete hotkey."""
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_pick_curve(self, kwargs: ViewerStateEventKwargs, handle_event: _CurvePickEvent) -> bool: ...
    def read_point_mode_value(self, point: hou.Point) -> hou.Vector3 | float: ...
    def apply_drag_preview_from_event(self, event: xg._HandleUpdateKwargs, context: _HandleContext) -> None: ...
    def reset_drag_preview_parms(self, controller: Curve3Controller) -> None: ...
