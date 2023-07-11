# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QtCore as QtCore
import QtCore.Qt
from typing import Set, Tuple

LOG_DRAG_MIN: float
METHOD_LINEAR: int
METHOD_LOG: int

def ComputeAdjustedValue(startValue: int | float, delta: float, multiplier: float = ..., adjustmentMethod: int = ...) -> float: ...
def ComputeMultiplier(modifiers: QtCore.Qt.KeyboardModifiers) -> float: ...
def GetAdjustmentMethodFromString(methodStr: str) -> int: ...
