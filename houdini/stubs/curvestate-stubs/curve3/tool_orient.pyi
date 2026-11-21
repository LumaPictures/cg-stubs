# Houdini stubs generated from Houdini 22.0.466

from .tool_orient_scale_base import Curve3OrientScaleBaseTool as Curve3OrientScaleBaseTool, ModeSpec as ModeSpec
from collections.abc import Callable as Callable, Mapping
from houtypes import ViewerMenuItemState

class Curve3OrientTool(Curve3OrientScaleBaseTool):
    tool_name: str
    tool_label: str
    default_optype: str | None
    hud_hints: list[dict[str, str]]
    prompt_message: str
    mode_spec: ModeSpec
    def hud_tool_hints(self, *, hint_fn: Callable[[str, str], dict[str, str]], selection_hints: list[dict[str, str]], hotkey_refs: Mapping[str, str]) -> list[dict[str, str]]:
        """Return orient HUD hints in the established order."""
    def update_menu_item_states(self, menu_item_states: dict[str, ViewerMenuItemState], *, active: bool, set_visible_fn: Callable[[dict[str, ViewerMenuItemState], str, bool], object]) -> None:
        """Show orient-only context-menu actions only while orient mode is active."""
