# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import PyQt5.QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from typing import Set, Tuple

def GetApplicationIcon() -> PyQt5.QtGui.QIcon: ...
