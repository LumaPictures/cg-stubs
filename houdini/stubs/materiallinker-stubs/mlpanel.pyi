import hou
import husdui.models
import husdui.widgets
from husd.utils import expandCollectionPath as expandCollectionPath, getCollection as getCollection
from hutil.PySide import QtCore, QtWidgets
from pxr import Usd as Usd, UsdShade

from typing import TypeAlias
from typing import TypeAlias
_AnyIndex: TypeAlias = QtCore.QModelIndex | QtCore.QPersistentModelIndex
HOTKEY_REMOVE_MATERIAL: str
theMLLhsTypes: list[type[UsdShade.Material]]
theMLRhsTypes: list[type[Usd.Typed]]
theSourceMenuXmlFilename: str
theMaterialLinkMaterialMenuXmlFilename: str
theMaterialLinkGeometryMenuXmlFilename: str
theMaterialLinkToolMenuXmlFilename: str

class MaterialLinkerWidget(husdui.widgets.LinkerWidget):
    def __init__(self, pane: hou.PythonPanel | None, parent: QtWidgets.QWidget | None = None) -> None: ...

class MaterialAssetDropPlugin(husdui.models.AbstractDropHandlerPlugin):
    """
    Plugin to allow dropping a material onto a prim in the targets tree in
    order to assign that material to the prim.
    """
    def mimeTypes(self) -> list[str]: ...
    def canDropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: _AnyIndex, stage: Usd.Stage | None, node: hou.LopNode | None) -> bool: ...
    def dropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: _AnyIndex, stage: Usd.Stage | None, node: hou.LopNode | None) -> bool: ...
    def flags(self, index: _AnyIndex, flags: QtCore.Qt.ItemFlag, stage: Usd.Stage | None, node: hou.LopNode | None) -> QtCore.Qt.ItemFlag: ...

class MaterialAssetRefDropPlugin(husdui.models.AbstractDropHandlerPlugin):
    """
    Plugin to allow dropping a material asset into the materials list/tree in
    order to create a referene to that material asset.
    """
    def mimeTypes(self) -> list[str]: ...
    def canDropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: _AnyIndex, stage: Usd.Stage | None, node: hou.LopNode | None) -> bool: ...
    def dropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: _AnyIndex, stage: Usd.Stage | None, node: hou.LopNode | None) -> bool: ...
    def flags(self, index: _AnyIndex, flags: QtCore.Qt.ItemFlag, stage: Usd.Stage | None, node: hou.LopNode | None) -> QtCore.Qt.ItemFlag: ...
    def setData(self, index: _AnyIndex, value: object, role: int, stage: Usd.Stage | None, node: hou.LopNode | None) -> bool: ...

class MaterialLinkRuleModel(husdui.models.RuleModel):
    def __init__(self, node: hou.LopNode | None = None, parent: QtCore.QObject | None = None) -> None: ...
    def mimeTypes(self) -> list[str]: ...
    def canDropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: QtCore.QModelIndex) -> bool: ...
    def dropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: QtCore.QModelIndex) -> bool: ...
