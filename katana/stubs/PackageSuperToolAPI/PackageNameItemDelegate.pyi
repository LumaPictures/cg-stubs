# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import NodegraphAPI as NodegraphAPI
import PackageSuperToolAPI.Packages
import PackageSuperToolAPI.Packages as Packages
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SceneGraphView
from UI4.Widgets.SceneGraphView.ItemDelegates.NameItemDelegate import NameItemDelegate
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class PackageNameItemDelegate(NameItemDelegate):
    DefaultColumnWidth: ClassVar[int] = ...
    MaximumColumnWidth: ClassVar[None] = ...
    def __init__(self, bridge: UI4.Widgets.SceneGraphView.Bridge, treeWidget: PyQt5.QtWidgets.QTreeWidget, parent: Incomplete | None = ...) -> None: ...
    def _PackageNameItemDelegate__getEditPackageClass(self, locationPath: str) -> type | None: ...
    def _PackageNameItemDelegate__getErrorOrWarning(self, locationPath: str) -> tuple[bool, bool, str, str]: ...
    def _PackageNameItemDelegate__getIcon(self, iconNameOrFilename: str, desiredResolution: int = ...) -> PyQt5.QtGui.QIcon | None: ...
    def _PackageNameItemDelegate__getPackageFromSceneGraphLocation(self, locationPath: str) -> PackageSuperToolAPI.Packages.Package | None: ...
    def _PackageNameItemDelegate__isErrorOrWarning(self, locationPath) -> bool: ...
    def createEditor(self, parent: PyQt5.QtWidgets.QWidget, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex) -> PyQt5.QtWidgets.QWidget | None: ...
    def initStyleOption(self, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex): ...
    def setModelData(self, editor: PyQt5.QtWidgets.QWidget, model: PyQt5.QtCore.QAbstractItemModel, index: PyQt5.QtCore.QModelIndex): ...
    def setSuperToolName(self, superToolName: str | None): ...
    def toolTipEvent(self, index: PyQt5.QtCore.QModelIndex): ...
