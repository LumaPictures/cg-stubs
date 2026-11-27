import hou
from collections.abc import Mapping, Sequence
from hutil.qt.data.panels import _HudTemplate, _HudUpdates

def hudInfo(self: hou.CompositorViewer, show: bool | int = True, terminate: bool = False, state: hou.EnumValue[hou.hudInfoState] = ..., template: _HudTemplate | None = None, values: _HudUpdates | None = None, panel: hou.EnumValue[hou.hudPanel] | int = ..., update_hotkey_bindings: bool = False, **kwargs: object) -> None:
    """
hudInfo(self, show=-1, state=None, template=None, values=None,
panel=hou.hudPanel.ToolInfo, terminate=False,
update_hotkey_bindings=False)

    Not implemented.

"""
def clearPromptMessage(self: hou.CompositorViewer) -> None: ...
def setPromptMessage(self: hou.CompositorViewer, msg: str, msg_type: hou.EnumValue[hou.promptMessageType] | None = None) -> None: ...
def selectDrawableGeometry(self: hou.CompositorViewer, drawable_selection: Mapping[str, Mapping[str, Sequence[int]]], selection_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None: ...
def beginStateUndo(self: hou.CompositorViewer, label: str) -> None: ...
def endStateUndo(self: hou.CompositorViewer) -> None: ...
