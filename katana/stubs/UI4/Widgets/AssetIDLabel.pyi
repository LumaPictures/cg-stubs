# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4Widgets.PopdownLabel import PopdownLabel as PopdownLabel
from _typeshed import Incomplete
from typing import Set, Tuple

class AssetIDLabel(PopdownLabel):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def buildMenu(self, menu: PyQt5.QtWidgets.QMenu): ...
