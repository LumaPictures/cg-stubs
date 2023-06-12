# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"


STATE_MIXED: int
STATE_OFF: int
STATE_ON: int

class MixedGroupState:
    def __init__(self): ...
    def _MixedGroupState__resolveState(self): ...
    def addState(self, state): ...
    def getState(self): ...
    def removeState(self, state): ...
    def swapState(self, fromState, toState): ...