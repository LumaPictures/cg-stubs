import hou

from typing import TypeAlias
from typing import TypeAlias
_Parms: TypeAlias = str | hou.Parm | hou.ParmTuple | list[str] | list[hou.Parm] | list[hou.ParmTuple] | list[str | hou.Parm | hou.ParmTuple]
def scrollTo(self: hou.ParameterEditor, parms: _Parms, scroll_pos: hou.EnumValue[hou.scrollPosition] = ...) -> None:
    """
scrollTo(self, parms, scroll_pos)

    Adjust the Parameter Editor vertical scroll bar to align one or more
    parameters using hou.scrollPosition mode.

    The parms argument can be a list or a single str, hou.Parm or
    hou.ParmTuple. The types can also be mixed in the list. If an entry
    is a str, you can pass a comma separated list of parameter names but
    wildcards are not supported.

    The scroll_pos argument defines how to align the vertical bounding
    box of the affected parameters. See hou.scrollPosition.

"""
def moveFocusTo(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> None:
    """
moveFocusTo(self, parm)

    Try to move keyboard focus to the specified parameter in the
    Parameter Editor.

"""
def pressJumpButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool:
    """
pressJumpButton(self, parm)

    Press the jump button on a parameter. parm can be a string, a
    hou.Parm or a hou.ParmTuple. Return True if it succeeded.

"""
def pressPlusButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool:
    """
pressPlusButton(self, parm)

    Press the plus button on a parameter. parm can be a string, a
    hou.Parm or a hou.ParmTuple. Return True if it succeeded.

"""
def pressScriptActionButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool:
    """
pressScriptActionButton(self, parm)

    Press the script action button on a parameter. parm can be a string,
    a hou.Parm or a hou.ParmTuple. Return True if it succeeded.

"""
def pressColorButton(self: hou.ParameterEditor, parm: str | hou.Parm | hou.ParmTuple) -> bool:
    """
pressColorButton(self, parm)

    Press the color button on a parameter. parm can be a string, a
    hou.Parm or a hou.ParmTuple. Return True if it succeeded.

"""
