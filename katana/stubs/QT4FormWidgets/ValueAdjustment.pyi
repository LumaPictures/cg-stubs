# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtCore as QtCore
from typing import Set, Tuple

def ComputeAdjustedValue(startValue: int | float, delta: float, multiplier: float = ..., adjustmentMethod: int = ...) -> float: ...
def ComputeMultiplier(modifiers: PyQt5.QtCore.Qt.KeyboardModifiers) -> float: ...
def GetAdjustmentMethodFromString(methodStr: str) -> int: ...
