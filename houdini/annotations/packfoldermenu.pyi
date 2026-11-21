from collections.abc import Sequence
from typing import Literal

from houtypes import ParmActionButtonKwargs

class PackFolderMenuEntry:
    name: str
    value: str
    menutype: Sequence[str]
    visible: bool
    def __init__(self, name: str, value: str, menutype: Sequence[str], visible: bool) -> None: ...

def packFolderMenuBuildEntries(menutype: str) -> list[PackFolderMenuEntry]: ...
def updateParm(scriptargs: ParmActionButtonKwargs, entry: PackFolderMenuEntry) -> Literal[False] | None: ...
def packFolderMenu(kwargs: ParmActionButtonKwargs, menutype: str) -> None: ...
