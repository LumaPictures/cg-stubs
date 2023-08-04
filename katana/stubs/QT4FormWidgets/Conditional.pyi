# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import ClassVar, Set, Tuple

class ConditionalVisibilityOpBase(PyQt5.QtCore.QObject):
    conditionalStateEval: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def _ConditionalVisibilityOpBase__targetPolicyChanged(self, event): ...
    def checkState(self): ...
    def freeze(self): ...
    def getProcessedTargetValue(self, value): ...
    def getTargetPolicy(self): ...
    def thaw(self): ...

class _OpAnd(_OpBoolean):
    def checkState(self): ...

class _OpBoolean(PyQt5.QtCore.QObject):
    conditionalStateEval: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, policy, hints, prefix) -> None: ...
    def _OpBoolean__operandChanged(self, state): ...
    def checkState(self): ...
    def freeze(self): ...
    def left(self): ...
    def right(self): ...
    def thaw(self): ...

class _OpContains(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpDoesNotContain(_OpContains):
    def checkState(self): ...

class _OpEqualTo(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpGreaterThan(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpGreaterThanOrEqualTo(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpIn(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpLessThan(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpLessThanOrEqualTo(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpNotEqualTo(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpNotIn(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

class _OpOr(_OpBoolean):
    def checkState(self): ...

class _OpRegexMatch(ConditionalVisibilityOpBase):
    def __init__(self, targetPolicy, hints, prefix) -> None: ...
    def checkState(self): ...

def ParseStandardConditionalHints(policy, hints): ...
def RegisterConditionalVisibilityOp(name, obj, pathIsNotParameter: bool = ...): ...
