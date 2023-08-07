# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import UI4.Widgets.SceneGraphView.DataRoles as DataRoles
import UI4.Widgets.FilterPopups as FilterPopups
import NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import RenderingAPI.RenderPlugins as RenderPlugins
import RenderingAPI as RenderingAPI
import UI4.Util.ScenegraphIconManager as ScenegraphIconManager
import UI4.Widgets.FilterPopups
import UI4.Widgets.SceneGraphView.Bridge
import Utils as Utils
import typing
from UI4.Util.UndoGrouping import UndoContextGuard as UndoContextGuard
from UI4.Widgets.FilterPopups import LookFileMaterialFilterPopup as LookFileMaterialFilterPopup
from UI4.Widgets.SceneGraphView.ColumnDataType import RegisterDataType as RegisterDataType
from UI4.Widgets.SceneGraphView.ItemDelegates.BaseItemDelegate import BaseItemDelegate as BaseItemDelegate
from UI4.Widgets.SceneGraphView.ItemDelegates.ParameterItemDelegate import ParameterItemDelegate as ParameterItemDelegate
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ShaderItemDelegate(ParameterItemDelegate):
    class MaterialSelectionPopupFrame(PyQt5.QtWidgets.QFrame):
        def __init__(self, valuePolicy: ValuePolicy, lookFileAsset: str, lookFileMaterialPath: str, parent: Incomplete | None = ...) -> None: ...
        def _MaterialSelectionPopupFrame__lookFileChangedCallback(self, *args, **kwds): ...
        def _MaterialSelectionPopupFrame__on_lookFileMaterialFilterPopup_itemChosen(self, item, meta: Incomplete | None = ...): ...
        def _MaterialSelectionPopupFrame__on_shaderFilterPopup_itemChosen(self, item): ...
        def getShaderFilterPopup(self): ...
        def popup(self, globalPos): ...
        def setLookFileMaterialAssignmentCallback(self, callback, locationPath): ...
        def setMasterMaterialsRequestCallback(self, callback, locationPath): ...
        def setTemplateMaterialsRequestCallback(self, callback, locationPath): ...

    class ShaderFilterPopup(UI4.Widgets.FilterPopups.ShaderFilterPopup):
        class ItemDelegate(BaseItemDelegate):
            kTemplateMaterialColor: ClassVar[PyQt5.QtGui.QColor] = ...
            def initStyleOption(self, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex): ...
        def __init__(self, valuePolicy: ValuePolicy, parent: Incomplete | None = ...) -> None: ...
        def _refreshContents(self): ...
        def setMasterMaterialsRequestCallback(self, callback, locationPath): ...
        def setTemplateMaterialsRequestCallback(self, callback: typing.Callable, locationPath: str): ...
    AffectsOtherItemDelegates: ClassVar[bool] = ...
    OnParameterSetCallbackType: ClassVar[str] = ...
    kTemplateMaterialKey: ClassVar[str] = ...
    def __init__(self, bridge: Bridge[UI4.Widgets.SceneGraphView.Bridge.Bridge], treeWidget: PyQt5.QtWidgets.QTreeWidget, parent: Incomplete | None = ...) -> None: ...
    def _ShaderItemDelegate__assignTemplateMaterialToPackages(self, templateMaterialLocationPath: str, locationPaths: list[str]): ...
    def _ShaderItemDelegate__getShaderNodeAndParameter(self, index: PyQt5.QtCore.QModelIndex) -> tuple[NodegraphAPI.Node, NodegraphAPI.Parameter] | Tuple[None, None]: ...
    def _ShaderItemDelegate__getShaderSubTypeForLocation(self, locationPath: str) -> str | None: ...
    def _ShaderItemDelegate__on_removeAllShadersAction_triggered(self): ...
    def _ShaderItemDelegate__on_shaderFilterPopup_itemChosen(self, itemText: str, itemMeta: str): ...
    def _ShaderItemDelegate__on_shaderTypeAction_triggered(self): ...
    def _ShaderItemDelegate__on_unassignTemplateMaterialsAction_triggered(self): ...
    def _ShaderItemDelegate__removeAllShadersFromSelectedPackages(self): ...
    def _ShaderItemDelegate__setShaderForSelectedPackages(self, shaderType: str, shaderName: str): ...
    def _ShaderItemDelegate__setTemplateMaterialForSelectedPackages(self, templateMaterialLocationPath: str | None): ...
    def _ShaderItemDelegate__unassignTemplateMaterialsFromPackages(self, locationPaths: list[str]): ...
    def createContextMenu(self, index: PyQt5.QtCore.QModelIndex, selectedItems: list[PyQt5.QtWidgets.QTreeWidgetItem]) -> PyQt5.QtWidgets.QMenu | None: ...
    def createEditor(self, parent: PyQt5.QtWidgets.QWidget, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex) -> PyQt5.QtWidgets.QWidget | None: ...
    def initStyleOption(self, option: PyQt5.QtWidgets.QStyleOptionViewItem, index: PyQt5.QtCore.QModelIndex): ...
    def setLookFileMaterialCallback(self, lookFileMaterialAssignmentCallback: typing.Callable | None): ...
    def setMasterMaterialCallbacks(self, masterMaterialsRequestCallback: typing.Callable, masterMaterialAssignmentCallback: typing.Callable): ...
    def setTemplateMaterialCallbacks(self, templateMaterialsRequestCallback: typing.Callable, templateMaterialAssignmentCallback: typing.Callable): ...
