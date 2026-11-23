import re
from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence
from datetime import datetime
from typing import Any, ClassVar, Self, TypeVar

import PySide6.QtCore
import PySide6.QtGui
from pxr import Usd

import hou
from hutil.qt.common import core
from hutil.qt.info import attrdiffs, custom, tops
from hutil.qt.pluto import colors

_T = TypeVar("_T")

GENERIC_VIZ: hou.ViewportVisualizerType
TAG_VIZ: hou.ViewportVisualizerType
COLOR_VIZ: hou.ViewportVisualizerType
MARKER_VIZ: hou.ViewportVisualizerType
var_expr: re.Pattern[str]
geo_memory_expr: re.Pattern[str]
node_specific_branch_expr: re.Pattern[str]
node_path_expr: re.Pattern[str]
lop_geo_count_key_expr: re.Pattern[str]
def abbr(string: str, weight: int = ...) -> str: ...
def span(string: str, weight: int = ...) -> str: ...
def markupFloat(string: float | str, show_fraction: bool = ..., whole_weight: int = ..., fraction_weight: int = ...) -> str: ...
def divideSeconds(secs: float) -> tuple[int, int, float]: ...
def formatHMS(secs: float, markup: bool = ..., decimal_places: int = ..., auto_decimal: int = ..., less_than_1_ms: bool = ..., whole_weight: int = ..., fraction_weight: int = ..., zero: str = ...) -> str: ...
def almostEqual(x: float, y: float, places: int = ...) -> bool: ...
def formatNum(value: float, places: int = ...) -> str: ...
def formatVoxelSize(size: hou.Vector3) -> str: ...
def usdPrimIcon(prim_name: str) -> str: ...
def countListKeyFn(exemplars: Sequence[str]) -> Callable[[Number], int]: ...
def formatDatetime(dt: datetime, relative_days: bool = ..., use_24h: bool = ...) -> str: ...
def objSortKey(obj: hou.Attrib | hou.PointGroup | hou.PrimGroup | hou.EdgeGroup | hou.VertexGroup) -> tuple[str | int, ...]: ...
def refSortKeyFn(node: hou.Node, parm_refs: bool = ...) -> Callable[[str], tuple[int, str]]: ...
def unique(seq: Iterable[_T]) -> list[_T]: ...
def nodeTypeSummary(nodetype: hou.NodeType) -> str | None: ...
def attrBriefDataDesc(attrib: hou.Attrib, pref_prec: int) -> str: ...
def attrFullDataDesc(attrib: hou.Attrib, include_string_count: bool = ...) -> str: ...
def attrDataTypeColor(attrib: hou.Attrib) -> PySide6.QtGui.QColor | None: ...
def attrQualifers(attrib: hou.Attrib) -> tuple[str, str]: ...
def frozenGeometry(node: hou.SopNode, output_index: int = ...) -> hou.Geometry | None: ...
def nodeDefinitionString(node: hou.Node) -> str | None: ...
def objectOutputNode(obj_node: hou.Node) -> hou.Node | None: ...
def countLabel(noun: str, count: int, plural: str | None = ...) -> str: ...
def getDataId(data_id: hou.AttribDataId | tuple[int, ...]) -> int: ...
def trs(m: hou.Matrix4, xform_order: str, rot_order: str, pivot: hou.Vector3, pivot_rot: hou.Vector3) -> list[tuple[float, float, float]]: ...
def makeAttr(attrib: hou.Attrib, type_name: str, pref_prec: int, debug: bool = ..., added_names: Collection[str] | None = ..., diffs: attrdiffs.Differences | None = ..., full_diff: bool = ..., viz_names: Collection[str] | None = ...) -> Attr: ...
def attrIterator(geom: hou.Geometry, type_name: str, debug: bool = ..., viz_names: Collection[str] | None = ..., diffs: attrdiffs.Differences | None = ..., full_diff: bool = ...) -> tuple[int, Iterator[Attr]]: ...
def getAttrs(geom: hou.Geometry, type_name: str, debug: bool = ..., viz_names: Collection[str] | None = ..., diffs: attrdiffs.Differences | None = ..., full_diff: bool = ...) -> tuple[int, list[Attr]]: ...
def _annoAttrs(attr_type: hou.EnumValue[hou.attribType], attrs: list[Attr], diffs: attrdiffs.Differences, full_diff: bool) -> None: ...
def getGroups(geom: hou.Geometry, group_type: str) -> list[Group]: ...
def linkify(node: hou.Node, text: str, weight: int = ...) -> str: ...
def brectToRect(br: hou.BoundingRect) -> PySide6.QtCore.QRectF: ...
def xformToString(xform: hou.Matrix4, t: tuple[float, float, float], r: tuple[float, float, float], s: tuple[float, float, float]) -> str: ...
class PerfStats(core.Info):
    profileName: str
    cookCount: int
    cookCountString: str
    cookTotal: float
    cookTotalString: str
    cookSelf: float
    cookSelfString: str
    cookAvg: float
    cookAvgString: str
    cookMin: float
    cookMinString: str
    cookMax: float
    cookMaxString: str
    startFrame: int
    endFrame: int
    perFrame: list[float]
    perFrameNormalized: list[float]
    profileNameChanged: ClassVar[PySide6.QtCore.Signal]
    cookCountChanged: ClassVar[PySide6.QtCore.Signal]
    cookCountStringChanged: ClassVar[PySide6.QtCore.Signal]
    cookTotalChanged: ClassVar[PySide6.QtCore.Signal]
    cookTotalStringChanged: ClassVar[PySide6.QtCore.Signal]
    cookSelfChanged: ClassVar[PySide6.QtCore.Signal]
    cookSelfStringChanged: ClassVar[PySide6.QtCore.Signal]
    cookAvgChanged: ClassVar[PySide6.QtCore.Signal]
    cookAvgStringChanged: ClassVar[PySide6.QtCore.Signal]
    cookMinChanged: ClassVar[PySide6.QtCore.Signal]
    cookMinStringChanged: ClassVar[PySide6.QtCore.Signal]
    cookMaxChanged: ClassVar[PySide6.QtCore.Signal]
    cookMaxStringChanged: ClassVar[PySide6.QtCore.Signal]
    startFrameChanged: ClassVar[PySide6.QtCore.Signal]
    endFrameChanged: ClassVar[PySide6.QtCore.Signal]
    perFrameChanged: ClassVar[PySide6.QtCore.Signal]
    perFrameNormalizedChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forPath(cls, node_path: str) -> PerfStats | None: ...
class Message(core.Info):
    original: str
    html: str
    originalChanged: ClassVar[PySide6.QtCore.Signal]
    htmlChanged: ClassVar[PySide6.QtCore.Signal]
class Xform(core.Info):
    isIdentity: bool
    translate: tuple[float, float, float]
    rotate: tuple[float, float, float]
    scale: tuple[float, float, float]
    string: str
    isIdentityChanged: ClassVar[PySide6.QtCore.Signal]
    translateChanged: ClassVar[PySide6.QtCore.Signal]
    rotateChanged: ClassVar[PySide6.QtCore.Signal]
    scaleChanged: ClassVar[PySide6.QtCore.Signal]
    stringChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def fromMatrix(cls, mtx: hou.Matrix4, xord: str = ..., rord: str = ..., pivot: tuple[float, ...] | list[float] | hou.Vector3 = ..., pivot_rot: tuple[float, ...] | list[float] | hou.Vector3 = ...) -> Xform: ...
class PathExpansion(core.Info):
    rawText: str
    expandedText: str
    rawHtml: str
    expandedHtml: str
    rawTextChanged: ClassVar[PySide6.QtCore.Signal]
    expandedTextChanged: ClassVar[PySide6.QtCore.Signal]
    rawHtmlChanged: ClassVar[PySide6.QtCore.Signal]
    expandedHtmlChanged: ClassVar[PySide6.QtCore.Signal]
def expandedPath(parm: hou.Parm, theme: colors.Theme) -> PathExpansion: ...
class ObjInfo(core.Info):
    origin: tuple[float, float, float]
    pivot: tuple[float, float, float]
    pivotRotate: tuple[float, float, float]
    xformOrder: str
    rotateOrder: str
    xformOrderString: str
    displayNodeName: str
    renderNodeName: str
    preXform: Xform
    worldXform: Xform
    localXform: Xform
    originChanged: ClassVar[PySide6.QtCore.Signal]
    pivotChanged: ClassVar[PySide6.QtCore.Signal]
    pivotRotateChanged: ClassVar[PySide6.QtCore.Signal]
    xformOrderChanged: ClassVar[PySide6.QtCore.Signal]
    rotateOrderChanged: ClassVar[PySide6.QtCore.Signal]
    xformOrderStringChanged: ClassVar[PySide6.QtCore.Signal]
    displayNodeNameChanged: ClassVar[PySide6.QtCore.Signal]
    renderNodeNameChanged: ClassVar[PySide6.QtCore.Signal]
    preXformChanged: ClassVar[PySide6.QtCore.Signal]
    worldXformChanged: ClassVar[PySide6.QtCore.Signal]
    localXformChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forNode(cls, node: hou.Node, recook: bool = ...) -> ObjInfo | None: ...
class ChopTrack(core.Info):
    name: str
    color: PySide6.QtGui.QColor
    sampleCount: int
    current: float
    minimum: float
    maximum: float
    extendLeft: str
    extendRight: str
    override: str
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    colorChanged: ClassVar[PySide6.QtCore.Signal]
    sampleCountChanged: ClassVar[PySide6.QtCore.Signal]
    currentChanged: ClassVar[PySide6.QtCore.Signal]
    minimumChanged: ClassVar[PySide6.QtCore.Signal]
    maximumChanged: ClassVar[PySide6.QtCore.Signal]
    extendLeftChanged: ClassVar[PySide6.QtCore.Signal]
    extendRightChanged: ClassVar[PySide6.QtCore.Signal]
    overrideChanged: ClassVar[PySide6.QtCore.Signal]
class ChopInfo(core.Info):
    mode: str
    sampleRate: float
    sampleCount: int
    frameCount: int
    duration: float
    durationString: str
    startSample: int
    startFrame: float
    startTime: float
    startTimeString: str
    endSample: int
    endFrame: float
    endTime: float
    endTimeString: str
    tracks: list[ChopTrack]
    minimum: float
    maximum: float
    minMaxString: str
    hasOverrides: bool
    modeChanged: ClassVar[PySide6.QtCore.Signal]
    sampleRateChanged: ClassVar[PySide6.QtCore.Signal]
    sampleCountChanged: ClassVar[PySide6.QtCore.Signal]
    frameCountChanged: ClassVar[PySide6.QtCore.Signal]
    durationChanged: ClassVar[PySide6.QtCore.Signal]
    durationStringChanged: ClassVar[PySide6.QtCore.Signal]
    startSampleChanged: ClassVar[PySide6.QtCore.Signal]
    startFrameChanged: ClassVar[PySide6.QtCore.Signal]
    startTimeChanged: ClassVar[PySide6.QtCore.Signal]
    startTimeStringChanged: ClassVar[PySide6.QtCore.Signal]
    endSampleChanged: ClassVar[PySide6.QtCore.Signal]
    endFrameChanged: ClassVar[PySide6.QtCore.Signal]
    endTimeChanged: ClassVar[PySide6.QtCore.Signal]
    endTimeStringChanged: ClassVar[PySide6.QtCore.Signal]
    tracksChanged: ClassVar[PySide6.QtCore.Signal]
    minimumChanged: ClassVar[PySide6.QtCore.Signal]
    maximumChanged: ClassVar[PySide6.QtCore.Signal]
    minMaxStringChanged: ClassVar[PySide6.QtCore.Signal]
    hasOverridesChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forNode(cls, node: hou.Node, output_index: int) -> ChopInfo | None: ...
class Attr(core.Info):
    name: str
    typeName: str
    dataType: str
    size: int
    dataTypeName: str
    dataTypeDesc: str
    dataTypeColor: PySide6.QtGui.QColor
    qualifier: str
    qualifierBrief: str
    stringCount: int
    visualized: bool
    isNew: bool
    isModified: bool
    isEdited: bool
    isDeleted: bool
    diffText: str
    debugDataID: int
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeChanged: ClassVar[PySide6.QtCore.Signal]
    sizeChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeDescChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeColorChanged: ClassVar[PySide6.QtCore.Signal]
    qualifierChanged: ClassVar[PySide6.QtCore.Signal]
    qualifierBriefChanged: ClassVar[PySide6.QtCore.Signal]
    stringCountChanged: ClassVar[PySide6.QtCore.Signal]
    visualizedChanged: ClassVar[PySide6.QtCore.Signal]
    isNewChanged: ClassVar[PySide6.QtCore.Signal]
    isModifiedChanged: ClassVar[PySide6.QtCore.Signal]
    isEditedChanged: ClassVar[PySide6.QtCore.Signal]
    isDeletedChanged: ClassVar[PySide6.QtCore.Signal]
    diffTextChanged: ClassVar[PySide6.QtCore.Signal]
    debugDataIDChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def deleted(cls, name: str) -> Self: ...
class Group(core.Info):
    name: str
    typeName: str
    count: int
    isOrdered: bool
    visualized: bool
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    countChanged: ClassVar[PySide6.QtCore.Signal]
    isOrderedChanged: ClassVar[PySide6.QtCore.Signal]
    visualizedChanged: ClassVar[PySide6.QtCore.Signal]
class VolumeInfo(core.Info):
    name: str
    primNum: int
    typeName: str
    resolution: tuple[int, ...]
    resolutionStr: str
    voxelSize: tuple[float, ...]
    voxelSizeStr: str
    visMode: str
    isHeightfield: bool
    isSDF: bool
    dataTypeName: str
    isEmpty: bool
    voxelCount: int
    voxelCountStr: str
    backgroundStr: str
    bandwidthStr: str
    visualized: bool
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    primNumChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    resolutionChanged: ClassVar[PySide6.QtCore.Signal]
    resolutionStrChanged: ClassVar[PySide6.QtCore.Signal]
    voxelSizeChanged: ClassVar[PySide6.QtCore.Signal]
    voxelSizeStrChanged: ClassVar[PySide6.QtCore.Signal]
    visModeChanged: ClassVar[PySide6.QtCore.Signal]
    isHeightfieldChanged: ClassVar[PySide6.QtCore.Signal]
    isSDFChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    isEmptyChanged: ClassVar[PySide6.QtCore.Signal]
    voxelCountChanged: ClassVar[PySide6.QtCore.Signal]
    voxelCountStrChanged: ClassVar[PySide6.QtCore.Signal]
    backgroundStrChanged: ClassVar[PySide6.QtCore.Signal]
    bandwidthStrChanged: ClassVar[PySide6.QtCore.Signal]
    visualizedChanged: ClassVar[PySide6.QtCore.Signal]
    def setResolution(self, resolution: hou.Vector3) -> None: ...
    def setVoxelCount(self, count: int) -> None: ...
    def setVoxelSize(self, size: hou.Vector3) -> None: ...
    @classmethod
    def fromDopData(cls, name: str, data: hou.DopData) -> VolumeInfo: ...
    @classmethod
    def fromPrim(cls, prim: hou.Volume, name: str | None = ...) -> VolumeInfo: ...
class GeometryMemory(core.Info):
    full: str
    isInstanced: bool
    new: str
    unique: str
    fullChanged: ClassVar[PySide6.QtCore.Signal]
    isInstancedChanged: ClassVar[PySide6.QtCore.Signal]
    newChanged: ClassVar[PySide6.QtCore.Signal]
    uniqueChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def fromString(cls, geo_memory: str) -> GeometryMemory: ...
class Number(core.Info):
    name: str
    iconName: str
    value: float
    valueString: str
    fraction: float
    color: PySide6.QtGui.QColor
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    iconNameChanged: ClassVar[PySide6.QtCore.Signal]
    valueChanged: ClassVar[PySide6.QtCore.Signal]
    valueStringChanged: ClassVar[PySide6.QtCore.Signal]
    fractionChanged: ClassVar[PySide6.QtCore.Signal]
    colorChanged: ClassVar[PySide6.QtCore.Signal]
class DonutItem(core.Info):
    name: str
    text: str
    value: float
    color: PySide6.QtGui.QColor
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    textChanged: ClassVar[PySide6.QtCore.Signal]
    valueChanged: ClassVar[PySide6.QtCore.Signal]
    colorChanged: ClassVar[PySide6.QtCore.Signal]
class GeoInfo(core.Info):
    sessionID: int
    outputIndex: int
    isSop: bool
    bboxSize: list[float]
    bboxCenter: list[float]
    bboxMin: list[float]
    bboxMax: list[float]
    primCount: int
    primCountString: str
    pointCount: int
    pointCountString: str
    vertexCount: int
    vertexCountString: str
    componentCounts: list[Number]
    primTypeCounts: list[Number]
    detailAttrs: list[Attr]
    primitiveAttrs: list[Attr]
    pointAttrs: list[Attr]
    vertexAttrs: list[Attr]
    canShowDiffs: bool
    detailAttrCount: int
    primitiveAttrCount: int
    pointAttrCount: int
    vertexAttrCount: int
    primGroups: list[Group]
    pointGroups: list[Group]
    vertexGroups: list[Group]
    edgeGroups: list[Group]
    memory: GeometryMemory
    volumes: list[VolumeInfo]
    debugChangeCount: int
    debugDetailID: int
    debugPrimID: int
    debugTopologyID: int
    debugChangeCountAltered: bool
    debugDetailIDAltered: bool
    debugPrimIDAltered: bool
    debugTopologyIDAltered: bool
    sessionIDChanged: ClassVar[PySide6.QtCore.Signal]
    outputIndexChanged: ClassVar[PySide6.QtCore.Signal]
    isSopChanged: ClassVar[PySide6.QtCore.Signal]
    bboxSizeChanged: ClassVar[PySide6.QtCore.Signal]
    bboxCenterChanged: ClassVar[PySide6.QtCore.Signal]
    bboxMinChanged: ClassVar[PySide6.QtCore.Signal]
    bboxMaxChanged: ClassVar[PySide6.QtCore.Signal]
    primCountChanged: ClassVar[PySide6.QtCore.Signal]
    primCountStringChanged: ClassVar[PySide6.QtCore.Signal]
    pointCountChanged: ClassVar[PySide6.QtCore.Signal]
    pointCountStringChanged: ClassVar[PySide6.QtCore.Signal]
    vertexCountChanged: ClassVar[PySide6.QtCore.Signal]
    vertexCountStringChanged: ClassVar[PySide6.QtCore.Signal]
    componentCountsChanged: ClassVar[PySide6.QtCore.Signal]
    primTypeCountsChanged: ClassVar[PySide6.QtCore.Signal]
    detailAttrsChanged: ClassVar[PySide6.QtCore.Signal]
    primitiveAttrsChanged: ClassVar[PySide6.QtCore.Signal]
    pointAttrsChanged: ClassVar[PySide6.QtCore.Signal]
    vertexAttrsChanged: ClassVar[PySide6.QtCore.Signal]
    canShowDiffsChanged: ClassVar[PySide6.QtCore.Signal]
    detailAttrCountChanged: ClassVar[PySide6.QtCore.Signal]
    primitiveAttrCountChanged: ClassVar[PySide6.QtCore.Signal]
    pointAttrCountChanged: ClassVar[PySide6.QtCore.Signal]
    vertexAttrCountChanged: ClassVar[PySide6.QtCore.Signal]
    primGroupsChanged: ClassVar[PySide6.QtCore.Signal]
    pointGroupsChanged: ClassVar[PySide6.QtCore.Signal]
    vertexGroupsChanged: ClassVar[PySide6.QtCore.Signal]
    edgeGroupsChanged: ClassVar[PySide6.QtCore.Signal]
    memoryChanged: ClassVar[PySide6.QtCore.Signal]
    volumesChanged: ClassVar[PySide6.QtCore.Signal]
    debugChangeCountChanged: ClassVar[PySide6.QtCore.Signal]
    debugDetailIDChanged: ClassVar[PySide6.QtCore.Signal]
    debugPrimIDChanged: ClassVar[PySide6.QtCore.Signal]
    debugTopologyIDChanged: ClassVar[PySide6.QtCore.Signal]
    debugChangeCountAlteredChanged: ClassVar[PySide6.QtCore.Signal]
    debugDetailIDAlteredChanged: ClassVar[PySide6.QtCore.Signal]
    debugPrimIDAlteredChanged: ClassVar[PySide6.QtCore.Signal]
    debugTopologyIDAlteredChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, session_id: int = ...) -> None: ...
    def node(self) -> hou.Node | None: ...
    def isEmpty(self) -> bool: ...
    def fillCommonGeoInfo(self, geom: hou.Geometry) -> None: ...
    def fillDetails(self, geom: hou.Geometry, debug: bool = ..., highlight_new: bool = ..., full_diff: bool = ...) -> None: ...
    def stopBackgroundActivity(self) -> None: ...
    def updateVisualizers(self) -> None: ...
    def fillAttrs(self, geom: hou.Geometry, debug: bool = ..., highlight_new: bool = ..., full_diff: bool = ...) -> None: ...
    def fillGroups(self, geom: hou.Geometry, debug: bool = ...) -> None: ...
    def fillVolumes(self, geom: hou.Geometry) -> None: ...
    def recomputeAttrs(self, highlight_new: bool, full_diff: bool, debug: bool) -> None: ...
    @classmethod
    def forNode(cls, node: hou.Node, geo_tree: hou.NodeInfoTree | None, output_index: int, highlight_new: bool = ..., full_diff: bool = ..., debug: bool = ...) -> GeoInfo | None: ...
class SimGeo(core.Info):
    name: str
    geometry: GeoInfo
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    geometryChanged: ClassVar[PySide6.QtCore.Signal]
class SimObject(core.Info):
    path: str
    dataType: str
    geometries: list[SimGeo]
    volumes: list[VolumeInfo]
    created: bool
    pathChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeChanged: ClassVar[PySide6.QtCore.Signal]
    geometriesChanged: ClassVar[PySide6.QtCore.Signal]
    volumesChanged: ClassVar[PySide6.QtCore.Signal]
    createdChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forData(cls, dop_obj: hou.DopObject) -> SimObject: ...
class DopInfo(core.Info):
    simMemoryUsage: int
    simMemoryString: str
    lastTimestepFrame: float
    processedObjectCount: int
    objects: list[SimObject]
    changedOptions: list[LabeledValue]
    simMemoryUsageChanged: ClassVar[PySide6.QtCore.Signal]
    simMemoryStringChanged: ClassVar[PySide6.QtCore.Signal]
    lastTimestepFrameChanged: ClassVar[PySide6.QtCore.Signal]
    processedObjectCountChanged: ClassVar[PySide6.QtCore.Signal]
    objectsChanged: ClassVar[PySide6.QtCore.Signal]
    changedOptionsChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forNode(cls, node: hou.Node) -> DopInfo | None: ...
class UsdPrimCountCategory(core.Info):
    label: str
    counts: list[Number]
    total: int
    totalString: str
    labelChanged: ClassVar[PySide6.QtCore.Signal]
    countsChanged: ClassVar[PySide6.QtCore.Signal]
    totalChanged: ClassVar[PySide6.QtCore.Signal]
    totalStringChanged: ClassVar[PySide6.QtCore.Signal]
class UsdPrimInfo(core.Info):
    path: str
    typeName: str
    kindName: str
    iconName: str
    pathChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    kindNameChanged: ClassVar[PySide6.QtCore.Signal]
    iconNameChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forPrim(cls, prim: Usd.Prim) -> Self: ...
    @classmethod
    def forObject(cls, obj: Usd.Object) -> Self: ...
class UsdPrimCounts(core.Info):
    categorizedPrimCounts: list[UsdPrimCountCategory]
    modelKindCounts: list[Number]
    modelTotal: int
    modelTotalString: str
    subcomponentKindCounts: list[Number]
    subcomponentTotal: int
    subcomponentTotalString: str
    otherKindCounts: list[Number]
    otherTotal: int
    otherTotalString: str
    geometryCounts: list[Number]
    countTimeoutMs: int
    countsTimedOut: bool
    categorizedPrimCountsChanged: ClassVar[PySide6.QtCore.Signal]
    modelKindCountsChanged: ClassVar[PySide6.QtCore.Signal]
    modelTotalChanged: ClassVar[PySide6.QtCore.Signal]
    modelTotalStringChanged: ClassVar[PySide6.QtCore.Signal]
    subcomponentKindCountsChanged: ClassVar[PySide6.QtCore.Signal]
    subcomponentTotalChanged: ClassVar[PySide6.QtCore.Signal]
    subcomponentTotalStringChanged: ClassVar[PySide6.QtCore.Signal]
    otherKindCountsChanged: ClassVar[PySide6.QtCore.Signal]
    otherTotalChanged: ClassVar[PySide6.QtCore.Signal]
    otherTotalStringChanged: ClassVar[PySide6.QtCore.Signal]
    geometryCountsChanged: ClassVar[PySide6.QtCore.Signal]
    countTimeoutMsChanged: ClassVar[PySide6.QtCore.Signal]
    countsTimedOutChanged: ClassVar[PySide6.QtCore.Signal]
    def fillFrom(self, node: hou.LopNode, output_index: int = ..., *, prim_path: str | None = ..., lop_geo_details: bool = ..., kind_details: bool = ..., timeout_ms: int = ...) -> None: ...
class LopInfo(core.Info):
    sessionID: int
    outputIndex: int
    layerCount: int
    layerCountString: str
    loadedPaths: tuple[str, ...] | None
    populatedPaths: tuple[str, ...] | None
    mutedLayers: tuple[str, ...]
    counts: UsdPrimCounts
    modifiedPrims: list[UsdPrimInfo]
    sessionIDChanged: ClassVar[PySide6.QtCore.Signal]
    outputIndexChanged: ClassVar[PySide6.QtCore.Signal]
    layerCountChanged: ClassVar[PySide6.QtCore.Signal]
    layerCountStringChanged: ClassVar[PySide6.QtCore.Signal]
    loadedPathsChanged: ClassVar[PySide6.QtCore.Signal]
    populatedPathsChanged: ClassVar[PySide6.QtCore.Signal]
    mutedLayersChanged: ClassVar[PySide6.QtCore.Signal]
    countsChanged: ClassVar[PySide6.QtCore.Signal]
    modifiedPrimsChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, session_id: int = ...) -> None: ...
    def node(self) -> hou.Node | None: ...
    def fillPrimCounts(self, node: hou.LopNode, output_index: int, *, lop_geo_details: bool = ..., kind_details: bool = ..., timeout_ms: int = ...) -> None: ...
    def recomputeCounts(self, lop_geo_details: bool, timeout_ms: int = ...) -> None: ...
    @classmethod
    def forNode(cls, node: hou.Node, output_index: int, lop_geo_details: bool = ...) -> LopInfo | None: ...
class TopInfo(core.Info):
    filtered: bool
    filterNodes: list[NodeReference]
    stateName: str
    pdgNodeName: str
    count: int
    canceledCount: int
    failedCount: int
    successCount: int
    cachedCount: int
    cookingCount: int
    dirtyCount: int
    scheduledCount: int
    uncookedCount: int
    waitingCount: int
    dirtyTotal: int
    finishedTotal: int
    cookingTotal: int
    successful: bool
    failed: bool
    finishedFraction: float
    cookingFraction: float
    failedFraction: float
    totalGenerateTime: float
    totalGenerateTimeStr: str
    totalCookTime: float
    totalCookTimeStr: str
    averageCookTime: float
    averageCookTimeStr: str
    timeSlices: list[float]
    serviceTypeNames: list[str]
    isStandardScript: bool
    jobCommand: str
    outputFiles: list[tops.FileInfo]
    outputFilesText: str
    attributes: tops.PdgAttrProxyModel
    attributeCount: int
    maxAttrNameChars: int
    maxAttrCountChars: int
    filteredChanged: ClassVar[PySide6.QtCore.Signal]
    filterNodesChanged: ClassVar[PySide6.QtCore.Signal]
    stateNameChanged: ClassVar[PySide6.QtCore.Signal]
    pdgNodeNameChanged: ClassVar[PySide6.QtCore.Signal]
    countChanged: ClassVar[PySide6.QtCore.Signal]
    canceledCountChanged: ClassVar[PySide6.QtCore.Signal]
    failedCountChanged: ClassVar[PySide6.QtCore.Signal]
    successCountChanged: ClassVar[PySide6.QtCore.Signal]
    cachedCountChanged: ClassVar[PySide6.QtCore.Signal]
    cookingCountChanged: ClassVar[PySide6.QtCore.Signal]
    dirtyCountChanged: ClassVar[PySide6.QtCore.Signal]
    scheduledCountChanged: ClassVar[PySide6.QtCore.Signal]
    uncookedCountChanged: ClassVar[PySide6.QtCore.Signal]
    waitingCountChanged: ClassVar[PySide6.QtCore.Signal]
    dirtyTotalChanged: ClassVar[PySide6.QtCore.Signal]
    finishedTotalChanged: ClassVar[PySide6.QtCore.Signal]
    cookingTotalChanged: ClassVar[PySide6.QtCore.Signal]
    successfulChanged: ClassVar[PySide6.QtCore.Signal]
    failedChanged: ClassVar[PySide6.QtCore.Signal]
    finishedFractionChanged: ClassVar[PySide6.QtCore.Signal]
    cookingFractionChanged: ClassVar[PySide6.QtCore.Signal]
    failedFractionChanged: ClassVar[PySide6.QtCore.Signal]
    totalGenerateTimeChanged: ClassVar[PySide6.QtCore.Signal]
    totalGenerateTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    totalCookTimeChanged: ClassVar[PySide6.QtCore.Signal]
    totalCookTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    averageCookTimeChanged: ClassVar[PySide6.QtCore.Signal]
    averageCookTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    timeSlicesChanged: ClassVar[PySide6.QtCore.Signal]
    serviceTypeNamesChanged: ClassVar[PySide6.QtCore.Signal]
    isStandardScriptChanged: ClassVar[PySide6.QtCore.Signal]
    jobCommandChanged: ClassVar[PySide6.QtCore.Signal]
    outputFilesChanged: ClassVar[PySide6.QtCore.Signal]
    outputFilesTextChanged: ClassVar[PySide6.QtCore.Signal]
    attributesChanged: ClassVar[PySide6.QtCore.Signal]
    attributeCountChanged: ClassVar[PySide6.QtCore.Signal]
    maxAttrNameCharsChanged: ClassVar[PySide6.QtCore.Signal]
    maxAttrCountCharsChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forNode(cls, node: hou.Node, output_index: int | None) -> TopInfo | None: ...
class CopLayer(core.Info):
    outputIndex: int
    name: str
    label: str
    valid: bool
    resolution: PySide6.QtCore.QSize
    resolutionString: str
    oddResolution: bool
    dataRect: PySide6.QtCore.QRect
    dataRectString: str
    dataIsOffset: bool
    dataIsSized: bool
    displayRect: PySide6.QtCore.QRect
    displayRectString: str
    displayIsOffset: bool
    displayIsSized: bool
    onGPU: bool
    onCPU: bool
    storageTypeName: str
    isInt: bool
    storageTypeBriefName: str
    borderTypeName: str
    dataType: str
    visualizationName: str
    isConstant: bool
    channelCount: int
    pixelScale: list[float]
    pixelScaleString: str
    aspectRatio: float
    clipNear: float
    clipFar: float
    projectionName: str
    aperture: float
    focalLength: float
    cameraPos: list[float]
    imageDistance: float
    fStop: float
    focusDistance: float
    cameraIsDefault: bool
    attributes: list[LabeledValue]
    imageXform: Xform
    geometry: GeoInfo
    isVDB: bool
    leafCount: int
    voxelCount: int
    voxelCountStr: str
    voxelSize: tuple[float, float, float]
    voxelSizeStr: str
    voxelResolution: tuple[int, ...]
    voxelResolutionStr: str
    isAttrib: bool
    length: int
    lengthStr: str
    tupleSize: int
    owner: str
    thumbnail: PySide6.QtGui.QPixmap
    subWires: list[CopCableWire]
    outputIndexChanged: ClassVar[PySide6.QtCore.Signal]
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    labelChanged: ClassVar[PySide6.QtCore.Signal]
    validChanged: ClassVar[PySide6.QtCore.Signal]
    resolutionChanged: ClassVar[PySide6.QtCore.Signal]
    resolutionStringChanged: ClassVar[PySide6.QtCore.Signal]
    oddResolutionChanged: ClassVar[PySide6.QtCore.Signal]
    dataRectChanged: ClassVar[PySide6.QtCore.Signal]
    dataRectStringChanged: ClassVar[PySide6.QtCore.Signal]
    dataIsOffsetChanged: ClassVar[PySide6.QtCore.Signal]
    dataIsSizedChanged: ClassVar[PySide6.QtCore.Signal]
    displayRectChanged: ClassVar[PySide6.QtCore.Signal]
    displayRectStringChanged: ClassVar[PySide6.QtCore.Signal]
    displayIsOffsetChanged: ClassVar[PySide6.QtCore.Signal]
    displayIsSizedChanged: ClassVar[PySide6.QtCore.Signal]
    onGPUChanged: ClassVar[PySide6.QtCore.Signal]
    onCPUChanged: ClassVar[PySide6.QtCore.Signal]
    storageTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    isIntChanged: ClassVar[PySide6.QtCore.Signal]
    storageTypeBriefNameChanged: ClassVar[PySide6.QtCore.Signal]
    borderTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeChanged: ClassVar[PySide6.QtCore.Signal]
    visualizationNameChanged: ClassVar[PySide6.QtCore.Signal]
    isConstantChanged: ClassVar[PySide6.QtCore.Signal]
    channelCountChanged: ClassVar[PySide6.QtCore.Signal]
    pixelScaleChanged: ClassVar[PySide6.QtCore.Signal]
    pixelScaleStringChanged: ClassVar[PySide6.QtCore.Signal]
    aspectRatioChanged: ClassVar[PySide6.QtCore.Signal]
    clipNearChanged: ClassVar[PySide6.QtCore.Signal]
    clipFarChanged: ClassVar[PySide6.QtCore.Signal]
    projectionNameChanged: ClassVar[PySide6.QtCore.Signal]
    apertureChanged: ClassVar[PySide6.QtCore.Signal]
    focalLengthChanged: ClassVar[PySide6.QtCore.Signal]
    cameraPosChanged: ClassVar[PySide6.QtCore.Signal]
    imageDistanceChanged: ClassVar[PySide6.QtCore.Signal]
    fStopChanged: ClassVar[PySide6.QtCore.Signal]
    focusDistanceChanged: ClassVar[PySide6.QtCore.Signal]
    cameraIsDefaultChanged: ClassVar[PySide6.QtCore.Signal]
    attributesChanged: ClassVar[PySide6.QtCore.Signal]
    imageXformChanged: ClassVar[PySide6.QtCore.Signal]
    geometryChanged: ClassVar[PySide6.QtCore.Signal]
    isVDBChanged: ClassVar[PySide6.QtCore.Signal]
    leafCountChanged: ClassVar[PySide6.QtCore.Signal]
    voxelCountChanged: ClassVar[PySide6.QtCore.Signal]
    voxelCountStrChanged: ClassVar[PySide6.QtCore.Signal]
    voxelSizeChanged: ClassVar[PySide6.QtCore.Signal]
    voxelSizeStrChanged: ClassVar[PySide6.QtCore.Signal]
    voxelResolutionChanged: ClassVar[PySide6.QtCore.Signal]
    voxelResolutionStrChanged: ClassVar[PySide6.QtCore.Signal]
    isAttribChanged: ClassVar[PySide6.QtCore.Signal]
    lengthChanged: ClassVar[PySide6.QtCore.Signal]
    lengthStrChanged: ClassVar[PySide6.QtCore.Signal]
    tupleSizeChanged: ClassVar[PySide6.QtCore.Signal]
    ownerChanged: ClassVar[PySide6.QtCore.Signal]
    thumbnailChanged: ClassVar[PySide6.QtCore.Signal]
    subWiresChanged: ClassVar[PySide6.QtCore.Signal]
    @staticmethod
    def rectToString(rect: PySide6.QtCore.QRect) -> str: ...
    @staticmethod
    def sizeToString(size: PySide6.QtCore.QSizeF | PySide6.QtCore.QSize) -> str: ...
    def setAttrs(self, attrs: Mapping[str, str]) -> None: ...
    def fillFromVDB(self, vdb: hou.NanoVDB) -> None: ...
    def fillFromAttribute(self, attrib: hou.DetachedAttrib) -> None: ...
    def fillFromLayer(self, layer: hou.ImageLayer) -> None: ...
class CopCableWire(core.Info):
    name: str
    dataTypeName: str
    appearanceIndex: int
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    dataTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    appearanceIndexChanged: ClassVar[PySide6.QtCore.Signal]
class CopInfo(core.Info):
    resolution: PySide6.QtCore.QSize
    resolutionString: str
    mixedResolutions: bool
    layers: list[CopLayer]
    thumbnail: PySide6.QtGui.QPixmap
    viewOutput: int
    resolutionChanged: ClassVar[PySide6.QtCore.Signal]
    resolutionStringChanged: ClassVar[PySide6.QtCore.Signal]
    mixedResolutionsChanged: ClassVar[PySide6.QtCore.Signal]
    layersChanged: ClassVar[PySide6.QtCore.Signal]
    thumbnailChanged: ClassVar[PySide6.QtCore.Signal]
    viewOutputChanged: ClassVar[PySide6.QtCore.Signal]
    def flagChanged(self, node: hou.OpNode) -> None: ...
    @classmethod
    def forNode(cls, node: hou.Node, output_names: Sequence[str], output_labels: Sequence[str], output_index: int | None) -> CopInfo | None: ...
class RopInfo(core.Info):
    ...
class LabeledValue(core.Info):
    label: str
    text: str
    labelColor: PySide6.QtGui.QColor
    textColor: PySide6.QtGui.QColor
    monospaced: bool
    link: str
    format: str
    labelChanged: ClassVar[PySide6.QtCore.Signal]
    textChanged: ClassVar[PySide6.QtCore.Signal]
    labelColorChanged: ClassVar[PySide6.QtCore.Signal]
    textColorChanged: ClassVar[PySide6.QtCore.Signal]
    monospacedChanged: ClassVar[PySide6.QtCore.Signal]
    linkChanged: ClassVar[PySide6.QtCore.Signal]
    formatChanged: ClassVar[PySide6.QtCore.Signal]
class NodeReference(core.Info):
    name: str
    path: str
    iconName: str
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    pathChanged: ClassVar[PySide6.QtCore.Signal]
    iconNameChanged: ClassVar[PySide6.QtCore.Signal]
    @classmethod
    def forNode(cls, node: hou.Node) -> NodeReference: ...
class NodeSpecificRow(core.Info):
    label: str
    text: str
    visible: bool
    labelChanged: ClassVar[PySide6.QtCore.Signal]
    textChanged: ClassVar[PySide6.QtCore.Signal]
    visibleChanged: ClassVar[PySide6.QtCore.Signal]
class NodeOutput(core.Info):
    index: int
    internalName: str
    label: str
    indexChanged: ClassVar[PySide6.QtCore.Signal]
    internalNameChanged: ClassVar[PySide6.QtCore.Signal]
    labelChanged: ClassVar[PySide6.QtCore.Signal]
class NodeInfo(core.Info):
    sessionID: int
    name: str
    path: str
    parentPath: str
    className: str
    categoryName: str
    typeName: str
    typeNameWithCategory: str
    typeDesc: str
    iconName: str
    iconPixmap: PySide6.QtGui.QPixmap
    color: PySide6.QtGui.QColor
    colorIsDefault: bool
    comment: str
    displayComment: bool
    namespace: str
    basename: str
    version: str
    summary: str
    outputs: list[NodeOutput]
    outputLabels: tuple[str, ...]
    currentOutputIndex: int
    currentOutputName: str | None
    incomingParmRefs: list[str]
    outgoingNodePaths: list[str]
    isBypassed: bool
    timeDependent: bool
    isAsset: bool
    matchesCurrent: bool
    creationTime: PySide6.QtCore.QDateTime
    creationTimeString: str
    baseTime: PySide6.QtCore.QDateTime
    modificationTime: PySide6.QtCore.QDateTime
    modificationTimeString: str
    userData: list[LabeledValue]
    assetComment: str
    definedBy: str | None
    definedInHFS: bool | None
    debug: bool
    errors: list[Message]
    warnings: list[Message]
    messages: list[Message]
    subnetOutputs: list[str]
    cookCount: int
    lastCookTime: float
    lastCookTimeString: str
    perfStats: PerfStats | None
    nodeSpecificBranchName: str
    nodeSpecificRows: list[LabeledValue]
    geometry: GeoInfo | None
    objInfo: ObjInfo | None
    dopInfo: DopInfo | None
    lopInfo: LopInfo | None
    topInfo: TopInfo | None
    copInfo: CopInfo | None
    ropInfo: RopInfo | None
    chopInfo: ChopInfo | None
    customTags: list[custom.CustomTag]
    customTop: list[custom.CustomContainer]
    customMiddle: list[custom.CustomContainer]
    customBottom: list[custom.CustomContainer]
    sessionIDChanged: ClassVar[PySide6.QtCore.Signal]
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    pathChanged: ClassVar[PySide6.QtCore.Signal]
    parentPathChanged: ClassVar[PySide6.QtCore.Signal]
    classNameChanged: ClassVar[PySide6.QtCore.Signal]
    categoryNameChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameWithCategoryChanged: ClassVar[PySide6.QtCore.Signal]
    typeDescChanged: ClassVar[PySide6.QtCore.Signal]
    iconNameChanged: ClassVar[PySide6.QtCore.Signal]
    iconPixmapChanged: ClassVar[PySide6.QtCore.Signal]
    colorChanged: ClassVar[PySide6.QtCore.Signal]
    colorIsDefaultChanged: ClassVar[PySide6.QtCore.Signal]
    commentChanged: ClassVar[PySide6.QtCore.Signal]
    displayCommentChanged: ClassVar[PySide6.QtCore.Signal]
    namespaceChanged: ClassVar[PySide6.QtCore.Signal]
    basenameChanged: ClassVar[PySide6.QtCore.Signal]
    versionChanged: ClassVar[PySide6.QtCore.Signal]
    summaryChanged: ClassVar[PySide6.QtCore.Signal]
    outputsChanged: ClassVar[PySide6.QtCore.Signal]
    outputLabelsChanged: ClassVar[PySide6.QtCore.Signal]
    currentOutputIndexChanged: ClassVar[PySide6.QtCore.Signal]
    currentOutputNameChanged: ClassVar[PySide6.QtCore.Signal]
    incomingParmRefsChanged: ClassVar[PySide6.QtCore.Signal]
    outgoingNodePathsChanged: ClassVar[PySide6.QtCore.Signal]
    isBypassedChanged: ClassVar[PySide6.QtCore.Signal]
    timeDependentChanged: ClassVar[PySide6.QtCore.Signal]
    isAssetChanged: ClassVar[PySide6.QtCore.Signal]
    matchesCurrentChanged: ClassVar[PySide6.QtCore.Signal]
    creationTimeChanged: ClassVar[PySide6.QtCore.Signal]
    creationTimeStringChanged: ClassVar[PySide6.QtCore.Signal]
    baseTimeChanged: ClassVar[PySide6.QtCore.Signal]
    modificationTimeChanged: ClassVar[PySide6.QtCore.Signal]
    modificationTimeStringChanged: ClassVar[PySide6.QtCore.Signal]
    userDataChanged: ClassVar[PySide6.QtCore.Signal]
    assetCommentChanged: ClassVar[PySide6.QtCore.Signal]
    definedByChanged: ClassVar[PySide6.QtCore.Signal]
    definedInHFSChanged: ClassVar[PySide6.QtCore.Signal]
    debugChanged: ClassVar[PySide6.QtCore.Signal]
    errorsChanged: ClassVar[PySide6.QtCore.Signal]
    warningsChanged: ClassVar[PySide6.QtCore.Signal]
    messagesChanged: ClassVar[PySide6.QtCore.Signal]
    subnetOutputsChanged: ClassVar[PySide6.QtCore.Signal]
    cookCountChanged: ClassVar[PySide6.QtCore.Signal]
    lastCookTimeChanged: ClassVar[PySide6.QtCore.Signal]
    lastCookTimeStringChanged: ClassVar[PySide6.QtCore.Signal]
    perfStatsChanged: ClassVar[PySide6.QtCore.Signal]
    nodeSpecificBranchNameChanged: ClassVar[PySide6.QtCore.Signal]
    nodeSpecificRowsChanged: ClassVar[PySide6.QtCore.Signal]
    geometryChanged: ClassVar[PySide6.QtCore.Signal]
    objInfoChanged: ClassVar[PySide6.QtCore.Signal]
    dopInfoChanged: ClassVar[PySide6.QtCore.Signal]
    lopInfoChanged: ClassVar[PySide6.QtCore.Signal]
    topInfoChanged: ClassVar[PySide6.QtCore.Signal]
    copInfoChanged: ClassVar[PySide6.QtCore.Signal]
    ropInfoChanged: ClassVar[PySide6.QtCore.Signal]
    chopInfoChanged: ClassVar[PySide6.QtCore.Signal]
    customTagsChanged: ClassVar[PySide6.QtCore.Signal]
    customTopChanged: ClassVar[PySide6.QtCore.Signal]
    customMiddleChanged: ClassVar[PySide6.QtCore.Signal]
    customBottomChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, session_id: int) -> None: ...
    def node(self) -> hou.OpNode | None: ...
    def setAttrVisualized(self, type_name: str, name: str, active: bool, open_settings: bool) -> None: ...
    def setVolumeVisualized(self, prim_num: int, name: str, active: bool, open_settings: bool) -> None: ...
    def setGroupVisualized(self, type_name: str, name: str, active: bool) -> None: ...
    def parm(self, name: str) -> hou.Parm | None: ...
    def floatParm(self, name: str) -> float | None: ...
    def intParm(self, name: str) -> int | None: ...
    def stringParm(self, name: str) -> str | None: ...
    def setCommentText(self, text: str) -> None: ...
    def setCommentVisible(self, visible: bool) -> None: ...
    def flagChanged(self) -> None: ...
    def stopBackgroundActivity(self) -> None: ...
    def setFrom(self, node: hou.OpNode, recook: bool = ..., output_index: int | None = ..., highlight_new: bool = ..., compare_attrs: bool = ..., debug: bool = ..., include_help: bool = ..., include_lop_geo_details: bool = ..., theme: colors.Theme | None = ...) -> None: ...
