import PySide6.QtCore
import hou
import pathlib
import pdg
import re
from . import window as window
from .general import naturalSortKey as naturalSortKey
from _typeshed import Incomplete
from collections.abc import Iterator
from hutil.PySide import QtCore as QtCore
from hutil.PySide.QtCore import Qt as Qt
from hutil.formatting import format_duration as format_duration, format_time as format_time
from hutil.qt.common import core as core
from hutil.qt.common.qmlviews import SST as SST
from hutil.qt.info.window import _BaseInfoStateKwargs
from hutil.qt.pluto import colors as colors
from typing import Any, ClassVar, Iterable, NamedTuple
from typing_extensions import Unpack

from typing import TypeAlias
AttribTypes: TypeAlias = pdg.AttributeFile | pdg.AttributeInt | pdg.AttributeFloat | pdg.AttributeString | pdg.AttributePyObject | pdg.AttributeDictionary | pdg.AttributeGeometry
pdg_type_registry: pdg.TypeRegistry
ws_expr: re.Pattern[str]
type_name: dict[type, str]
cache_state_label: dict[str, str]
NODE_EVENTS: tuple[hou.EnumValue[hou.nodeEventType]]
current_workitem_win: WorkItemViewWindow | None
log_expr: re.Pattern[str]

def getWorkItem(node: hou.TopNode, id: int) -> pdg.WorkItem | None: ...
def log_styler(m: re.Match[str]) -> str: ...
def format_timestamp(ts: float) -> str: ...
def delta(start: float, end: float, places: int = 3) -> float: ...
def getPdgWorkItem(context_name: str, pdg_node_name: str, item_name: str) -> tuple[hou.TopNode, pdg.WorkItem] | None: ...
def selectPdgWorkItem(context_name: str, pdg_node_name: str, item_name: str, editor: hou.NetworkEditor | None = None) -> tuple[hou.TopNode, pdg.WorkItem] | None: ...
def readFromURL(scheduler: pdg.SchedulerBase | None, url: PySide6.QtCore.QUrl) -> str: ...

class WorkItemStatus(NamedTuple):
    context_name: str
    node_name: str
    name: str
    frame: float
    cache_state: pdg.workItemCacheState
    @classmethod
    def ofWorkItem(cls, workitem: pdg.WorkItem) -> WorkItemStatus: ...

class WorkItemReference(core.Info):
    contextNameChanged: ClassVar[PySide6.QtCore.Signal]
    nodeNameChanged: ClassVar[PySide6.QtCore.Signal]
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    linkChanged: ClassVar[PySide6.QtCore.Signal]
    successfulChanged: ClassVar[PySide6.QtCore.Signal]
    failedChanged: ClassVar[PySide6.QtCore.Signal]
    contextName: str
    nodeName: str
    name: str
    link: str
    successful: bool
    failed: bool
    @classmethod
    def forWorkItem(cls, ctx_name: str, workitem: pdg.WorkItem) -> WorkItemReference: ...

class AttribInfo(core.Info):
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    previewChanged: ClassVar[PySide6.QtCore.Signal]
    valueChanged: ClassVar[PySide6.QtCore.Signal]
    numberChanged: ClassVar[PySide6.QtCore.Signal]
    inheritedChanged: ClassVar[PySide6.QtCore.Signal]
    noCopyChanged: ClassVar[PySide6.QtCore.Signal]
    internalChanged: ClassVar[PySide6.QtCore.Signal]
    countChanged: ClassVar[PySide6.QtCore.Signal]
    transferredChanged: ClassVar[PySide6.QtCore.Signal]
    timeDependentChanged: ClassVar[PySide6.QtCore.Signal]
    matchesChanged: ClassVar[PySide6.QtCore.Signal]
    fileInfoChanged: ClassVar[PySide6.QtCore.Signal]
    isNodeLinkChanged: ClassVar[PySide6.QtCore.Signal]
    isTimestampChanged: ClassVar[PySide6.QtCore.Signal]
    isMemorySizeChanged: ClassVar[PySide6.QtCore.Signal]
    timestampChanged: ClassVar[PySide6.QtCore.Signal]
    name: str
    typeName: str
    preview: str
    value: str
    number: float
    inherited: bool
    noCopy: bool
    internal: bool
    count: int
    transferred: bool
    timeDependent: bool
    matches: bool
    fileInfo: FileInfo | None
    isNodeLink: bool
    isTimestamp: bool
    isMemorySize: bool
    timestamp: PySide6.QtCore.QDateTime
    @classmethod
    def forAttrib(cls, attrib: AttribTypes, time_dependent: bool = False) -> AttribInfo: ...

class SimpleInfoModel(QtCore.QAbstractListModel):
    displayRoleName: str
    ModelData: PySide6.QtCore.Qt.ItemDataRole
    countChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def setItems(self, items: Iterable[core.Info]) -> None: ...
    def rowCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = None) -> int: ...
    def count(self) -> int: ...
    def roleNames(self) -> dict[int, bytes]: ...
    def data(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int = 0) -> Any: ...

class PdgPartitionModel(SimpleInfoModel):
    infoClass: type[WorkItemReference]

class PdgAttributeModel(SimpleInfoModel):
    infoClass: type[AttribInfo]
    maxAttrNameCharsChanged: ClassVar[PySide6.QtCore.Signal]
    maxAttrCountCharsChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def __iter__(self) -> Iterator[AttribInfo]: ...
    def setAttrsFrom(self, owner: pdg.AttributeOwner, force: bool = False) -> None: ...
    def maxAttrNameChars(self) -> int: ...
    def maxAttrCountChars(self) -> int: ...

class PdgAttrProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def setAttrsFrom(self, owner: pdg.AttributeOwner, force: bool = False) -> None: ...
    def setDebug(self, debug: bool) -> None: ...
    def setGroupByType(self, group_by_type: bool) -> None: ...
    def setShowInherited(self, show_inherited: bool) -> None: ...
    def setShowNoCopy(self, show_nocopy: bool) -> None: ...
    def setFiltered(self, filtered: bool) -> None: ...
    def patternIsValid(self) -> bool: ...
    def patternError(self) -> str: ...
    def matchCount(self) -> int: ...
    def lessThan(self, a: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, b: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> bool: ...
    def setFilter(self, workitem: pdg.WorkItem, filter_text: str) -> None: ...
    def filterAcceptsRow(self, src_row: int, src_parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> bool: ...

class FileInfo(core.Info):
    pathChanged: ClassVar[PySide6.QtCore.Signal]
    localPathChanged: ClassVar[PySide6.QtCore.Signal]
    urlChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    sizeChanged: ClassVar[PySide6.QtCore.Signal]
    tagChanged: ClassVar[PySide6.QtCore.Signal]
    expectedChanged: ClassVar[PySide6.QtCore.Signal]
    viewableChanged: ClassVar[PySide6.QtCore.Signal]
    path: str
    localPath: str
    url: PySide6.QtCore.QUrl
    typeName: str
    size: int
    tag: str
    expected: bool
    viewable: bool
    @classmethod
    def fromPdgFile(cls, file: pdg.File, hip_dir: pathlib.Path | None = None, expected: bool = False) -> FileInfo: ...

class WorkItemInfo(core.Info):
    idChanged: ClassVar[PySide6.QtCore.Signal]
    nameChanged: ClassVar[PySide6.QtCore.Signal]
    nodeNameChanged: ClassVar[PySide6.QtCore.Signal]
    contextNameChanged: ClassVar[PySide6.QtCore.Signal]
    labelChanged: ClassVar[PySide6.QtCore.Signal]
    topNameChanged: ClassVar[PySide6.QtCore.Signal]
    topIconChanged: ClassVar[PySide6.QtCore.Signal]
    typeNameChanged: ClassVar[PySide6.QtCore.Signal]
    inProcessChanged: ClassVar[PySide6.QtCore.Signal]
    indexChanged: ClassVar[PySide6.QtCore.Signal]
    priorityChanged: ClassVar[PySide6.QtCore.Signal]
    frameChanged: ClassVar[PySide6.QtCore.Signal]
    stateNameChanged: ClassVar[PySide6.QtCore.Signal]
    successfulChanged: ClassVar[PySide6.QtCore.Signal]
    failedChanged: ClassVar[PySide6.QtCore.Signal]
    dependencyStateNameChanged: ClassVar[PySide6.QtCore.Signal]
    failedDependenciesChanged: ClassVar[PySide6.QtCore.Signal]
    cacheStateNameChanged: ClassVar[PySide6.QtCore.Signal]
    cacheStateLabelChanged: ClassVar[PySide6.QtCore.Signal]
    batchNameChanged: ClassVar[PySide6.QtCore.Signal]
    batchIndexChanged: ClassVar[PySide6.QtCore.Signal]
    partitionItemsChanged: ClassVar[PySide6.QtCore.Signal]
    cookTypeNameChanged: ClassVar[PySide6.QtCore.Signal]
    commandChanged: ClassVar[PySide6.QtCore.Signal]
    hasPlatformCommandChanged: ClassVar[PySide6.QtCore.Signal]
    linuxCommandChanged: ClassVar[PySide6.QtCore.Signal]
    macCommandChanged: ClassVar[PySide6.QtCore.Signal]
    windowsCommandChanged: ClassVar[PySide6.QtCore.Signal]
    schedulerNameChanged: ClassVar[PySide6.QtCore.Signal]
    schedulerTopPathChanged: ClassVar[PySide6.QtCore.Signal]
    schedulerTopIconChanged: ClassVar[PySide6.QtCore.Signal]
    schedulerIconChanged: ClassVar[PySide6.QtCore.Signal]
    statusURLChanged: ClassVar[PySide6.QtCore.Signal]
    logURLChanged: ClassVar[PySide6.QtCore.Signal]
    logTextChanged: ClassVar[PySide6.QtCore.Signal]
    logHTMLChanged: ClassVar[PySide6.QtCore.Signal]
    percentDoneChanged: ClassVar[PySide6.QtCore.Signal]
    pythonModuleNameChanged: ClassVar[PySide6.QtCore.Signal]
    onMainThreadChanged: ClassVar[PySide6.QtCore.Signal]
    serviceNameChanged: ClassVar[PySide6.QtCore.Signal]
    serviceClientChanged: ClassVar[PySide6.QtCore.Signal]
    queueTimeChanged: ClassVar[PySide6.QtCore.Signal]
    queueTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    scheduleTimeChanged: ClassVar[PySide6.QtCore.Signal]
    scheduleTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    startTimeChanged: ClassVar[PySide6.QtCore.Signal]
    startTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    endTimeChanged: ClassVar[PySide6.QtCore.Signal]
    endTimeStrChanged: ClassVar[PySide6.QtCore.Signal]
    queueSecondsChanged: ClassVar[PySide6.QtCore.Signal]
    queueSecondsStrChanged: ClassVar[PySide6.QtCore.Signal]
    scheduleSecondsChanged: ClassVar[PySide6.QtCore.Signal]
    scheduleSecondsStrChanged: ClassVar[PySide6.QtCore.Signal]
    runSecondsChanged: ClassVar[PySide6.QtCore.Signal]
    runSecondsStrChanged: ClassVar[PySide6.QtCore.Signal]
    totalSecondsChanged: ClassVar[PySide6.QtCore.Signal]
    totalSecondsStrChanged: ClassVar[PySide6.QtCore.Signal]
    inputFilesChanged: ClassVar[PySide6.QtCore.Signal]
    inputFilesTextChanged: ClassVar[PySide6.QtCore.Signal]
    outputFilesChanged: ClassVar[PySide6.QtCore.Signal]
    outputFilesTextChanged: ClassVar[PySide6.QtCore.Signal]
    expectedCountChanged: ClassVar[PySide6.QtCore.Signal]
    transferOutputsChanged: ClassVar[PySide6.QtCore.Signal]
    patternIsValidChanged: ClassVar[PySide6.QtCore.Signal]
    patternErrorChanged: ClassVar[PySide6.QtCore.Signal]
    filterMatchCountChanged: ClassVar[PySide6.QtCore.Signal]
    attributesChanged: ClassVar[PySide6.QtCore.Signal]
    attributeCountChanged: ClassVar[PySide6.QtCore.Signal]
    maxAttrNameCharsChanged: ClassVar[PySide6.QtCore.Signal]
    maxAttrCountCharsChanged: ClassVar[PySide6.QtCore.Signal]
    id: int
    name: str
    nodeName: str
    contextName: str
    label: str
    topName: str
    topIcon: str
    typeName: str
    inProcess: bool
    index: int
    priority: int
    frame: float
    stateName: str
    successful: bool
    failed: bool
    dependencyStateName: str
    failedDependencies: list[WorkItemReference]
    cacheStateName: str
    cacheStateLabel: str
    batchName: str
    batchIndex: int
    partitionItems: PdgPartitionModel
    cookTypeName: str
    command: str
    hasPlatformCommand: bool
    linuxCommand: str
    macCommand: str
    windowsCommand: str
    schedulerName: str
    schedulerTopPath: str
    schedulerTopIcon: str
    schedulerIcon: str
    statusURL: PySide6.QtCore.QUrl
    logURL: PySide6.QtCore.QUrl
    logText: str
    logHTML: str
    percentDone: float
    pythonModuleName: str
    onMainThread: bool
    serviceName: str
    serviceClient: str
    queueTime: float
    queueTimeStr: str
    scheduleTime: float
    scheduleTimeStr: str
    startTime: float
    startTimeStr: str
    endTime: float
    endTimeStr: str
    queueSeconds: float
    queueSecondsStr: str
    scheduleSeconds: float
    scheduleSecondsStr: str
    runSeconds: float
    runSecondsStr: str
    totalSeconds: float
    totalSecondsStr: str
    inputFiles: list[FileInfo]
    inputFilesText: str
    outputFiles: list[FileInfo]
    outputFilesText: str
    expectedCount: int
    transferOutputs: bool
    patternIsValid: bool
    patternError: str
    filterMatchCount: int
    attributes: PdgAttrProxyModel
    attributeCount: int
    maxAttrNameChars: int
    maxAttrCountChars: int
    def __init__(self, **kwargs: object) -> None: ...
    def graphContext(self) -> pdg.GraphContext | None: ...
    def scheduler(self) -> pdg.SchedulerBase | None: ...
    def workItem(self) -> pdg.WorkItem | None: ...
    def shouldUpdateLog(self) -> bool: ...
    def logInMemory(self) -> bool: ...
    def clear(self) -> None: ...
    def setFrom(self, node: hou.TopNode | None, workitem: pdg.WorkItem, group_attrs_by_type: bool = False, debug: bool = False) -> None: ...
    def setFilesFrom(self, workitem: pdg.WorkItem) -> None: ...
    def setAttrsFrom(self, workitem: pdg.WorkItem, group_by_type: bool = False, force: bool = False, debug: bool = False) -> None: ...
    def setTimingsFrom(self, stats: pdg.WorkItemStats) -> None: ...
    def updateLog(self, scheduler: pdg.SchedulerBase | None = None, workitem: pdg.WorkItem | None = None) -> None: ...

class WorkItemConfig(window.NodeInfoConfig):
    workItemThemeNameChanged: ClassVar[PySide6.QtCore.Signal]
    showInheritedWorkItemAttrsChanged: ClassVar[PySide6.QtCore.Signal]
    showNoCopyWorkItemAttrsChanged: ClassVar[PySide6.QtCore.Signal]
    localizePdgPathsChanged: ClassVar[PySide6.QtCore.Signal]
    groupAttrsByTypeChanged: ClassVar[PySide6.QtCore.Signal]
    workItemThemeName: str
    showInheritedWorkItemAttrs: bool
    showNoCopyWorkItemAttrs: bool
    localizePdgPaths: bool
    groupAttrsByType: bool

class WorkItemState(window.BaseInfoState[WorkItemConfig, WorkItemInfo]):
    filteringChanged: ClassVar[PySide6.QtCore.Signal]
    filterTextChanged: ClassVar[PySide6.QtCore.Signal]
    filtering: bool
    filterText: str
    workItemSelected: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, **kwargs: Unpack[_BaseInfoStateKwargs]) -> None: ...
    def outOfDate(self) -> bool: ...
    def openFile(self, url: PySide6.QtCore.QUrl, tag: str) -> None: ...
    def saveText(self, text: str) -> None: ...
    def clearWorkItem(self) -> None: ...
    def setWorkItem(self, top_node: hou.TopNode | None, workitem: int | pdg.WorkItem | None) -> None: ...
    def selectNextWorkItem(self) -> None: ...
    def selectPreviousWorkItem(self) -> None: ...
    def topNet(self) -> hou.OpNode | None: ...
    def topNode(self) -> hou.TopNode | None: ...
    def workItemID(self) -> int: ...
    def workItem(self) -> pdg.WorkItem | None: ...
    def isUpdatable(self) -> bool: ...
    def reload(self, recook: bool = False, force_update: bool = False) -> None: ...

class WorkItemViewWindow(window.InfoViewWindow[WorkItemState]):
    SOURCE_URL: str
    def isTransient(self) -> bool: ...
    def topNode(self) -> hou.TopNode | None: ...
    def workItemID(self) -> int: ...
    def pathKey(self) -> str: ...
    def display(self, node: hou.TopNode | None, workitem_id: int | None, pos: PySide6.QtCore.QPoint | None = None, interactive: bool = True, editor: hou.NetworkEditor | None = None) -> None: ...

def createWorkItemInfoWindow(node: hou.TopNode, workitem_id: int | None = None, interactive: bool = True, editor: hou.NetworkEditor | None = None, pos: PySide6.QtCore.QPoint | None = None, delete_on_close: bool = False) -> WorkItemViewWindow: ...
def toggleWorkItemInfoWindow(node: hou.TopNode, workitem_id: int, show: bool = True, interactive: bool = True, editor: hou.NetworkEditor | None = None, pos: PySide6.QtCore.QPoint | None = None) -> WorkItemViewWindow | None: ...
