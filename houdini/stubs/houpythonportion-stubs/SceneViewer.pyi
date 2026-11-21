import hou
from hutil.qt.data.panels import _HudTemplate, _HudUpdates
from typing import Any

PANEL_TO_ENUM: dict[int, hou.EnumValue[hou.hudPanel]]

def hudInfo(self: hou.SceneViewer, show: bool | int = True, terminate: bool = False, state: hou.EnumValue[hou.hudInfoState] = ..., template: _HudTemplate | None = None, values: _HudUpdates | None = None, panel: hou.EnumValue[hou.hudPanel] | int = ..., update_hotkey_bindings: bool = False, **kwargs: Any) -> None:
    """
hudInfo(self, show=-1, state=None, template=None, values=None,
panel=hou.hudPanel.ToolInfo, terminate=False,
update_hotkey_bindings=False)

    Creates, updates, or controls a read-only heads-up-display panel in
    the viewer. The HUD panel extends across viewport divisions.

    This interface is experimental and subject to change. See Python
    state info panels for more information.

  * Houdini will automatically clear the HUD panel when the tool/state
    changes.

  * Houdini will automatically hide/show the panel when the user presses
    [Shift + F1].


    show
        Show the HUD if True or hide it if False. This option is a tri-
        state option and is ignored by default.

    state
        Specifies the display state for the hou.hudPanel.ToolInfo panel.
        See hou.hudInfoState for details.

    template
        A dictionary describing the HUD template to format the
        information to display.

    values
        A dictionary of values for updating the information displayed by
        the HUD.

    panel
        Identifier for specifying the layout and home location of the
        HUD. Defaults to hou.hudPanel.ToolInfo.

    terminate
        Delete the HUD identified with panel and remove it from the
        viewport if currently displayed, other arguments are ignored.
        Defaults to False.

    update_hotkey_bindings
        Will redo the lookup of keys bound to hotkey symbols when True.

    See viewer HUD info panels for more information.

"""
