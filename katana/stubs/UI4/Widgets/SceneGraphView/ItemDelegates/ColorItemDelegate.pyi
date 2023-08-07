# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4Color as QT4Color
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.FormMaster.BaseParameterPolicy
import UI4.Widgets.SceneGraphView.Bridge
import Utils as Utils
from UI4.Widgets.SceneGraphView.ColumnDataType import RegisterDataType as RegisterDataType
from UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate import ParameterItemDelegate as ParameterItemDelegate
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ColorItemDelegate(ParameterItemDelegate):
    ColorSwatchWidth: ClassVar[int] = ...
    DefaultColumnWidth: ClassVar[int] = ...
    MaximumColumnWidth: ClassVar[int] = ...
    Padding: ClassVar[int] = ...
    PaddingRight: ClassVar[int] = ...
    def __init__(self, bridge: Bridge[UI4.Widgets.SceneGraphView.Bridge.Bridge], treeWidget: PyQt5.QtWidgets.QTreeWidget, parent: Incomplete | None = ...) -> None: ...
    def _ColorItemDelegate__getDisplayValues(self, index): ...
    def createEditor(self, parent: PyQt5.QtWidgets.QWidget, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex) -> PyQt5.QtWidgets.QWidget | None: ...
    def doesParameterValueMatchModelValue(self, parameterPolicy: BaseParameterPolicy[UI4.FormMaster.BaseParameterPolicy.BaseParameterPolicy], index: PyQt5.QtCore.QModelIndex) -> bool: ...
    def isFilmlookEnabled(self) -> bool: ...
    def paint(self, painter: PyQt5.QtGui.QPainter, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex): ...
    def setFilmlookEnabled(self, filmlookEnabled: bool): ...
