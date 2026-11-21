from typing import Any

import hou
from hutil.qt.data.panels import _HudTemplate, _HudUpdates

PANEL_TO_ENUM: dict[int, hou.EnumValue[hou.hudPanel]]

def hudInfo(
    self: hou.SceneViewer,
    show: bool | int = ...,
    terminate: bool = ...,
    state: hou.EnumValue[hou.hudInfoState] = ...,
    template: _HudTemplate | None = ...,
    values: _HudUpdates | None = ...,
    panel: hou.EnumValue[hou.hudPanel] | int = ...,
    update_hotkey_bindings: bool = ...,
    **kwargs: Any,
) -> None: ...
