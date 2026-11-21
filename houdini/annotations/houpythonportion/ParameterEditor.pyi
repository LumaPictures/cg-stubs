from typing import TypeAlias

import hou

# _scrollTo only recognises a list, not other sequences.
_Parms: TypeAlias = (
    str
    | hou.Parm
    | hou.ParmTuple
    | list[str]
    | list[hou.Parm]
    | list[hou.ParmTuple]
    | list[str | hou.Parm | hou.ParmTuple]
)

def scrollTo(
    self: hou.ParameterEditor,
    parms: _Parms,
    scroll_pos: hou.EnumValue[hou.scrollPosition] = ...,
) -> None: ...
def moveFocusTo(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> None: ...
def pressJumpButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool: ...
def pressPlusButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool: ...
def pressScriptActionButton(
    self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple
) -> bool: ...
def pressColorButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool: ...
