from typing import TypeAlias

import hou
import husdui.models
import husdui.widgets
from pxr import Usd, UsdShade
from PySide6 import QtCore, QtWidgets

_AnyIndex: TypeAlias = QtCore.QModelIndex | QtCore.QPersistentModelIndex

HOTKEY_REMOVE_MATERIAL: str

theMLLhsTypes: list[type[UsdShade.Material]]
theMLRhsTypes: list[type[Usd.Typed]]

theSourceMenuXmlFilename: str
theMaterialLinkMaterialMenuXmlFilename: str
theMaterialLinkGeometryMenuXmlFilename: str
theMaterialLinkToolMenuXmlFilename: str

class MaterialLinkerWidget(husdui.widgets.LinkerWidget):
    def __init__(
        self, pane: hou.PythonPanel | None, parent: QtWidgets.QWidget | None = ...
    ) -> None: ...

class MaterialAssetDropPlugin(husdui.models.AbstractDropHandlerPlugin):
    def mimeTypes(self) -> list[str]: ...
    def canDropMimeData(
        self,
        mimedata: QtCore.QMimeData,
        action: QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: _AnyIndex,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> bool: ...
    def dropMimeData(
        self,
        mimedata: QtCore.QMimeData,
        action: QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: _AnyIndex,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> bool: ...
    def flags(
        self,
        index: _AnyIndex,
        flags: QtCore.Qt.ItemFlag,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> QtCore.Qt.ItemFlag: ...

class MaterialAssetRefDropPlugin(husdui.models.AbstractDropHandlerPlugin):
    def mimeTypes(self) -> list[str]: ...
    def canDropMimeData(
        self,
        mimedata: QtCore.QMimeData,
        action: QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: _AnyIndex,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> bool: ...
    def dropMimeData(
        self,
        mimedata: QtCore.QMimeData,
        action: QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: _AnyIndex,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> bool: ...
    def flags(
        self,
        index: _AnyIndex,
        flags: QtCore.Qt.ItemFlag,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> QtCore.Qt.ItemFlag: ...
    def setData(
        self,
        index: _AnyIndex,
        value: object,
        role: int,
        stage: Usd.Stage | None,
        node: hou.LopNode | None,
    ) -> bool: ...

class MaterialLinkRuleModel(husdui.models.RuleModel):
    def __init__(
        self, node: hou.LopNode | None = ..., parent: QtCore.QObject | None = ...
    ) -> None: ...
    def mimeTypes(self) -> list[str]: ...
    def canDropMimeData(
        self,
        mimedata: QtCore.QMimeData,
        action: QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: QtCore.QModelIndex,
    ) -> bool: ...
    def dropMimeData(
        self,
        mimedata: QtCore.QMimeData,
        action: QtCore.Qt.DropAction,
        row: int,
        column: int,
        parent_index: QtCore.QModelIndex,
    ) -> bool: ...
