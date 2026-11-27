from collections.abc import Mapping, Sequence

import hou
from hutil.qt.data.panels import _HudTemplate, _HudUpdates

def hudInfo(
    self: hou.CompositorViewer,
    show: bool | int = ...,
    terminate: bool = ...,
    state: hou.EnumValue[hou.hudInfoState] = ...,
    template: _HudTemplate | None = ...,
    values: _HudUpdates | None = ...,
    panel: hou.EnumValue[hou.hudPanel] | int = ...,
    update_hotkey_bindings: bool = ...,
    **kwargs: object,
) -> None: ...
def clearPromptMessage(self: hou.CompositorViewer) -> None: ...
def setPromptMessage(
    self: hou.CompositorViewer, msg: str, msg_type: hou.EnumValue[hou.promptMessageType] | None = ...
) -> None: ...
def selectDrawableGeometry(
    self: hou.CompositorViewer,
    drawable_selection: Mapping[str, Mapping[str, Sequence[int]]],
    selection_modifier: hou.EnumValue[hou.pickModifier] | None = ...,
) -> None: ...
def beginStateUndo(self: hou.CompositorViewer, label: str) -> None: ...
def endStateUndo(self: hou.CompositorViewer) -> None: ...
