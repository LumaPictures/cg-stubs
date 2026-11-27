from typing import ClassVar, Self

from typing_extensions import Unpack

import PySide6.QtCore
from pxr import Pcp, Usd

import hou
from hutil.qt.common import core
from hutil.qt.info import nodeinfo, window
from hutil.qt.info.window import _BaseInfoStateKwargs

current_prim_win: UsdInfoWindow | None
attr_source_label: dict[Usd.ResolveInfoSource, str]
arc_type_label: dict[Pcp.ArcType, str]
arc_type_order: tuple[Pcp.ArcType, ...]

def material(prim: Usd.Prim, token: str) -> str: ...
def arcKey(name: Pcp.ArcType) -> int: ...

class CollectionInfo(core.Info):
    expression: str
    members: list[nodeinfo.UsdPrimInfo]
    expressionChanged: ClassVar[PySide6.QtCore.Signal]
    membersChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forCollection(cls, stage: Usd.Stage, obj: Usd.CollectionAPI) -> Self: ...

class RelationshipInfo(core.Info):
    targets: list[nodeinfo.UsdPrimInfo]
    targetsChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forRelationship(cls, stage: Usd.Stage, obj: Usd.Relationship) -> Self: ...

class AssetInfo(core.Info):
    primPath: str
    identifier: str
    name: str
    thumbnailURL: PySide6.QtCore.QUrl
    primPathChanged: ClassVar[PySide6.QtCore.Signal]
    identifierChanged: ClassVar[PySide6.QtCore.Signal]
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    thumbnailURLChanged: ClassVar[PySide6.QtCore.Signal]

class ExtendedPrimInfo(nodeinfo.UsdPrimInfo):
    active: bool
    activeAuthored: bool
    loaded: bool
    previewMaterial: str
    fullMaterial: str
    visible: bool
    purpose: str
    counts: nodeinfo.UsdPrimCounts
    appliedSchemas: list[str]
    compositionCounts: list[nodeinfo.Number]
    assetInfo: AssetInfo | None
    bboxEmpty: bool
    bboxMin: tuple[float, float, float]
    bboxMax: tuple[float, float, float]
    bboxSize: tuple[float, float, float]
    bboxCenter: tuple[float, float, float]
    activeChanged: ClassVar[PySide6.QtCore.Signal]
    activeAuthoredChanged: ClassVar[PySide6.QtCore.Signal]
    loadedChanged: ClassVar[PySide6.QtCore.Signal]
    previewMaterialChanged: ClassVar[PySide6.QtCore.Signal]
    fullMaterialChanged: ClassVar[PySide6.QtCore.Signal]
    visibleChanged: ClassVar[PySide6.QtCore.Signal]
    purposeChanged: ClassVar[PySide6.QtCore.Signal]
    countsChanged: ClassVar[PySide6.QtCore.Signal]
    appliedSchemasChanged: ClassVar[PySide6.QtCore.Signal]
    compositionCountsChanged: ClassVar[PySide6.QtCore.Signal]
    assetInfoChanged: ClassVar[PySide6.QtCore.Signal]
    bboxEmptyChanged: ClassVar[PySide6.QtCore.Signal]
    bboxMinChanged: ClassVar[PySide6.QtCore.Signal]
    bboxMaxChanged: ClassVar[PySide6.QtCore.Signal]
    bboxSizeChanged: ClassVar[PySide6.QtCore.Signal]
    bboxCenterChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: object) -> None: ...
    @classmethod
    def forPrimExtended(cls, node: hou.LopNode, prim: Usd.Prim) -> Self: ...
    def node(self) -> hou.LopNode | None: ...
    def fillPrimCounts(self, *, lop_geo_details: bool = ..., kind_details: bool = ..., timeout_ms: int = ...) -> None: ...

class RuleInfo(core.Info):
    pattern: str
    matches: list[nodeinfo.UsdPrimInfo]
    patternChanged: ClassVar[PySide6.QtCore.Signal]
    matchesChanged: ClassVar[PySide6.QtCore.Signal]

class AttributeInfo(core.Info):
    isArray: bool
    uniform: bool
    roleName: str
    dataTypeName: str
    source: str
    colorSpace: str
    sampleCount: int
    sampleCountString: str
    documentation: str
    isArrayChanged: ClassVar[PySide6.QtCore.Signal]
    uniformChanged: ClassVar[PySide6.QtCore.Signal]
    roleNameChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    sourceChanged: ClassVar[PySide6.QtCore.Signal]
    colorSpaceChanged: ClassVar[PySide6.QtCore.Signal]
    sampleCountChanged: ClassVar[PySide6.QtCore.Signal]
    sampleCountStringChanged: ClassVar[PySide6.QtCore.Signal]
    documentationChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forAttr(cls, obj: Usd.Attribute) -> Self: ...

class UsdInfo(core.Info):
    lopPath: str
    lopName: str
    lopIcon: str
    fullPath: str
    parentPath: str
    primName: str
    name: str
    typeName: str
    iconName: str
    collection: CollectionInfo | None
    relationship: RelationshipInfo | None
    prim: ExtendedPrimInfo | None
    rule: RuleInfo | None
    attribute: AttributeInfo | None
    lopPathChanged: ClassVar[PySide6.QtCore.Signal]
    lopNameChanged: ClassVar[PySide6.QtCore.Signal]
    lopIconChanged: ClassVar[PySide6.QtCore.Signal]
    fullPathChanged: ClassVar[PySide6.QtCore.Signal]
    parentPathChanged: ClassVar[PySide6.QtCore.Signal]
    primNameChanged: ClassVar[PySide6.QtCore.Signal]
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    iconNameChanged: ClassVar[PySide6.QtCore.Signal]
    collectionChanged: ClassVar[PySide6.QtCore.Signal]
    relationshipChanged: ClassVar[PySide6.QtCore.Signal]
    primChanged: ClassVar[PySide6.QtCore.Signal]
    ruleChanged: ClassVar[PySide6.QtCore.Signal]
    attributeChanged: ClassVar[PySide6.QtCore.Signal]
    def lopNode(self) -> hou.LopNode | None: ...
    def fillFromObject(self, node: hou.LopNode, prim_path: str) -> None: ...
    def fillFromRule(self, node: hou.LopNode, name: str) -> None: ...

class UsdConfig(window.NodeInfoConfig): ...

class UsdState(window.BaseInfoState[UsdConfig, UsdInfo]):
    reloadable: bool
    reloadableChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: Unpack[_BaseInfoStateKwargs]) -> None: ...
    def reload(self, recook: bool = ..., force_update: bool = ...) -> None: ...
    def outOfDate(self) -> bool: ...
    def lopNode(self) -> hou.LopNode | None: ...
    def primPath(self) -> str | None: ...
    def setObject(self, lop_node: hou.LopNode | None, prim_path: str, is_rule: bool = ..., force_cook: bool = ...) -> None: ...

class UsdInfoWindow(window.InfoViewWindow[UsdState]):
    SOURCE_URL: str
    def isTransient(self) -> bool: ...
    def pathKey(self) -> str: ...
    def display(self, node: hou.LopNode, path: str, is_rule: bool = ..., pos: PySide6.QtCore.QPoint | None = ..., interactive: bool = ..., force_cook: bool = ...) -> None: ...

def closeUsdInfoWindow() -> None: ...
def createInfoWindow(node: hou.LopNode, path: str, is_rule: bool = ..., interactive: bool = ..., force_cook: bool = ...) -> UsdInfoWindow: ...
