from collections.abc import Callable, Mapping

import hou
from houtypes import ViewerMenuItemState

from curvestate.curve3.tool_orient_scale_base import Curve3OrientScaleBaseTool, ModeSpec


class Curve3ScaleTool(Curve3OrientScaleBaseTool):
    tool_name: str
    tool_label: str
    default_optype: str | None
    hud_hints: list[hou._HudRow]
    prompt_message: str
    mode_spec: ModeSpec
    def hud_tool_hints(
        self,
        *,
        hint_fn: Callable[[str, str], hou._HudRow],
        selection_hints: list[hou._HudRow],
        hotkey_refs: Mapping[str, str],
    ) -> list[hou._HudRow]: ...
    def update_menu_item_states(
        self,
        menu_item_states: dict[str, ViewerMenuItemState],
        *,
        active: bool,
        set_visible_fn: Callable[[dict[str, ViewerMenuItemState], str, bool], object],
    ) -> None: ...
    def handle_controller_command(self, command: str, args: object = ...) -> bool: ...
