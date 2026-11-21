# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
from houtypes import ParmActionButtonKwargs
from typing import Literal

class PackFolderMenuEntry:
    """
    Custom object for referecing components like menu name and corresponding parm value
    """
    name: str
    value: str
    menutype: Sequence[str]
    visible: bool
    def __init__(self, name: str, value: str, menutype: Sequence[str], visible: bool) -> None: ...

def packFolderMenuBuildEntries(menutype: str) -> list[PackFolderMenuEntry]:
    """
    Build the menu entries for frameRangeMenu
    """
def updateParm(scriptargs: ParmActionButtonKwargs, entry: PackFolderMenuEntry) -> Literal[False] | None: ...
def packFolderMenu(kwargs: ParmActionButtonKwargs, menutype: str) -> None:
    """
    Build a menu exposing pack extend input options
    """
