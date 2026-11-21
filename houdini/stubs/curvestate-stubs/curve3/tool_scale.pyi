# Houdini stubs generated from Houdini 22.0.466

from .tool_helpers import point_group_string as point_group_string
from .tool_orient_scale_base import Curve3OrientScaleBaseTool as Curve3OrientScaleBaseTool, ModeSpec as ModeSpec
from .undo_helpers import execute_with_undo as execute_with_undo
from collections.abc import Callable as Callable, Mapping
from houtypes import ViewerMenuItemState

class Curve3ScaleTool(Curve3OrientScaleBaseTool):
    tool_name: str
    tool_label: str
    default_optype: str | None
    hud_hints: list[dict[str, str]]
    prompt_message: str
    mode_spec: ModeSpec
    def hud_tool_hints(self, *, hint_fn: Callable[[str, str], dict[str, str]], selection_hints: list[dict[str, str]], hotkey_refs: Mapping[str, str]) -> list[dict[str, str]]:
        """Return scale HUD hints in the established order."""
    def update_menu_item_states(self, menu_item_states: dict[str, ViewerMenuItemState], *, active: bool, set_visible_fn: Callable[[dict[str, ViewerMenuItemState], str, bool], object]) -> None:
        """Show scale-only context-menu actions only while scale mode is active."""
    def handle_controller_command(self, command: str, args: object = None) -> bool:
        """Handle scale-tool context-menu commands."""
