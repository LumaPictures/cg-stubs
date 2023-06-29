# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils as Utils

_Callbacks: list
_PostCallbacks: list

def flush(isNodeGraphLoading: bool = ...): ...
def registerFlushCallback(fnc, post: bool = ...): ...
def setDirty(): ...