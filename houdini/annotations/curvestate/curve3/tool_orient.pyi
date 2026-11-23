from collections.abc import Callable, Mapping

from houtypes import ViewerMenuItemState

from curvestate.curve3.tool_orient_scale_base import Curve3OrientScaleBaseTool, ModeSpec


class Curve3OrientTool(Curve3OrientScaleBaseTool):
    tool_name: str
    tool_label: str
    default_optype: str | None
    hud_hints: list[dict[str, str]]
    prompt_message: str
    mode_spec: ModeSpec
    def hud_tool_hints(
        self,
        *,
        hint_fn: Callable[[str, str], dict[str, str]],
        selection_hints: list[dict[str, str]],
        hotkey_refs: Mapping[str, str],
    ) -> list[dict[str, str]]: ...
    def update_menu_item_states(
        self,
        menu_item_states: dict[str, ViewerMenuItemState],
        *,
        active: bool,
        set_visible_fn: Callable[[dict[str, ViewerMenuItemState], str, bool], object],
    ) -> None: ...
