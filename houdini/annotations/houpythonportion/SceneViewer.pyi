from typing import TypedDict, Unpack

import hou
from hutil.qt.data.panels import _HudTemplate, _HudUpdates

PANEL_TO_ENUM: dict[int, hou.EnumValue[hou.hudPanel]]

# The deprecated spellings hudInfo still accepts; other keys are ignored.
class _HudInfoDeprecatedKwargs(TypedDict, total=False):
    hud_state: hou.EnumValue[hou.hudInfoState]
    hud_template: _HudTemplate | None
    hud_values: _HudUpdates | None
    hud_panel: hou.EnumValue[hou.hudPanel] | int

def hudInfo(
    self: hou.SceneViewer,
    show: bool | int = ...,
    terminate: bool = ...,
    state: hou.EnumValue[hou.hudInfoState] = ...,
    template: _HudTemplate | None = ...,
    values: _HudUpdates | None = ...,
    panel: hou.EnumValue[hou.hudPanel] | int = ...,
    update_hotkey_bindings: bool = ...,
    **kwargs: Unpack[_HudInfoDeprecatedKwargs],
) -> None: ...
