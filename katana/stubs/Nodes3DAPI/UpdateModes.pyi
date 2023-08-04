# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils as Utils
from typing import Set, Tuple

ActionText: dict
Continuous: int
Manual: int
Modes: tuple
Options: list
PenUp: int

def GetUpdateMode() -> int: ...
def IsDirty(): ...
def SetDirty(dirty): ...
def SetUpdateMode(updateMode: int): ...
def TriggerManualUpdate(): ...
