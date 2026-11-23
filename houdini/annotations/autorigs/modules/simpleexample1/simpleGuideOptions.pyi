import collections
from typing import TypedDict

from PySide6 import QtWidgets

class _SimpleOptionsJson(TypedDict):
    stretch: bool

class ModuleOptionsWidget(QtWidgets.QWidget):
    stretch_toggle: QtWidgets.QCheckBox
    def __init__(self) -> None: ...
    def fromJSON(self, json: _SimpleOptionsJson) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, bool]: ...
    def unlinkAllNodes(self) -> None: ...
