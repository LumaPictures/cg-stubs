# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4Color as QT4Color
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.FormMaster.GroupParameterPolicy
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def GetCCArrayIndexHints(index, units): ...
def GetCCArrayIndexName(index): ...
def ShowColorPicker(colorPolicy: GroupParameterPolicy[UI4.FormMaster.GroupParameterPolicy.GroupParameterPolicy], widget: Incomplete | None = ...) -> PyQt5.QtWidgets.QDialog.DialogCode: ...
