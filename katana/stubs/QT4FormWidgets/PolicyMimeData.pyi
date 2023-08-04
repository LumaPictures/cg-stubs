# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyQt5.QtCore
import PyXmlIO as PyXmlIO
import QT4FormWidgets
import PyQt5.QtCore as QtCore
from typing import Set, Tuple

class ParamMimeData(PyQt5.QtCore.QMimeData): ...

def GetMimeData(policy: QT4FormWidgets.AbstractValuePolicy) -> PyQt5.QtCore.QMimeData: ...
