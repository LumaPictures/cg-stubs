# Houdini stubs generated from Houdini 22.0.466

UNKNOWN_TYPE: int
BOOL_TYPE: int
FLOAT_TYPE: int
INT_TYPE: int
COLOR_TYPE: int
STRING_TYPE: int
TRISTATE_TYPE: int
ICON_SIZE: int
BUTTON_SIZE: float
HOTKEY_PARMS_SET_KEYFRAME: str
HOTKEY_PARMS_REM_KEYFRAME: str
HOTKEY_PARMS_REVERT_DEFS: str
HOTKEY_PARMS_LOCK_PARM: str
HOTKEY_PARMS_UNLOCK_PARM: str
HOTKEY_PARMS_TOGGLE_EXPR: str
HOTKEY_PARMS_EDIT_EXPR: str
HOTKEY_PARMS_EXPAND_EXPR: str
HOTKEY_PARMS_EXPR_PYTHON: str
HOTKEY_PARMS_EXPR_HSCRIPT: str
HOTKEY_PARMS_HIDE_EXPR: str
HOTKEY_PARMS_SHOW_EXPR: str

class LinkType:
    UNKNOWN: int
    LIGHT: int
    SHADOW: int
    MATERIAL: int
    MATERIALDIRECT: int
    MATERIALCOLLECTION: int
    @staticmethod
    def getFromStr(linktype: str) -> int: ...
    @staticmethod
    def getStr(linktype: int) -> str: ...
    @staticmethod
    def getIconStr(linktype: int) -> str: ...
