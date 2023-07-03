# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils as Utils

ActionText: dict
Continuous: int
Manual: int
Modes: tuple
Options: list
PenUp: int
__dirty: bool
__updateMode: int

def GetUpdateMode() -> int: ...
def IsDirty(): ...
def SetDirty(dirty): ...
def SetUpdateMode(updateMode: int): ...
def TriggerManualUpdate(): ...