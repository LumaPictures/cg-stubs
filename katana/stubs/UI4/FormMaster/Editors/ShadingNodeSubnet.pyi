# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.IconManager as IconManager
import NodegraphAPI as NodegraphAPI
import PyQt5.QtGui
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
import UI4.Widgets as Widgets
from QT4FormWidgets.FormWidget import FormWidget
from _typeshed import Incomplete
from typing import Set, Tuple

class ShadingNodeSubnetInterfaceOrderFormWidget(FormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__aboutToDragCallback(self, items, dragObject): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__dragMoveEventCallback(self, event, parent, index, callbackRecord): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__dropEventCallback(self, event, parent, index): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__findItemIndex(self, item): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__getParameterDrop(self, event): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__getSliceCount(self, item, count: Incomplete | None = ...): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__jumpToSource(self): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__listMousePressEvent(self, event): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__menuAboutToShow(self, menu, selectedItems: Incomplete | None = ...): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__treeContextMenuCallback(self, event: PyQt5.QtGui.QContextMenuEvent): ...
    def _ShadingNodeSubnetInterfaceOrderFormWidget__updateTree(self): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def valueChangedEvent(self, event): ...
