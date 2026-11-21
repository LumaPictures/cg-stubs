# Houdini stubs generated from Houdini 22.0.466

import hou

HK_RADIAL_MENU: str

class HotkeyManager:
    """
    The hotkey symbols used in the Frame work and ALL tools. This is currently a limitation of the frame work
    structure that all hotkeys must be defined on the state directly and tools can only use pre bound hotkeys
    this class simply wraps the hotkey managment seperately from the actual state for easier managment and 
    access througout different tools
    """
    hud_channelwidget: str
    hud_parms: str
    tool_key_shift_h: str
    def __init__(self, state_typename: str, state_cat: hou.NodeTypeCategory) -> None: ...
    def definitions(self) -> hou.PluginHotkeyDefinitions:
        """
        Returns the hotkey definitions which can be registered with the
        viewer state template.
        """
    def context(self) -> str:
        """
        The hotkey context symbol for the state.
        """
