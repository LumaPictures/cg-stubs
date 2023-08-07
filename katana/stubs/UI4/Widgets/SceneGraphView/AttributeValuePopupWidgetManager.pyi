# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SceneGraphView.ItemDelegates.BaseItemDelegate
import UI4.Widgets.SceneGraphView.ItemDelegates.BaseItemDelegate
import UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate
import Utils as Utils
import typing
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class AttributeValuePopupWidget(PyQt5.QtWidgets.QWidget):
    BorderLineColor: ClassVar[PyQt5.QtGui.QColor] = ...
    MinimumPopupHeight: ClassVar[int] = ...
    MinimumPopupWidth: ClassVar[int] = ...
    Padding: ClassVar[int] = ...
    ShapePointPadding: ClassVar[int] = ...
    ShapePointWidth: ClassVar[int] = ...
    SizeHintHeightPadding: ClassVar[int] = ...
    SizeHintWidthPadding: ClassVar[int] = ...
    WindowFillColor: ClassVar[PyQt5.QtGui.QColor] = ...
    WindowFlags: ClassVar[PyQt5.QtCore.Qt.WindowType] = ...
    def __init__(self) -> None: ...
    def getActiveAreaRect(self) -> PyQt5.QtCore.QRect: ...
    def hideLater(self): ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
    def resizeToFitItemDelegate(self, sizeHint: PyQt5.QtCore.QSize): ...
    def show(self, index: PyQt5.QtCore.QModelIndex, itemDelegate: ParameterItemDelegate[UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate.ParameterItemDelegate], treeWidget: PyQt5.QtWidgets.QTreeWidget): ...

class AttributeValuePopupWidgetManager(PyQt5.QtCore.QObject):
    _instance: ClassVar[None] = ...
    def __init__(self) -> None: ...
    def eventFilter(self, obj, event): ...
    @classmethod
    def getInstance(cls) -> AttributeValuePopupWidgetManager: ...
    def hide(self): ...
    def setKeepVisible(self, keepVisible: bool): ...
    def show(self, index: PyQt5.QtCore.QModelIndex, itemDelegate: UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate, treeWidget: PyQt5.QtWidgets.QTreeWidget, keepVisible: bool = ...): ...

class ItemDelegateHostWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, index: Incomplete | None = ..., itemDelegate: Incomplete | None = ..., parent: Incomplete | None = ...) -> None: ...
    def _ItemDelegateHostWidget__on_model_dataChanged(self, startIndex: PyQt5.QtGui.QModelIndex, endIndex: PyQt5.QtGui.QModelIndex): ...
    def getItemDelegate(self) -> BaseItemDelegate[UI4.Widgets.SceneGraphView.ItemDelegates.BaseItemDelegate.BaseItemDelegate]: ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
    def setIndex(self, index: PyQt5.QtCore.QModelIndex): ...
    def setItemDelegate(self, itemDelegate: BaseItemDelegate[UI4.Widgets.SceneGraphView.ItemDelegates.BaseItemDelegate.BaseItemDelegate]): ...
    def setResizeCallback(self, callback: typing.Callable | None): ...
